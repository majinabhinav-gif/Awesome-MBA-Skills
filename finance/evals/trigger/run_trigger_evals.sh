#!/usr/bin/env bash
# run_trigger_evals.sh — skill-trigger accuracy harness for the finance-skills
# collision clusters, based on the agentskills.io trigger-testing pattern.
#
# For each query in queries.json this script runs `claude -p "<query>"
# --output-format json` RUNS_PER_QUERY times, detects which skills (if any)
# Claude invoked via the Skill tool, and computes per-query trigger rates.
#
# !!! COST WARNING !!!
# With the shipped queries.json (133 queries x 3 runs) this performs
# ~399 full `claude -p` invocations. Each one is a complete model call.
# Do NOT run this casually; use --cluster and --limit to scope a run.
#
# Usage:
#   ./run_trigger_evals.sh [--cluster <name>] [--runs N] [--limit N] [--out FILE]
#
# Requirements: bash 3.2+, python3, claude CLI on PATH, and the finance
# skills installed in the working project (see README.md).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
QUERIES_FILE="$SCRIPT_DIR/queries.json"
RUNS_PER_QUERY=3
CLUSTER_FILTER=""
LIMIT=0
OUT_FILE="$SCRIPT_DIR/trigger_results.json"

while [ $# -gt 0 ]; do
  case "$1" in
    --cluster) CLUSTER_FILTER="$2"; shift 2 ;;
    --runs)    RUNS_PER_QUERY="$2"; shift 2 ;;
    --limit)   LIMIT="$2"; shift 2 ;;
    --out)     OUT_FILE="$2"; shift 2 ;;
    -h|--help)
      sed -n '2,20p' "$0"
      exit 0
      ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
done

if ! command -v claude >/dev/null 2>&1; then
  echo "Error: claude CLI not found on PATH" >&2
  exit 1
fi
if [ ! -f "$QUERIES_FILE" ]; then
  echo "Error: $QUERIES_FILE not found" >&2
  exit 1
fi

# Flatten queries.json to tab-separated lines: index<TAB>cluster<TAB>expected<TAB>query
# (expected is "-" for should-not-trigger queries). bash 3.2: no mapfile.
TSV_FILE="$(mktemp)"
RUNS_FILE="$(mktemp)"
trap 'rm -f "$TSV_FILE" "$RUNS_FILE"' EXIT

python3 - "$QUERIES_FILE" "$CLUSTER_FILTER" <<'PYEOF' > "$TSV_FILE"
import json, sys
data = json.load(open(sys.argv[1]))
cluster_filter = sys.argv[2]
for i, item in enumerate(data["queries"]):
    if cluster_filter and item["cluster"] != cluster_filter:
        continue
    expected = item["expected_skill"] or "-"
    query = item["query"].replace("\t", " ").replace("\n", " ")
    print(f"{i}\t{item['cluster']}\t{expected}\t{query}")
PYEOF

total_queries=$(wc -l < "$TSV_FILE" | tr -d ' ')
if [ "$LIMIT" -gt 0 ] && [ "$LIMIT" -lt "$total_queries" ]; then
  head -n "$LIMIT" "$TSV_FILE" > "$TSV_FILE.lim" && mv "$TSV_FILE.lim" "$TSV_FILE"
  total_queries="$LIMIT"
fi

total_invocations=$((total_queries * RUNS_PER_QUERY))
echo "About to make $total_invocations claude invocations" >&2
echo "($total_queries queries x $RUNS_PER_QUERY runs). Ctrl-C now to abort; starting in 5s..." >&2
sleep 5

