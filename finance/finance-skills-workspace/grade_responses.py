#!/usr/bin/env python3
"""Grade eval responses against assertions from eval_metadata.json files.

Deterministic keyword grader for the with-skill / without-skill eval runs.

Design notes (rewritten after the 2026-06 eval-infrastructure audit):
- All keyword matching is word-boundary aware ("dol" no longer matches inside
  "methodology"). A trailing "*" on a keyword allows suffixes ("prorat*").
- Assertion meta-verbs ("Mentions", "Discusses", ...) are stripped before any
  concept extraction, so "Mentions Sortino ratio" requires Sortino, not the
  word "mention".
- There are NO default-pass paths. Any assertion the grader cannot evaluate
  mechanically gets an explicit "manual_review" status which does not count
  as a pass and is surfaced in both the CLI output and grading.json.
- Conceptual-focus assertions parse the focus direction from the assertion
  text itself ("Focuses on X, not Y" => X terms must outnumber Y terms).
- Every assertion must have ALL of its concept groups evidenced (no 60%
  benefit of the doubt), and evidence quotes the matched response snippet
  with surrounding context.
- Numeric assertions require magnitude-consistent matches: "$64K" only
  matches dollar amounts that normalize into the target band, never a bare
  "60" from "60/40".
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

PASS = "pass"
FAIL = "fail"
MANUAL_REVIEW = "manual_review"

SNIPPET_CONTEXT_CHARS = 60

# Leading verbs that describe the assertion, not the required concept.
META_VERBS = (
    "mentions", "discusses", "references", "addresses", "provides",
    "cites", "identifies", "recommends", "warns about", "warns",
    "calculates", "defines", "designs", "outlines", "analyzes",
    "applies", "shows", "states", "describes", "proposes", "includes",
    "flags", "notes", "covers", "explains",
)

_META_VERB_ALT = "|".join(re.escape(v) for v in META_VERBS)
_META_VERB_RE = re.compile(
    rf"^(?:(?:{_META_VERB_ALT})(?:\s+or\s+(?:{_META_VERB_ALT}))*\s+)+",
    re.IGNORECASE,
)

STOPWORDS = {
    "about", "should", "their", "which", "these", "those", "could", "would",
    "with", "that", "this", "from", "into", "does", "both", "each", "when",
    "what", "have", "must", "the", "and", "for", "not", "are", "its",
    "specific", "distinct disclose", "using", "given", "over", "part",
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def strip_meta_verbs(text: str) -> str:
    return _META_VERB_RE.sub("", text.strip())


def keyword_pattern(keyword: str) -> re.Pattern[str]:
    """Compile a keyword to a word-boundary-aware, hyphen/space-tolerant regex."""
    wildcard = keyword.endswith("*")
    if wildcard:
        keyword = keyword[:-1]
    parts = [p for p in re.split(r"[\s\-]+", keyword) if p]
    body = r"[\s\-]+".join(re.escape(p) for p in parts)
    if wildcard:
        body += r"\w*"
    return re.compile(rf"(?<![A-Za-z0-9$]){body}(?![A-Za-z0-9])", re.IGNORECASE)


def snippet(text: str, start: int, end: int, context: int = SNIPPET_CONTEXT_CHARS) -> str:
    lo = max(0, start - context)
    hi = min(len(text), end + context)
    prefix = "..." if lo > 0 else ""
    suffix = "..." if hi < len(text) else ""
    excerpt = re.sub(r"\s+", " ", text[lo:hi]).strip()
    return f'{prefix}{excerpt}{suffix}'


def find_keyword(response: str, keyword: str) -> tuple[str, str] | None:
    """Return (matched_keyword, quoted_snippet) for the first match, else None."""
    match = keyword_pattern(keyword).search(response)
    if match is None:
        return None
    return keyword, snippet(response, match.start(), match.end())


def find_group(response: str, group: list[str]) -> tuple[str, str] | None:
    for keyword in group:
        hit = find_keyword(response, keyword)
        if hit is not None:
            return hit
    return None


def count_terms(response: str, terms: list[str]) -> tuple[int, list[str]]:
    """Total occurrence count across terms, plus which terms were found."""
    total = 0
    found: list[str] = []
    for term in terms:
        n = len(keyword_pattern(term).findall(response))
        if n:
            total += n
            found.append(f"{term} x{n}")
    return total, found


@dataclass(frozen=True)
class AssertionResult:
    text: str
    status: str  # pass | fail | manual_review
    evidence: str

    @property
    def passed(self) -> bool:
        return self.status == PASS


# ---------------------------------------------------------------------------
# contains_concept
# ---------------------------------------------------------------------------

# Curated concept groups keyed by normalized assertion text. Within a group,
# any keyword satisfies the group (OR). ALL groups must be evidenced (AND).
CONCEPT_RULES: dict[str, list[list[str]]] = {
    "mentions reg bi by name": [
        ["reg bi", "regulation best interest"],
    ],
    "cites the four reg bi obligations": [
        ["reg bi", "regulation best interest"],
        ["disclosure"],
        ["care"],
        ["conflict*"],
        ["compliance"],
    ],
    "mentions pte 2020-02 or dol prohibited transaction exemption": [
        ["pte 2020-02", "pte 2020", "prohibited transaction exemption"],
    ],
    "discusses reasonably available alternatives analysis": [
        ["alternative*"],
        ["reasonably available", "stay* in", "staying in", "remain* in",
         "leave the", "left in", "new employer", "current plan",
         "existing plan", "in-plan", "current 401"],
    ],
    "applies ia act section 206 fiduciary framework": [
        ["section 206", "sections 206", "206(1)", "206(2)", "advisers act", "ia act"],
        ["fiduciary"],
    ],
    "analyzes both duty of care and duty of loyalty": [
        ["duty of care"],
        ["duty of loyalty"],
    ],
    "identifies proprietary fund as conflict of interest": [
        ["proprietary"],
        ["conflict*"],
    ],
    "discusses cost differential materiality": [
        ["cost*", "fee*", "expense*"],
        ["differential*", "difference*", "cheaper", "more expensive",
         "lower-cost", "higher-cost", "costlier", "basis points", "bps"],
    ],
    "references form adv part 2a item 5": [
        ["form adv", "part 2a"],
        ["item 5"],
    ],
    "addresses 12b-1 fee disclosure as indirect compensation or conflict": [
        ["12b-1"],
        ["indirect compensation", "conflict*"],
    ],
    "discusses how to present tiered fee schedules in disclosure documents": [
        ["tier*", "breakpoint*", "graduated"],
        ["fee schedule*", "schedule*"],
        ["disclos*"],
    ],
    "provides proration formula or methodology for partial-quarter accounts": [
        ["prorat*"],
        ["formula*", "methodolog*", "calculat*", "days"],
    ],
    "addresses mid-quarter termination refund calculation": [
        ["refund*"],
        ["terminat*"],
    ],
    "discusses billing system mechanics (custodian deduction, valuation dates)": [
        ["custodi*"],
        ["deduct*", "debit*"],
        ["valuation date*", "valuation", "last business day", "billing date*",
         "quarter-end value*", "as-of date*"],
    ],
    "addresses cip/kyc for each trustee individually": [
        ["cip", "customer identification", "kyc", "know your customer"],
        ["trustee*"],
    ],
    "mentions beneficial ownership certification requirement": [
        ["beneficial owner*"],
        ["certif*"],
    ],
    "flags the non-us trustee as requiring enhanced due diligence": [
        ["enhanced due diligence", "edd", "enhanced review", "enhanced screening",
         "enhanced compliance", "heightened scrutiny", "heightened review",
         "elevated risk", "additional screening", "additional due diligence"],
        ["non-us", "non-u.s.", "uk", "foreign", "non-resident"],
    ],
    "references ofac or sanctions screening": [
        ["ofac", "sanction*"],
    ],
    "addresses nigo root cause analysis and specific rejection patterns": [
        ["nigo", "not in good order"],
        ["root cause*", "rejection*", "reject*"],
    ],
    "proposes workflow validation gates or pre-submission checks": [
        ["validat*", "pre-submission", "pre-submit", "quality control", "qc",
         "pre-check*", "pre-flight"],
    ],
    "mentions specific custodian integration or submission mechanics": [
        ["schwab", "fidelity", "pershing", "custodian*"],
        ["api*", "esign*", "e-sign*", "docusign", "digital onboarding",
         "electronic submission", "submission", "submit*", "integrat*"],
    ],
    "calculates or discusses sharpe ratio using provided return and volatility data": [
        ["sharpe"],
        ["risk-free", "risk free"],
    ],
    "analyzes the -32% max drawdown in context (severity, recovery)": [
        ["drawdown*"],
        ["recover*"],
        ["32"],
    ],
    "mentions sortino ratio or downside risk metrics": [
        ["sortino", "downside"],
    ],
    "discusses monte carlo simulation or stochastic modeling": [
        ["monte carlo", "stochastic"],
    ],
    "mentions capital market assumptions or expected return estimation": [
        ["capital market assumption*", "cma*", "expected return*"],
    ],
    "addresses probability of meeting the return target over the time horizon": [
        ["probability", "likelihood", "chance"],
        ["target*"],
    ],
    "defines or calculates stp rate and sets improvement targets": [
        ["stp", "straight-through", "straight through"],
        ["90%", "target*", "goal*"],
    ],
    "identifies exception categories and auto-resolution patterns": [
        ["exception*"],
        ["categor*", "classif*", "taxonomy", "tier*", "bucket*", "type*"],
        ["auto-resol*", "auto resol*", "automatic resolution",
         "automatically resolv*", "auto-clear*", "self-heal*", "auto-correct*",
         "auto-fix*", "auto-match*", "auto-remediat*"],
    ],
    "discusses api vs rpa integration approaches for legacy systems": [
        ["api*"],
        ["rpa", "robotic process automation", "screen-scrap*", "screen scrap*"],
    ],
    "designs multi-level approval chain with different thresholds by request type": [
        ["approval*"],
        ["level*", "chain*", "tier*", "multi-level"],
    ],
    "addresses sla targets and escalation rules for aging items": [
        ["sla*", "service level*"],
        ["escalat*"],
    ],
    "discusses task routing or state machine modeling": [
        ["state machine*", "routing", "route*", "workflow engine",
         "task queue*", "queue*"],
    ],
    "mwr/irr is lower than twr": [
        ["mwr", "money-weighted", "money weighted", "irr"],
        ["twr", "time-weighted", "time weighted"],
        ["lower", "less than", "below", "smaller", "lags", "trails", "drags"],
    ],
    "shows sub-period return calculations step by step": [
        ["sub-period*", "subperiod*", "sub period*", "first six months",
         "first 6 months", "period 1", "first half", "first period"],
        ["15%"],
    ],
    "identifies twr as manager skill, mwr as investor experience": [
        ["manager*"],
        ["investor*", "client*"],
    ],
    "identifies that the 5% band has been breached (68% > 65%)": [
        ["band*", "threshold*", "toleranc*", "corridor*"],
        ["breach*", "exceed*", "outside", "violat*", "trigger*", "drift*"],
        ["65%", "8%"],  # quantifies the breach: 65% upper limit or 8% drift
    ],
    "recommends harvesting the $15k loss as part of the rebalance": [
        ["harvest*"],
        ["$15k", "$15,000", "15k"],
    ],
    "warns about wash-sale rules": [
        ["wash sale*"],
    ],
    "mentions replacement security selection": [
        ["replacement*", "substitute*", "proxy", "similar etf*",
         "similar fund*", "swap*", "stand-in"],
    ],
}


def fallback_concept_groups(assertion_text: str) -> list[list[str]]:
    """Derive concept groups from assertion content words (no curated rule)."""
    stripped = strip_meta_verbs(assertion_text)
    stripped = re.sub(r"[(),]", " ", stripped.lower())
    words = [
        w for w in re.findall(r"[a-z][a-z0-9\-]{3,}", stripped)
        if w not in STOPWORDS
    ]
    return [[f"{w}*"] for w in words[:4]]


def grade_contains_concept(response: str, assertion_text: str) -> AssertionResult:
    key = normalize(assertion_text)
    groups = CONCEPT_RULES.get(key)
    derived = False
    if groups is None:
        groups = fallback_concept_groups(assertion_text)
        derived = True
        if not groups:
            return AssertionResult(
                assertion_text, MANUAL_REVIEW,
                "No curated concept mapping and no content words could be "
                "derived from the assertion text.",
            )

    found: list[str] = []
    missing: list[str] = []
    for group in groups:
        hit = find_group(response, group)
        if hit is None:
            missing.append("/".join(group))
        else:
            keyword, quote = hit
            found.append(f"'{keyword}' -> \"{quote}\"")

    prefix = "(derived keywords) " if derived else ""
    if not missing:
        return AssertionResult(
            assertion_text, PASS,
            prefix + "All concept groups evidenced: " + " | ".join(found),
        )
    evidence = prefix + f"Missing concept group(s): {'; '.join(missing)}."
    if found:
        evidence += " Found: " + " | ".join(found)
    return AssertionResult(assertion_text, FAIL, evidence)


# ---------------------------------------------------------------------------
# absence
# ---------------------------------------------------------------------------

def grade_absence(response: str, assertion_text: str) -> AssertionResult:
    norm = normalize(assertion_text)

    if "capacity" in norm and "fiduciary" in norm:
        # e.g. "Does not incorrectly apply pure fiduciary standard without
        # acknowledging BD capacity" — require an explicit BD-capacity anchor.
        hit = find_group(response, [
            "reg bi", "regulation best interest", "broker-dealer",
            "broker dealer", "bd capacity", "dual-registrant", "dual registrant",
        ])
        if hit is not None:
            keyword, quote = hit
            return AssertionResult(
                assertion_text, PASS,
                f"BD capacity acknowledged via '{keyword}' -> \"{quote}\"",
            )
        return AssertionResult(
            assertion_text, FAIL,
            "No acknowledgment of broker-dealer capacity or Reg BI found; "
            "response appears to apply a pure fiduciary framing.",
        )

    if "suitability" in norm:
        # e.g. "Does not apply FINRA suitability as primary standard" —
        # suitability framing must not dominate the fiduciary/best-interest
        # framing.
        suit_count, suit_found = count_terms(response, ["suitability", "rule 2111"])
        fid_count, fid_found = count_terms(response, [
            "fiduciary", "best interest", "duty of loyalty", "duty of care",
            "section 206", "advisers act",
        ])
        detail = (
            f"suitability terms: {suit_count} ({', '.join(suit_found) or 'none'}) "
            f"vs fiduciary/best-interest terms: {fid_count} "
            f"({', '.join(fid_found) or 'none'})"
        )
        if suit_count > fid_count:
            return AssertionResult(
                assertion_text, FAIL,
                f"Suitability framing dominates — {detail}",
            )
        return AssertionResult(
            assertion_text, PASS,
            f"Fiduciary/best-interest framing dominant or equal — {detail}",
        )

    return AssertionResult(
        assertion_text, MANUAL_REVIEW,
        "No mechanical rule for this absence assertion; requires manual review.",
    )


# ---------------------------------------------------------------------------
# numerical_accuracy
# ---------------------------------------------------------------------------

_DOLLAR_RE = re.compile(
    r"\$\s?(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)\s*(k|thousand|mm|m|million)?(?![\w%])",
    re.IGNORECASE,
)
_BARE_K_RE = re.compile(r"(?<![\w$.,])(\d+(?:\.\d+)?)\s?k(?![\w])", re.IGNORECASE)
_PERCENT_RE = re.compile(r"(-?\d+(?:\.\d+)?)\s*(?:%|percent)")

_SUFFIX_MULTIPLIER = {
    None: 1.0, "": 1.0,
    "k": 1_000.0, "thousand": 1_000.0,
    "m": 1_000_000.0, "mm": 1_000_000.0, "million": 1_000_000.0,
}


def _dollar_candidates(response: str) -> list[tuple[float, int, int]]:
    """Magnitude-normalized dollar amounts in the response.

    Only $-prefixed amounts or K-suffixed amounts qualify, so a bare "60"
    (e.g. from "60/40") can never satisfy a dollar-magnitude assertion.
    """
    candidates: list[tuple[float, int, int]] = []
    for match in _DOLLAR_RE.finditer(response):
        raw, suffix = match.group(1), (match.group(2) or "").lower()
        value = float(raw.replace(",", "")) * _SUFFIX_MULTIPLIER[suffix]
        candidates.append((value, match.start(), match.end()))
    for match in _BARE_K_RE.finditer(response):
        value = float(match.group(1)) * 1_000.0
        candidates.append((value, match.start(), match.end()))
    return candidates


def grade_numerical(response: str, assertion_text: str) -> AssertionResult:
    # Explicit range, e.g. "(range 23.5-24.5%)"
    range_match = re.search(
        r"range\s+(\d+(?:\.\d+)?)\s*[-–]\s*(\d+(?:\.\d+)?)\s*%", assertion_text
    )
    approx_pct = re.search(
        r"(?:approximately|about|~)\s*(\d+(?:\.\d+)?)\s*%", assertion_text
    )
    if range_match or approx_pct:
        if range_match:
            lo, hi = float(range_match.group(1)), float(range_match.group(2))
        else:
            center = float(approx_pct.group(1))  # type: ignore[union-attr]
            lo, hi = center - 0.5, center + 0.5
        seen: list[float] = []
        for match in _PERCENT_RE.finditer(response):
            value = float(match.group(1))
            seen.append(value)
            if lo <= value <= hi:
                return AssertionResult(
                    assertion_text, PASS,
                    f"Found {value}% within [{lo}%, {hi}%] -> "
                    f"\"{snippet(response, match.start(), match.end())}\"",
                )
        return AssertionResult(
            assertion_text, FAIL,
            f"No percentage within [{lo}%, {hi}%]. "
            f"Percentages found: {sorted(set(seen))[:12]}",
        )

    dollar_match = re.search(
        r"~?\$(\d+(?:\.\d+)?)\s*(k|thousand|mm|m|million)?",
        assertion_text, re.IGNORECASE,
    )
    if dollar_match:
        suffix = (dollar_match.group(2) or "").lower()
        target = float(dollar_match.group(1)) * _SUFFIX_MULTIPLIER[suffix]
        lo, hi = target * 0.85, target * 1.15
        candidates = _dollar_candidates(response)
        for value, start, end in candidates:
            if lo <= value <= hi:
                return AssertionResult(
                    assertion_text, PASS,
                    f"Found ${value:,.0f} within [${lo:,.0f}, ${hi:,.0f}] -> "
                    f"\"{snippet(response, start, end)}\"",
                )
        found = sorted({v for v, _, _ in candidates})
        return AssertionResult(
            assertion_text, FAIL,
            f"No magnitude-consistent dollar amount within "
            f"[${lo:,.0f}, ${hi:,.0f}]. Dollar amounts found: "
            f"{[f'${v:,.0f}' for v in found[:12]]}",
        )

    return AssertionResult(
        assertion_text, MANUAL_REVIEW,
        "Could not parse a numeric target (percent range or dollar amount) "
        "from the assertion text; requires manual review.",
    )


# ---------------------------------------------------------------------------
# depth_check
# ---------------------------------------------------------------------------

_CITATION_PATTERNS = [
    r"\brule\s+\d+[a-z]?(?:[-.]\d+)*(?:\([a-z0-9]+\))*",
    r"\bsection\s+\d+[a-z]?(?:\([a-z0-9]+\))*",
    r"\b\d+\s+c\.?f\.?r\.?\s*(?:§+\s*)?[\d.]+",
    r"\b\d+\s+u\.?s\.?c\.?\s*(?:§+\s*)?[\d.]+",
    r"\bpte\s+\d{4}-\d{2}",
    r"\bform\s+(?:adv|crs|u4|u5|bd|13f|pf)\b",
    r"\breg(?:ulation)?\s+(?:bi|s-p|s-id|sho|nms|d\b|t\b)",
    r"\bfinra\s+rule\s+\d+",
    r"\bsec\s+rule\s+\d+[a-z]?(?:[-.]\d+)*",
    r"\b31\s+cfr\s+[\d.]+",
    r"\bsection\s+32[0-6]\b",
    r"\b§+\s*[\d.]+",
    r"\bitem\s+\d+[a-z]?\b",
    r"\b12b-1\b",
    r"\b(?:investment\s+)?advisers\s+act\b",
    r"\binvestment\s+company\s+act\b",
    r"\bsecurities\s+exchange\s+act\b",
    r"\b(?:usa\s+)?patriot\s+act\b",
    r"\bbank\s+secrecy\s+act\b",
    r"\berisa\b",
    r"\bfatca\b",
    r"\bfincen\s+(?:rule\s+)?[\d(]+[a-z0-9()]*",
]

_RISK_METRIC_TERMS = [
    "sharpe", "sortino", "max drawdown", "maximum drawdown", "calmar",
    "information ratio", "tracking error", "treynor", "beta", "alpha",
    "standard deviation", "downside deviation", "value at risk", "cvar",
    "expected shortfall", "ulcer index", "capture ratio", "omega ratio",
    "m-squared", "r-squared",
]

_EDGE_CASE_MARKERS = [
    "edge case*", "pitfall*", "caveat*", "gotcha*", "watch out", "be careful",
    "common mistake*", "common error*", "trap*", "special case*",
    "exception*", "however", "failure to", "failing to", "often overlooked",
    "frequently missed", "don't forget", "easy to miss", "subtle*",
    "complication*", "corner case*",
]


_EDGE_SECTION_HEAD_RE = re.compile(
    r"(?im)^(#{2,6})[^\n]*\b(edge\s+case|pitfall|gotcha|caveat|mistake|"
    r"watch|complication|trap|key\s+risks?|risk\s+factors)",
)


def _count_edge_case_section_items(response: str) -> int:
    """Count enumerated items inside sections titled edge cases / pitfalls.

    Responses typically structure edge cases as subsections or bold lead-ins
    under a heading like '## Edge Cases to Handle' rather than repeating
    marker words, so marker counting alone undercounts.
    """
    total = 0
    for head in _EDGE_SECTION_HEAD_RE.finditer(response):
        level = len(head.group(1))
        block_start = head.end()
        next_head = re.search(
            rf"(?m)^#{{1,{level}}}\s", response[block_start:]
        )
        block = response[block_start:block_start + next_head.start()] \
            if next_head else response[block_start:]
        subheadings = len(re.findall(rf"(?m)^#{{{level + 1},6}}\s", block))
        bold_leads = len(re.findall(r"(?m)^\*\*[^*\n]+", block))
        bullets = len(re.findall(r"(?m)^\s*[-*]\s+\S", block))
        numbered = len(re.findall(r"(?m)^\s*\d{1,2}[.)]\s+\S", block))
        total += max(subheadings, bold_leads, bullets, numbered)
    return total


def _count_steps(response: str) -> tuple[int, list[str]]:
    ordinals: set[int] = set()
    samples: list[str] = []
    for match in re.finditer(r"(?m)^\s{0,6}(?:\*\*)?(\d{1,2})[.)]\s", response):
        ordinals.add(int(match.group(1)))
    for match in re.finditer(r"\b(?:step|phase|stage)\s+(\d{1,2})\b", response, re.IGNORECASE):
        ordinals.add(int(match.group(1)))
        samples.append(snippet(response, match.start(), match.end(), 30))
    return len(ordinals), samples[:3]


def grade_depth_check(response: str, assertion_text: str) -> AssertionResult:
    norm = normalize(assertion_text)
    count_match = re.search(r"(\d+)\s*\+|at least (\d+)", norm)
    if not count_match:
        return AssertionResult(
            assertion_text, MANUAL_REVIEW,
            "Could not parse a minimum count (e.g. '3+') from the assertion "
            "text; requires manual review.",
        )
    min_count = int(count_match.group(1) or count_match.group(2))

    if "rule number" in norm or "citation" in norm or "specific rule" in norm:
        found: set[str] = set()
        for pattern in _CITATION_PATTERNS:
            for match in re.finditer(pattern, response, re.IGNORECASE):
                found.add(re.sub(r"\s+", " ", match.group(0).lower()).strip())
        sample = sorted(found)[:8]
        if len(found) >= min_count:
            return AssertionResult(
                assertion_text, PASS,
                f"{len(found)} distinct citations (need {min_count}+): {sample}",
            )
        return AssertionResult(
            assertion_text, FAIL,
            f"Only {len(found)} distinct citations (need {min_count}+): {sample}",
        )

    if "risk metric" in norm:
        found_metrics = [
            term for term in _RISK_METRIC_TERMS
            if keyword_pattern(term).search(response)
        ]
        if len(found_metrics) >= min_count:
            return AssertionResult(
                assertion_text, PASS,
                f"{len(found_metrics)} distinct risk metrics "
                f"(need {min_count}+): {found_metrics}",
            )
        return AssertionResult(
            assertion_text, FAIL,
            f"Only {len(found_metrics)} distinct risk metrics "
            f"(need {min_count}+): {found_metrics}",
        )

    if "edge case" in norm or "pitfall" in norm:
        found_markers = [
            marker for marker in _EDGE_CASE_MARKERS
            if keyword_pattern(marker).search(response)
        ]
        section_items = _count_edge_case_section_items(response)
        count = max(len(found_markers), section_items)
        detail = (
            f"{len(found_markers)} distinct marker terms "
            f"({found_markers[:6]}), {section_items} enumerated items in "
            f"edge-case/pitfall sections"
        )
        if count >= min_count:
            return AssertionResult(
                assertion_text, PASS,
                f"{count} edge cases/pitfalls evidenced (need {min_count}+): {detail}",
            )
        return AssertionResult(
            assertion_text, FAIL,
            f"Only {count} edge cases/pitfalls evidenced (need {min_count}+): {detail}",
        )

    if "step" in norm or "phase" in norm or "stage" in norm:
        count, samples = _count_steps(response)
        detail = f" e.g. {samples}" if samples else ""
        if count >= min_count:
            return AssertionResult(
                assertion_text, PASS,
                f"{count} distinct enumerated steps/phases (need {min_count}+).{detail}",
            )
        return AssertionResult(
            assertion_text, FAIL,
            f"Only {count} distinct enumerated steps/phases (need {min_count}+).{detail}",
        )

    paragraphs = [p for p in response.split("\n\n") if len(p) > 100]
    if len(paragraphs) >= min_count:
        return AssertionResult(
            assertion_text, PASS,
            f"{len(paragraphs)} substantive paragraphs (need {min_count}+)",
        )
    return AssertionResult(
        assertion_text, FAIL,
        f"Only {len(paragraphs)} substantive paragraphs (need {min_count}+)",
    )


# ---------------------------------------------------------------------------
# conceptual_focus
# ---------------------------------------------------------------------------

# Topic lexicon: 'triggers' identify the topic inside the ASSERTION text;
# 'terms' are counted (word-boundary) inside the RESPONSE.
FOCUS_TOPICS: dict[str, dict[str, list[str]]] = {
    "disclosure": {
        "triggers": ["disclosure"],
        "terms": ["disclos*", "form adv", "brochure*", "item 5", "part 2a",
                  "filing*", "form crs"],
    },
    "billing": {
        "triggers": ["billing"],
        "terms": ["billing", "bill", "prorat*", "invoice*", "refund*",
                  "deduct*", "debit*", "valuation date*", "reconcil*",
                  "accrual*"],
    },
    "historical": {
        "triggers": ["historical", "realized"],
        "terms": ["historical", "realized", "ex-post", "ex post", "trailing",
                  "past performance", "actual return*"],
    },
    "forward": {
        "triggers": ["forward", "projection"],
        "terms": ["forward-looking", "forward", "projection*", "project*",
                  "monte carlo", "simulat*", "expected return*", "forecast*",
                  "scenario*"],
    },
    "automation": {
        "triggers": ["automation", "stp"],
        "terms": ["stp", "straight-through", "straight through", "automat*",
                  "exception*", "auto-resol*", "rpa"],
    },
    "routing_approvals": {
        "triggers": ["routing", "approval", "task routing"],
        "terms": ["approval*", "approver*", "routing", "route*", "escalat*",
                  "sla*", "sign-off*", "state machine*", "queue*", "delegat*"],
    },
    "process_improvement": {
        "triggers": ["process improvement"],
        "terms": ["workflow*", "process*", "validat*", "checklist*", "nigo",
                  "qc", "training", "root cause*", "automat*"],
    },
    "compliance_requirements": {
        "triggers": ["compliance requirement"],
        "terms": ["cip", "kyc", "aml", "ofac", "beneficial owner*",
                  "sanction*", "regulator*", "finra", "suitability"],
    },
}

_FOCUS_SPLIT_RE = re.compile(
    r"^(?:focus(?:es|ed)?\s+(?:is\s+)?on|analysis is grounded in|grounded in)?"
    r"\s*(?P<required>.+?)"
    r"(?:,\s*|\s*\()not(?:\s+just)?\s+(?P<excluded>.+?)\)?\s*$",
    re.IGNORECASE,
)


def _topics_for(side_text: str) -> set[str]:
    side_norm = normalize(side_text)
    return {
        name for name, spec in FOCUS_TOPICS.items()
        if any(trigger in side_norm for trigger in spec["triggers"])
    }


def grade_conceptual_focus(response: str, assertion_text: str) -> AssertionResult:
    norm = normalize(strip_meta_verbs(assertion_text))
    match = _FOCUS_SPLIT_RE.match(norm)
    if not match:
        return AssertionResult(
            assertion_text, MANUAL_REVIEW,
            "Could not parse a 'focuses on X, not Y' direction from the "
            "assertion text; requires manual review.",
        )

    required_topics = _topics_for(match.group("required"))
    excluded_topics = _topics_for(match.group("excluded")) - required_topics
    required_topics -= _topics_for(match.group("excluded"))
    if not required_topics or not excluded_topics:
        return AssertionResult(
            assertion_text, MANUAL_REVIEW,
            f"Could not map focus sides to distinct topic lexicons "
            f"(required='{match.group('required')}', "
            f"excluded='{match.group('excluded')}'); requires manual review.",
        )

    required_terms = sorted({t for n in required_topics for t in FOCUS_TOPICS[n]["terms"]})
    excluded_terms = sorted({t for n in excluded_topics for t in FOCUS_TOPICS[n]["terms"]})
    req_count, req_found = count_terms(response, required_terms)
    exc_count, exc_found = count_terms(response, excluded_terms)

    detail = (
        f"required topic(s) {sorted(required_topics)}: {req_count} hits "
        f"({', '.join(req_found[:6]) or 'none'}) vs excluded topic(s) "
        f"{sorted(excluded_topics)}: {exc_count} hits "
        f"({', '.join(exc_found[:6]) or 'none'})"
    )
    if req_count == 0 and exc_count == 0:
        return AssertionResult(
            assertion_text, MANUAL_REVIEW,
            f"No focus-topic terms found on either side; the lexicon cannot "
            f"determine focus direction mechanically — {detail}",
        )
    if req_count > exc_count:
        return AssertionResult(assertion_text, PASS, f"Focus direction correct — {detail}")
    return AssertionResult(assertion_text, FAIL, f"Focus direction wrong or unclear — {detail}")


# ---------------------------------------------------------------------------
# dispatch / runner
# ---------------------------------------------------------------------------

GRADERS = {
    "absence": grade_absence,
    "numerical_accuracy": grade_numerical,
    "conceptual_focus": grade_conceptual_focus,
    "depth_check": grade_depth_check,
    "contains_concept": grade_contains_concept,
}


def grade_response(response_text: str, assertions: list[dict]) -> list[AssertionResult]:
    results: list[AssertionResult] = []
    for assertion in assertions:
        text = assertion["text"]
        grader = GRADERS.get(assertion.get("type", "contains_concept"),
                             grade_contains_concept)
        results.append(grader(response_text, text))
    return results


def grading_payload(metadata: dict, variant: str,
                    results: list[AssertionResult]) -> dict:
    passed = sum(1 for r in results if r.status == PASS)
    failed = sum(1 for r in results if r.status == FAIL)
    manual = sum(1 for r in results if r.status == MANUAL_REVIEW)
    total = len(results)
    return {
        "eval_id": metadata["eval_id"],
        "eval_name": metadata["eval_name"],
        "variant": variant,
        "assertion_results": [
            {
                "text": r.text,
                "status": r.status,
                "passed": r.passed,
                "evidence": r.evidence,
            }
            for r in results
        ],
        "summary": {
            "passed": passed,
            "failed": failed,
            "manual_review": manual,
            "total": total,
            "pass_rate": passed / total if total else 0.0,
        },
    }


def iter_eval_dirs(workspace: Path, eval_filter: str | None) -> list[Path]:
    eval_dirs = sorted(
        d for d in workspace.iterdir()
        if d.is_dir() and d.name.startswith("eval-")
        and (d / "eval_metadata.json").exists()
    )
    if eval_filter is None:
        return eval_dirs
    return [
        d for d in eval_dirs
        if eval_filter in d.name
        or d.name.startswith(f"eval-{eval_filter}-")
        or d.name == f"eval-{eval_filter}"
    ]


def grade_workspace(workspace: Path, eval_filter: str | None,
                    dry_run: bool) -> tuple[int, int, int]:
    totals = {PASS: 0, FAIL: 0, MANUAL_REVIEW: 0}
    manual_items: list[str] = []

    for eval_dir in iter_eval_dirs(workspace, eval_filter):
        metadata = json.loads((eval_dir / "eval_metadata.json").read_text())
        assertions = metadata.get("assertions", [])

        print(f"\n{'=' * 70}")
        print(f"EVAL: {metadata['eval_name']}  ({eval_dir})")
        print("=" * 70)

        for variant in ("with_skill", "without_skill"):
            response_file = eval_dir / variant / "outputs" / "response.md"
            if not response_file.exists():
                print(f"\n  [{variant}] — NO RESPONSE FILE")
                continue

            results = grade_response(response_file.read_text(), assertions)
            payload = grading_payload(metadata, variant, results)
            summary = payload["summary"]
            totals[PASS] += summary["passed"]
            totals[FAIL] += summary["failed"]
            totals[MANUAL_REVIEW] += summary["manual_review"]

            print(f"\n  [{variant}] — {summary['passed']}/{summary['total']} passed, "
                  f"{summary['failed']} failed, "
                  f"{summary['manual_review']} need manual review")
            for result in results:
                label = {PASS: "PASS", FAIL: "FAIL", MANUAL_REVIEW: "MANUAL"}[result.status]
                print(f"    [{label:6}] {result.text}")
                print(f"             {result.evidence}")
                if result.status == MANUAL_REVIEW:
                    manual_items.append(
                        f"{workspace.name}/{eval_dir.name}/{variant}: {result.text}"
                    )

            if not dry_run:
                grading_file = eval_dir / variant / "grading.json"
                grading_file.write_text(json.dumps(payload, indent=2) + "\n")

    print(f"\n{'=' * 70}")
    print(f"WORKSPACE {workspace}: {totals[PASS]} passed, {totals[FAIL]} failed, "
          f"{totals[MANUAL_REVIEW]} manual-review")
    if manual_items:
        print("\nASSERTIONS REQUIRING MANUAL REVIEW (not counted as passes):")
        for item in manual_items:
            print(f"  - {item}")
    if dry_run:
        print("\n(dry run — no grading.json files written)")
    else:
        print("\nGrading written to grading.json in each run directory.")
    return totals[PASS], totals[FAIL], totals[MANUAL_REVIEW]


def resolve_workspaces(args: argparse.Namespace) -> list[Path]:
    root = Path(__file__).resolve().parent
    if args.workspace is not None:
        return [Path(args.workspace)]
    if args.iteration is not None:
        return [root / f"iteration-{args.iteration}"]
    return sorted(d for d in root.glob("iteration-*") if d.is_dir())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Grade eval response.md files against eval_metadata.json assertions."
    )
    parser.add_argument(
        "workspace", nargs="?", default=None,
        help="Iteration directory to grade (legacy positional form). "
             "Defaults to every iteration-* directory next to this script.",
    )
    parser.add_argument(
        "--iteration", type=int, choices=(1, 2), default=None,
        help="Grade only iteration-N (ignored if a positional workspace is given).",
    )
    parser.add_argument(
        "--eval", dest="eval_filter", default=None,
        help="Only grade eval directories matching this id or name substring "
             "(e.g. '3' or 'fee-disclosure').",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print grading results without writing grading.json files.",
    )
    args = parser.parse_args()

    workspaces = resolve_workspaces(args)
    if not workspaces:
        print("No iteration directories found.", file=sys.stderr)
        return 1

    for workspace in workspaces:
        if not workspace.is_dir():
            print(f"Workspace not found: {workspace}", file=sys.stderr)
            return 1
        grade_workspace(workspace, args.eval_filter, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
