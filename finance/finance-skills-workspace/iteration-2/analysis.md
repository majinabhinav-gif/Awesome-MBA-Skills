# Iteration 2 Analysis

Date: 2026-06-11
Grader: `grade_responses.py` (rewritten 2026-06 — word-boundary matching, no
default-pass paths, all concept groups required, quoted evidence). Both
iterations below are graded with the SAME grader, so the deltas are
apples-to-apples. All numbers are reproducible by running
`python3 grade_responses.py` and summing the `grading.json` summaries.

## Headline

| Variant | Iteration 1 | Iteration 2 | Change |
|---|---|---|---|
| with_skill | 62/63 (98.4%) | 61/63 (96.8%) | -1 assertion |
| without_skill | 57/63 (90.5%) | 56/63 (88.9%) | -1 assertion |
| with-skill delta | +7.9 pp | +7.9 pp | unchanged |

Note: iteration-2 has no `timing.json` files, so token and duration figures
are unavailable for this iteration (see `benchmark.json`).

## Per-Eval Comparison (assertions passed / total)

| Eval | Name | it1 with | it2 with | it1 without | it2 without |
|---|---|---|---|---|---|
| 1 | regbi-rollover-recommendation | 5/5 | 5/5 | 5/5 | **4/5** (down) |
| 2 | fiduciary-proprietary-fund-conflict | 5/5 | 5/5 | 5/5 | 5/5 |
| 3 | fee-disclosure-form-adv | 6/6 | **5/6** (down) | 5/6 | 5/6 |
| 4 | fee-billing-quarterly-process | 6/6 | 6/6 | 6/6 | 6/6 |
| 5 | account-opening-compliance-trust | 6/6 | 6/6 | 5/6 | 5/6 |
| 6 | account-opening-workflow-nigo | 5/6 | 5/6 | 4/6 | **5/6** (up) |
| 7 | historical-risk-fund-assessment | 5/5 | 5/5 | 5/5 | **4/5** (down, 1 manual review) |
| 8 | forward-risk-portfolio-simulation | 4/4 | 4/4 | 4/4 | 4/4 |
| 9 | stp-automation-acat-transfers | 6/6 | 6/6 | 5/6 | **4/6** (down) |
| 10 | workflow-automation-approval-chains | 5/5 | 5/5 | 4/5 | **5/5** (up) |
| 11 | core-twr-mwr-calculation | 4/4 | 4/4 | 4/4 | 4/4 |
| 13 | wm-rebalance-with-tlh-coordination | 5/5 | 5/5 | 5/5 | 5/5 |
| **Total** | | **62/63** | **61/63** | **57/63** | **56/63** |

## Where With-Skill Regressed or Improved

- **Eval 3 (fee disclosure), with-skill regression (6/6 -> 5/6).** The
  iteration-2 with-skill response restructured its ending into a short
  "Additional Considerations" list and dropped the explicit
  "Key Compliance Risks" enumeration the iteration-1 response had, so it no
  longer evidences 3+ distinct edge cases/pitfalls. This is response
  variance, not a skill change.
- No with-skill improvements were possible on the scoreboard: with-skill was
  already at ceiling (within one assertion of perfect) in iteration 1.
- Persistent with-skill miss in both iterations: eval 6's "4+ distinct edge
  cases or pitfalls in account opening" — both with-skill responses are
  organized as phased redesigns and never enumerate pitfalls explicitly.

## Without-Skill Movement (run-to-run variance of the baseline)

- Improved: eval 6 (4/6 -> 5/6, added e-signature/custodian submission
  mechanics), eval 10 (4/5 -> 5/5, enumerated 5+ workflow steps).
- Regressed: eval 1 (dropped PTE 2020-02 / DOL exemption entirely), eval 7
  (focus on historical-vs-forward could not be determined mechanically;
  flagged manual_review, counted as not-passed), eval 9 (lost the API-vs-RPA
  discussion and the 5+ enumerated phases).
- The most stable with-skill advantages across both iterations: eval 5
  (enhanced-due-diligence depth for the foreign trustee) and eval 9
  (API-vs-RPA tradeoff and exception taxonomy), where the baseline fails
  repeatedly.

## Status of Iteration-1 Recommendations

From `iteration-1/benchmark.json` and `iteration-1/final_benchmark.json`
analyst observations:

| Recommendation | Status |
|---|---|
| Add depth-of-analysis assertions (citations, edge cases, steps) | **Partially implemented.** Depth assertions were added to the iteration-1 `eval_metadata.json` files in round 2 — but the iteration-2 metadata is byte-identical to iteration-1, so assertions were NOT further strengthened between iterations, and they were never back-ported to `evals/evals.json` until this audit fix (now synced). |
| Add safety assertions (e.g. NIIT warnings) | **Not implemented.** No safety-type assertions exist in any eval_metadata.json. |
| Add NUA (net unrealized appreciation) treatment to the reg-bi skill | **Implemented** — `plugins/compliance/skills/reg-bi/SKILL.md` now covers NUA. |
| Add FATCA/CRS coverage (account-opening-compliance) | **Implemented** — `plugins/client-operations/skills/account-opening-compliance/SKILL.md` now covers FATCA, and the iteration-2 with-skill eval-5 response reflects it. |
| Add CAPM/Treynor metrics to historical-risk skill | **Not implemented** — no CAPM/Treynor content in `plugins/wealth-management/skills/historical-risk/`. |
| NSCC interface details (transfers/STP) | **Partially implemented** — NSCC appears in `account-transfers/SKILL.md` but not in `stp-automation/SKILL.md`. |

## Caveats

- Because eval assertions are unchanged between iterations, iteration 2
  measures response variance plus the few skill-content updates above — not
  performance against a harder bar.
- Assertion pass rates are near ceiling for both variants; they undercount
  the qualitative gap documented in iteration-1's qualitative review (which
  was not repeated for iteration 2).
- One assertion (eval 7 without-skill conceptual focus) requires manual
  review and is counted as not-passed.