# Extract skills invoked via the Skill tool from claude's JSON output.
# Reads the raw output on stdin, prints one skill name per line.
extract_skills() {
  python3 - <<'PYEOF'
import json, re, sys
raw = sys.stdin.read()
names = set()
# Try structured parse first (single JSON object or JSON-lines).
def walk(node):
    if isinstance(node, dict):
        if node.get("name") == "Skill":
            skill = (node.get("input") or {}).get("skill") or (node.get("input") or {}).get("command")
            if skill:
                names.add(str(skill).split(":")[-1])
        for v in node.values():
            walk(v)
    elif isinstance(node, list):
        for v in node:
            walk(v)
for chunk in raw.splitlines():
    chunk = chunk.strip()
    if not chunk:
        continue
    try:
        walk(json.loads(chunk))
    except ValueError:
        pass
try:
    walk(json.loads(raw))
except ValueError:
    pass
# Fallback: regex over the raw text for Skill tool invocations.
for m in re.finditer(r'"name"\s*:\s*"Skill".{0,400}?"(?:skill|command)"\s*:\s*"([^"]+)"', raw, re.S):
    names.add(m.group(1).split(":")[-1])
for n in sorted(names):
    print(n)
PYEOF
}

query_num=0
while IFS="$(printf '\t')" read -r idx cluster expected query; do
  query_num=$((query_num + 1))
  echo "[$query_num/$total_queries] ($cluster) $query" >&2

  run=0
  while [ "$run" -lt "$RUNS_PER_QUERY" ]; do
    run=$((run + 1))
    # pipefail-safe: never let a failed claude call abort the harness.
    output="$(claude -p "$query" --output-format json 2>/dev/null || true)"
    skills="$(printf '%s' "$output" | extract_skills || true)"
    # Record one line per run: idx|cluster|expected|comma-joined-skills
    joined="$(printf '%s' "$skills" | tr '\n' ',' | sed 's/,$//')"
    printf '%s\t%s\t%s\t%s\n' "$idx" "$cluster" "$expected" "$joined" >> "$RUNS_FILE"
    echo "    run $run -> invoked: ${joined:-<none>}" >&2
  done
done < "$TSV_FILE"

# Aggregate results into JSON.
python3 - "$QUERIES_FILE" "$RUNS_FILE" "$RUNS_PER_QUERY" "$OUT_FILE" <<'PYEOF'
import json, sys
from collections import defaultdict

queries = json.load(open(sys.argv[1]))["queries"]
runs_per_query = int(sys.argv[3])

# Skills belonging to each cluster (from the labeled queries).
cluster_skills = defaultdict(set)
for item in queries:
    if item["expected_skill"]:
        cluster_skills[item["cluster"]].add(item["expected_skill"])

runs = defaultdict(list)
for line in open(sys.argv[2]):
    idx, cluster, expected, joined = (line.rstrip("\n").split("\t") + [""])[:4]
    runs[int(idx)].append([s for s in joined.split(",") if s])

results = []
for idx, run_list in sorted(runs.items()):
    item = queries[idx]
    expected = item["expected_skill"]
    cskills = cluster_skills[item["cluster"]]
    n = len(run_list)
    if expected:
        hits = sum(1 for skills in run_list if expected in skills)
        rate = hits / n if n else 0.0
        passed = rate > 0.5
    else:
        hits = sum(1 for skills in run_list if any(s in cskills for s in skills))
        rate = hits / n if n else 0.0
        passed = rate < 0.5
    results.append({
        "query": item["query"],
        "cluster": item["cluster"],
        "expected_skill": expected,
        "runs": n,
        "invoked_per_run": run_list,
        "trigger_rate": round(rate, 3),
        "passed": passed,
    })

by_cluster = defaultdict(lambda: {"passed": 0, "total": 0})
for r in results:
    by_cluster[r["cluster"]]["total"] += 1
    by_cluster[r["cluster"]]["passed"] += int(r["passed"])

summary = {
    "runs_per_query": runs_per_query,
    "queries_tested": len(results),
    "queries_passed": sum(int(r["passed"]) for r in results),
    "by_cluster": {
        k: {**v, "pass_rate": round(v["passed"] / v["total"], 3)}
        for k, v in sorted(by_cluster.items())
    },
}
json.dump({"summary": summary, "results": results}, open(sys.argv[4], "w"), indent=2)
print(json.dumps(summary, indent=2))
print(f"\nFull results written to {sys.argv[4]}")
PYEOF
