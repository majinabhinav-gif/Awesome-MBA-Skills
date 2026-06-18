# Qualitative Comparison: With-Skill vs Without-Skill Responses

## Scoring Scale

- **1** = Missing or incorrect
- **2** = Superficial / vague
- **3** = Adequate for a generalist
- **4** = Strong, would satisfy a practicing professional
- **5** = Exceptional, peer-review quality for a finance professional

---

## Eval 1: Reg BI Rollover (401(k)-to-IRA, dual-registrant, age 58, $340K)

### Scores

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 5 | 5 |
| Actionable Detail | 5 | 5 |
| Edge Case Awareness | 4 | 5 |
| Overall Quality | 5 | 5 |

### Key Differences

Both responses are exceptionally strong. They cover the same core ground: capacity determination for dual-registrants, Reg BI's four obligations, IA fiduciary duty under Sections 206(1)/206(2), the four-alternatives analysis from the SEC Staff Bulletin, the age-55 separation-from-service rule, creditor protection, Form CRS delivery, and PTE 2020-02.

**Only in with_skill:**
- Explicit warning about "hat-switching" between BD and IA capacity
- Structured the documentation requirements separately for Reg BI vs IA fiduciary, making it clearer which items are additive under fiduciary duty (items 8-11)
- ADV Part 2A/2B delivery mentioned as a specific documentation item under IA capacity
- Summary table at the end

**Only in without_skill:**
- IRC Section 72(t)(2)(A)(v) statutory citation for the age-55 rule
- FINRA Regulatory Notice 13-45 cited as additional rollover guidance
- Net Unrealized Appreciation (NUA) analysis for employer stock -- a genuinely important edge case
- Roth conversion opportunity flagged as a rollover consideration
- Quantified fee differential example ($0.25% = meaningful over time)
- Collected regulatory references section at the end
- "When in doubt, apply the higher fiduciary standard" practical advice

### Verdict

**The skill does NOT add meaningful value for this question.** The without_skill response is marginally better due to NUA coverage, the IRC citation, and FINRA 13-45 reference. Both are excellent. The skill response is slightly more structured (separate BD vs IA documentation lists, summary table) but the without_skill response covers more edge cases. This is essentially a tie, with a slight edge to without_skill.

---

## Eval 2: Fiduciary Duty -- Proprietary Fund Recommendation (RIA, retired teacher, $600K)

### Scores

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 5 | 4 |
| Actionable Detail | 5 | 4 |
| Edge Case Awareness | 5 | 4 |
| Overall Quality | 5 | 4 |

### Key Differences

Both responses correctly identify this as a fiduciary issue under IA Act Sections 206(1)/206(2), cite the 2019 Fiduciary Interpretation, discuss the share-class selection enforcement sweep, and provide actionable remediation steps.

**Only in with_skill:**
- Release number IA-5248 for the 2019 Fiduciary Interpretation
- SEC Rule 206(4)-7 (compliance policies requirement)
- Explicit statement that generic ADV language like "we may recommend affiliated products" is insufficient -- a specific, practical compliance insight
- The "Mitigation Hierarchy" framework (Eliminate > Mitigate > Disclose) with the critical point that "disclosure does not cure a bad recommendation" and an adviser cannot "disclose away" a conflict
- Distinction between disclosure and informed consent (fiduciary requires the latter, not just the former)
- "Layered conflict" concept -- revenue at both advisory-fee and product-fee levels
- Compensation leveling as a specific structural mitigation
- Retrospective compliance review concept

**Only in without_skill:**
- Quantified the cost drag over a 20-year horizon ($70K-$100K), making the impact tangible for the client scenario
- SEC Risk Alert from November 2020 on examination observations
- Form ADV Part 2A Item 10 cited specifically
- Mentioned tax-loss harvesting as a potential justification for proprietary funds
- "Over $100 million in disgorgement" quantification of the share-class enforcement sweep

### Verdict

**The skill adds meaningful value for this question.** The with_skill response demonstrates noticeably deeper regulatory reasoning: the mitigation hierarchy, the disclosure-vs-consent distinction, the "disclosure does not cure" principle, and the specific release number. These are the kinds of insights that separate a compliance-aware response from a general one. The without_skill response is good but reads more like a well-informed overview; the with_skill response reads like it came from someone who has worked through enforcement proceedings.

---

## Eval 11: Core -- TWR vs MWR Calculation

### Scores

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 4 | 3 |
| Actionable Detail | 5 | 5 |
| Edge Case Awareness | 5 | 4 |
| Overall Quality | 5 | 4 |

### Key Differences

Both responses arrive at the correct answers: TWR = 24.06%, MWR approximately 22.6%. Both show their work step-by-step and explain why TWR exceeds MWR in this scenario.

**Only in with_skill:**
- Used the standard NPV = 0 IRR equation formulation (`0 = -100,000 + (-50,000)/(1+r)^0.5 + 178,000/(1+r)^1`), which is the textbook-correct present-value formulation
- Showed iterative convergence with explicit NPV checks at each trial rate, demonstrating the actual numerical method (trial-and-error with interpolation)
- Linear interpolation step between 22% and 23% explicitly shown
- Verification step (plugging r = 22.63% back in to confirm NPV near zero)
- Final observation: "If the client had instead added the $50,000 before the stronger first half, the MWR would have exceeded the TWR" -- a useful counterfactual that deepens understanding

