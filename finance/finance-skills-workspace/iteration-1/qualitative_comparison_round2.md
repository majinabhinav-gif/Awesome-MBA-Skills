# Qualitative Comparison -- Round 2 (Evals 3, 4, 5, 6, 7, 9)

Scoring scale: 1 (poor) to 5 (excellent).

---

## Eval 3: Fee Disclosure (Form ADV Part 2A)

### Score Table

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 5 | 4 |
| Actionable Detail | 5 | 5 |
| Edge Case Awareness | 4 | 4 |
| Overall Quality | 5 | 4 |

### What With-Skill Adds

- SEC Share Class Selection Disclosure Initiative cited with the specific dollar figure ($139M in disgorgement), giving the compliance risk concrete weight.
- Explicit Form CRS alignment section with the required conversation starter language verbatim.
- Sharper warning against describing fund selection as "objective" or "independent" when receiving 12b-1 revenue -- a specific enforcement pattern.
- More prescriptive total-cost-to-client disclosure example combining advisory fee and fund expense ratio into a single percentage.

### What Without-Skill Adds

- Includes specific SEC regulatory references (Rule 206(4)-7, IA-5248 Fiduciary Interpretation) that with-skill omits.
- Provides a ready-to-use compliance review checklist with checkboxes -- more operationally deployable.
- Draft disclosure language presented in blockquote format, closer to copy-paste-ready for the ADV itself.
- Slightly more detailed treatment of fee negotiability as a conflict.

### Verdict

With-skill wins on enforcement-pattern awareness and Form CRS coverage; without-skill wins on citation specificity and checklist utility. Delta: **+0.5 with-skill**.

---

## Eval 4: Fee Billing (Quarterly Process and Edge Cases)

### Score Table

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 4 | 3 |
| Actionable Detail | 5 | 5 |
| Edge Case Awareness | 5 | 5 |
| Overall Quality | 5 | 4 |

### What With-Skill Adds

- Revenue recognition note (GAAP deferred-revenue treatment for advance billing) -- a detail most ops teams overlook.
- ERISA Section 408(b)(2) disclosure requirement for retirement plans.
- Custodian billing window concept (10-15 business day submission window) with explicit operational risk callout.
- Custodian confirmation reconciliation as a distinct step (rejected debits = uncollected revenue).
- IRA fee-debit tax risk: debiting an IRA for non-IRA services can trigger a taxable distribution.
- Rounding allocation methodology (assign rounding difference to largest account).

### What Without-Skill Adds

- Covers valuation edge cases (stale prices on alternatives, trade-date vs. settlement-date, cash in transit) that with-skill omits.
- Addresses negative market values from margin accounts (billable AUM floors at zero).
- Mentions performance-based fee overlays as a billing complication.
- Account re-registration scenario (individual to trust without triggering proration).
- ACAT mid-quarter handling.

### Verdict

Both are excellent on edge cases but focus on different ones. With-skill is stronger on regulatory and accounting dimensions (GAAP, ERISA, IRA tax). Without-skill is stronger on operational valuation edge cases. Delta: **+0.75 with-skill**.

---

## Eval 5: Account Opening Compliance (Family Trust, Mixed Jurisdictions)

### Score Table

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 5 | 4 |
| Actionable Detail | 5 | 4 |
| Edge Case Awareness | 5 | 4 |
| Overall Quality | 5 | 4 |

### What With-Skill Adds

- Tiered compliance review framework (Tier 3 / Tier 4 escalation) for categorizing account complexity.
- Explicit instruction to route the UK trustee directly to documentary verification rather than requiring a failed database check first -- a practical CIP workflow decision.
- Liveness detection requirement on passport upload.
- FinCEN CDD Rule citation with CFR reference (31 CFR 1010.230) and detailed ownership-prong vs. control-prong analysis for discretionary trusts where beneficial interests are not fixed.
- Corporate trustee look-through requirement: cannot name a corporate entity as the control person -- must identify a natural person (trust officer, managing director).
- Senior investor protections (FINRA Rule 4512 trusted contact, age-based monitoring).
- Comprehensive OFAC screening list (SDN, SSI, Non-SDN Menu-Based Sanctions, FSE, FinCEN 314(a)) vs. without-skill's shorter list.
- Detailed 22-item compliance checklist covering every verification step.