**Only in without_skill:**
- Used the future-value equation formulation (`100K(1+r) + 50K(1+r)^0.5 = 178K`), which is algebraically equivalent but presented differently
- GIPS (Global Investment Performance Standards) mentioned as requiring TWR for manager performance reporting -- a valuable regulatory/industry-standards reference
- Cleaner "When to Use Each" comparison table

### Verdict

**The skill adds modest value for this question.** The with_skill response is more rigorous in its numerical method (NPV formulation, interpolation, verification step) and includes the useful counterfactual. The without_skill response compensates with the GIPS reference, which is practically important for anyone in the performance measurement space. The skill's main advantage is pedagogical thoroughness -- it teaches the method more completely. For a finance professional who needs to reproduce the calculation, the with_skill version is more useful.

---

## Eval 13: Rebalancing + Tax-Loss Harvesting Coordination ($800K, 60/40, $15K unrealized losses)

### Scores

| Dimension | With Skill | Without Skill |
|---|---|---|
| Regulatory Precision | 4 | 3 |
| Actionable Detail | 5 | 4 |
| Edge Case Awareness | 5 | 3 |
| Overall Quality | 5 | 4 |

### Key Differences

Both responses correctly identify the drift, calculate the $64,000 rebalancing trade, and describe coordinating the TLH with the rebalance. Both cover wash-sale basics and lot selection.

**Only in with_skill:**
- Quantified tax savings across three rate scenarios (15% LTCG, 20%+NIIT, 20%+NIIT+state) with dollar amounts ($2,250-$4,320)
- NIIT (Net Investment Income Tax) 3.8% threshold mentioned with MAGI limits ($250K MFJ / $200K single)
- Short-term vs long-term loss distinction and its impact on tax benefit
- $3,000 ordinary income offset rule AND the $12,000 carryforward explicitly calculated
- HIFO (Highest In, First Out) lot selection strategy named and explained
- Specific replacement security examples with correlation target (0.95+) and tracking error threshold (under 2% annualized)
- Prioritized sell order (losses first, then near-basis, then appreciated last)
- Cross-account wash-sale compliance: explicitly lists IRA, Roth IRA, 401(k), HSA, and spouse accounts
- DRIP suspension during the wash-sale window
- 401(k) fund reallocation during wash-sale window if it tracks the same index
- Swap-back evaluation after 31 days (warns about gains on replacement)
- Tax-deferred account rebalancing as an alternative to reduce taxable gains
- "Do not over-harvest" warning with explanation of basis reduction trade-off
- Before/after summary table with estimated tax savings
- Upcoming cash flows as a partial rebalancing alternative

**Only in without_skill:**
- Net tax impact calculation showing how harvested losses offset gains from other rebalancing sales (netting example)
- Practical note that wash sale concern is reduced when rebalancing down in equities (you may not need to replace)
- Transaction costs and bid-ask spread caveat
- Natural drift consideration (whether contributions/withdrawals might close the gap)

### Verdict

**The skill adds substantial value for this question.** This is the clearest differentiation across all four evals. The with_skill response is dramatically more comprehensive on tax mechanics (NIIT, rate scenarios, HIFO, cross-account wash sales, DRIP suspension, 401(k) index overlap). The without_skill response is competent but omits several non-obvious pitfalls that could cost a real client money -- particularly the cross-account wash-sale triggers and the DRIP suspension. For a wealth management professional, the with_skill response is materially more useful and safer to act on.

---

## Aggregate Summary

| Eval | With Skill | Without Skill | Skill Delta | Verdict |
|---|---|---|---|---|
| 1 -- Reg BI Rollover | 4.75 | 5.00 | -0.25 | No value added (without_skill slightly better) |
| 2 -- Fiduciary/Proprietary | 5.00 | 4.00 | +1.00 | Meaningful value added |
| 11 -- TWR vs MWR | 4.75 | 4.00 | +0.75 | Modest value added |
| 13 -- Rebalance + TLH | 4.75 | 3.50 | +1.25 | Substantial value added |
| **Average** | **4.81** | **4.13** | **+0.69** | |

### Overall Findings

1. **Skills help most on multi-step quantitative + regulatory intersections.** The rebalance/TLH eval showed the largest gap because it requires coordinating tax law (wash sales, NIIT, lot selection), portfolio math, and practical execution sequencing. The skill structured this knowledge in a way that produced meaningfully safer, more actionable output.

2. **Skills help on compliance nuance.** The fiduciary/proprietary eval showed that the skill produced deeper regulatory reasoning (mitigation hierarchy, disclosure-vs-consent) that a compliance officer would value.

3. **Skills help less when base model knowledge is already strong.** The Reg BI rollover question is well-covered in Claude's training data. The without_skill response was equally good and actually covered an edge case (NUA) that the with_skill response missed.

4. **Quantitative skills provide pedagogical rigor.** The TWR/MWR skill produced a more methodologically complete calculation, though both arrived at the correct answer.

5. **Key pattern: skills excel at checklists and cross-domain interactions.** The most valuable skill contributions were exhaustive checklists (cross-account wash-sale sources, DRIP suspension, documentation requirements) and connections between domains (tax rates + rebalancing mechanics + wash-sale compliance).