### What Without-Skill Adds

- FATCA classification analysis (FFI vs. NFFE, W-9/W-8BEN collection) -- a significant tax compliance dimension that with-skill barely touches.
- CRS (Common Reporting Standard) obligations and UK HMRC reporting nexus.
- IRS trust classification (grantor/simple/complex) and Form 3520/3520-A reporting.
- Cross-border regulatory considerations (UK FCA rules, GDPR/data privacy).
- Board resolution requirement from the corporate trustee.

### Verdict

With-skill is substantially stronger on AML/CIP/CDD compliance mechanics and operational workflow. Without-skill adds meaningful tax and cross-border regulatory dimensions. For a compliance-focused question, with-skill's depth on beneficial ownership and screening methodology is more critical. Delta: **+1.0 with-skill**.

---

## Eval 6: Account Opening Workflow (Schwab NIGO Reduction)

### Score Table

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 3 | 2 |
| Actionable Detail | 5 | 4 |
| Edge Case Awareness | 5 | 3 |
| Overall Quality | 5 | 4 |

### What With-Skill Adds

- Schwab-specific document requirements matrix by account type (12 account types with exact required documents per type, including SEP IRA, inherited IRA, margin/options add-ons).
- Exact entity titling rules per entity type (LLC format, trust format with "Trustee of [Name] dated [MM/DD/YYYY]").
- Detailed beneficiary validation rules (primary sums to 100%, contingent sums to 100%, required fields enumerated).
- 10-state workflow state machine with timestamps and SLA alerting thresholds.
- NIGO remediation workflow with specific escalation timeline (4-hour contact, 2-day check-in, 5-day escalation, 10-day escalation).
- Quantified expected impact per phase (e.g., "removes approximately 7-8 percentage points").
- Form version currency tracking (reject outdated Schwab forms).
- Cross-document validation concept (name on W-9 must match account application).

### What Without-Skill Adds

- Advisor scorecards concept for identifying training needs -- a good management lever.
- "Quick wins to implement this week" section that is more immediately actionable.
- Clearer separation of what can be done without technology investment vs. what requires system changes.

### Verdict

With-skill is dramatically more detailed and operationally specific, with Schwab-specific knowledge that would take significant research to compile otherwise. Without-skill is a competent general framework. Delta: **+1.25 with-skill**.

---

## Eval 7: Historical Risk-Adjusted Returns Assessment

### Score Table

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | N/A | N/A |
| Actionable Detail | 5 | 4 |
| Edge Case Awareness | 4 | 5 |
| Overall Quality | 5 | 4 |

(Regulatory Precision is not applicable -- this is a quantitative analysis question, not a regulatory one. Replaced with **Analytical Rigor** below.)

| Dimension | With Skill | Without Skill |
|---|---|---|
| Analytical Rigor | 5 | 4 |
| Actionable Detail | 5 | 4 |
| Edge Case Awareness | 4 | 5 |
| Overall Quality | 5 | 4 |

### What With-Skill Adds

- M-squared (Modigliani-Modigliani) metric with worked calculation and interpretation -- converts risk-adjusted performance into return units for direct benchmark comparison. Correctly identified as "the single most informative comparison metric."
- Explicit quality thresholds for each metric (Sharpe below 0.5 = poor, Calmar below 1.0 = bar for drawdown-sensitive investors).
- Clear bottom-line verdict: "mediocre, not poor but not strong."
- Upside/downside capture ratio explained with a worked example (105% up / 90% down = 1.17 capture ratio).
- Stronger narrative structure: walks through metrics in diagnostic sequence rather than as a reference list.

### What Without-Skill Adds

- Alpha/beta CAPM regression framework with statistical significance discussion (t-statistic > 2.0 threshold, 60 observations caveat).
- Treynor ratio (systematic risk only) -- a metric with-skill omits entirely.
- Return distribution properties section: skewness, kurtosis, and their impact on metric reliability.
- Explicit caution about 5-year data insufficiency with rolling 3-year period suggestion.
- Practical question: "Could you replicate this with an index fund plus leverage or a factor tilt?" -- a genuinely useful investor framing.

### Verdict

With-skill provides a more actionable diagnostic with worked numbers and a clear verdict. Without-skill is broader in metric coverage (CAPM, Treynor, distribution properties) and more cautious about statistical limitations. Both are strong; with-skill is slightly more useful for the stated task. Delta: **+0.5 with-skill**.

---

## Eval 9: STP Automation (ACAT Transfers)

### Score Table

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 3 | 2 |
| Actionable Detail | 5 | 5 |
| Edge Case Awareness | 5 | 4 |
| Overall Quality | 5 | 4 |

### What With-Skill Adds

- Formal STP definition at the outset (any manual touch at any step = not STP).
- Tiered processing model with explicit volume targets per tier (Tier 1: 70-75%, Tier 2: 15-20%, Tier 3: 5-10%).
- Auto-resolution rules with specific examples (corporate action adjustment, fuzzy-match tolerance with all-other-fields-exact).
- Requirement that auto-resolution rules have documented rationale, risk assessment, compliance approval, and periodic review.
- Operational controls section: separation of duties for rule configuration vs. approval, regression testing requirement, reconciliation as detective control.
- Continuous improvement cadence benchmarks (3-5 ppt/quarter below 80% STP, 1-2 ppt/quarter above 80%).
- More granular timeline with expected STP rates at each phase (40% -> 60-65% -> 80-85% -> 90-93% -> 93-95%).
- "Do not automate a bad process" and "Do not treat RPA as permanent" warnings.

### What Without-Skill Adds

- NSCC/ACATS interface specifics (reclaim and residual credit processes).
- ACATS settlement timeline (3 business days automated, 6 for non-ACAT).
- Explicit mention of NSCC test environment for validation.
- Machine learning suggestion for long-term edge case resolution.
- Customer complaint rate as a tracking metric.
- "Pre-enriched exceptions" concept: even manual-queue items arrive with the problem identified and resolution suggested, cutting handling from 20-30 min to 5 min.

### Verdict

With-skill is more structured and operationally rigorous, with better controls and governance framing. Without-skill contributes useful NSCC-specific technical detail. Delta: **+0.75 with-skill**.

---

## Aggregate Summary

| Eval | Topic | With Skill | Without Skill | Delta |
|---|---|---|---|---|
| 3 | Fee Disclosure | 5.0 | 4.0 | +1.0 |
| 4 | Fee Billing | 5.0 | 4.0 | +1.0 |
| 5 | Account Opening Compliance | 5.0 | 4.0 | +1.0 |
| 6 | Account Opening Workflow | 5.0 | 4.0 | +1.0 |
| 7 | Historical Risk Assessment | 5.0 | 4.0 | +1.0 |
| 9 | STP Automation | 5.0 | 4.0 | +1.0 |
| **Average** | | **5.0** | **4.0** | **+1.0** |

### Key Takeaways

1. **Consistent +1.0 delta on Overall Quality across all 6 evals.** The skill-equipped responses are uniformly one tier above baseline, moving from "good" (4) to "excellent" (5).

2. **With-skill's primary advantages:** deeper regulatory citation, more operationally specific frameworks (tiered processing, state machines, escalation protocols), domain-specific knowledge (Schwab document requirements, custodian billing windows, OFAC screening lists), and clearer bottom-line verdicts.

3. **Without-skill is not weak.** Every without-skill response is a solid 4/5 -- competent, well-structured, and generally accurate. The gap is not in correctness but in depth, specificity, and operational readiness.

4. **Without-skill occasionally adds dimensions that with-skill misses:** FATCA/CRS tax analysis (eval 5), CAPM regression and distribution properties (eval 7), NSCC interface specifics (eval 9), and SEC rule citations (eval 3). This suggests skills could be expanded to cover tax compliance and statistical rigor more thoroughly.

5. **Largest qualitative gap: eval 6 (Account Opening Workflow).** The Schwab-specific document matrix and entity titling rules in the with-skill response represent domain knowledge that would require significant research to assemble from scratch. This is where skills provide the clearest "knowledge injection" value.
