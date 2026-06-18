# Structuring Your Quarterly Advance Billing Process

## Billing Calculation Framework

Your setup -- quarterly billing in advance on prior quarter-end AUM, with new account proration and mid-quarter termination refunds -- is the most common RIA billing model. Here is how to structure the calculation, following the standard ten-step process.

### Step-by-Step Calculation

**1. Determine household composition.** Identify every account linked to each billing household: individual, joint, IRA, Roth IRA, trust, UGMA/UTMA, entity accounts. The household definition must match what is documented in each advisory agreement.

**2. Retrieve account valuations.** Pull market values as of the last business day of the prior quarter from your custodian position files. Apply any agreement-specific exclusions (cash exclusions, margin debit netting, held-away asset inclusion).

**3. Aggregate household AUM.** Sum billable market values across all accounts in the household. This aggregate determines which fee tier applies.

**4. Apply the fee schedule.** Calculate the annual fee using your tiered or flat schedule against the household-level AUM. For a tiered schedule, apply each tier's rate only to the dollars falling within that tier's range.

Example for a $1,800,000 household under a tiered schedule:

| Tier | AUM Range | Rate | Fee |
|------|-----------|------|-----|
| 1 | First $500K | 1.00% | $5,000 |
| 2 | Next $500K | 0.80% | $4,000 |
| 3 | Remaining $800K | 0.60% | $4,800 |
| **Annual** | | **Effective: 0.767%** | **$13,800** |

**5. Convert to quarterly.** Divide the annual fee by 4.

```
Quarterly Fee = $13,800 / 4 = $3,450.00
```

**6. Apply overrides and adjustments.** Check for negotiated rate overrides, minimum fee floors, fee caps, and waivers. Apply in order: standard calculation, then negotiated rate, then minimum, then cap, then waivers.

**7. Allocate to accounts.** Distribute the household fee across individual accounts pro rata by market value.

**8. Prorate new accounts** (see below).

**9. Apply rounding.** Round each account fee to the nearest cent. Allocate any rounding remainder (positive or negative) to the largest account in the household so account-level fees sum exactly to the household fee.

**10. Generate billing output.** Produce the custodian debit instruction file and the billing detail report with full audit trail.

---

## New Account Proration

For accounts funded mid-quarter, calculate the fee based on the number of days the account was active relative to the total days in the billing period:

```
Prorated Fee = Full-Quarter Fee * (Days from Funding Date to Quarter-End / Total Days in Quarter)
```

For example, if Q1 runs January 1 through March 31 (90 days) and a new account is funded on February 15 (day 46), the account is active for 44 days:

```
Prorated Fee = Full-Quarter Fee * (44 / 90)
```

Since you bill in advance on prior quarter-end AUM, new accounts opened mid-quarter will not have a prior quarter-end value. You should bill these accounts based on their funding-date market value, prorated for the remaining days in the quarter. Include the prorated charge as an adjustment on the current quarter's billing run or, if the billing run has already been submitted, as an adjustment line item on the next quarter's run.

---

## Mid-Quarter Termination Refunds

When a client terminates mid-quarter and you have already collected the full quarter's fee in advance, you owe a refund for the unused portion:

```
Refund = Quarterly Fee * (Remaining Days from Termination to Quarter-End / Total Days in Quarter)
```

For example, if a client terminates on day 71 of a 91-day quarter, the unused portion is 20 days:

```
Refund = $500.00 * (20 / 91) = $109.89
```

Apply the refund as a credit on the next billing cycle, or issue a direct refund if the account is fully closing and there will be no future billing cycle to net against. Your advisory agreement should specify the refund methodology so there is no ambiguity at termination.

---

## Edge Cases You Need to Handle

### Valuation and Timing

- **Last business day definition.** Define clearly what "last business day" means -- market holidays, early closes, and custodian processing schedules can create ambiguity. Use the custodian's official end-of-day valuations for that date.
- **Stale or missing valuations.** If a custodian feed is delayed or an account's valuation is missing on the billing date, have a fallback process (e.g., use the most recent available valuation and flag the account for manual review).
- **Held-away assets.** If any accounts include held-away assets in billable AUM per the advisory agreement, obtaining timely valuations from external custodians is a persistent challenge. Build a process to request and verify these values before each billing run.

### Proration and Day-Count

- **Day-count consistency.** Use the same day-count convention for both new account proration and termination refunds. Calendar days (not business days) is the standard. Document the convention.
- **Funding date vs. account open date.** A new account may be opened on one date but not funded until later. Bill from the funding date (when assets are present to manage), not the account open date.
- **Multiple fundings.** If a new account receives several tranches of funding over the first few weeks, decide whether to prorate from the initial funding date on the total eventual balance, or to prorate each tranche separately. The simpler approach (prorate from initial funding on total balance at quarter-end) is more common.

### Mid-Quarter Events

- **Large contributions to existing accounts.** Decide whether material contributions trigger a mid-quarter fee adjustment. Many firms set a materiality threshold (e.g., contributions exceeding $10,000 or 10% of account value). If you do prorate for contributions, the additional charge is calculated on the contribution amount for the remaining days in the quarter and added to the next billing cycle.
- **Large withdrawals.** The mirror of contributions. If a client withdraws a large amount, you may owe a partial refund or credit. Apply the same materiality threshold and proration logic.
- **Internal transfers between household accounts.** Transfers within the same household (e.g., from taxable to IRA) should be revenue-neutral. The household AUM does not change, so no fee adjustment is needed. Update per-account allocations going forward but do not change the household-level fee.
- **Partial termination.** A client closes one account but keeps others. Refund the prorated fee for the terminated account. The remaining accounts continue to be billed normally; recalculate the household tier at the next full billing cycle.

### Billing Mechanics

- **Rounding discrepancies.** When you allocate a household fee across multiple accounts and round each to the nearest cent, the sum of account-level fees may not equal the household fee. Always allocate the rounding remainder to a designated account (typically the largest) so the totals reconcile exactly.
- **Minimum fee floors.** If you have a minimum quarterly fee (e.g., $250), apply it at the household level, not per account. A new prorated account may calculate below the minimum -- decide whether the minimum applies to prorated first-quarter fees or only to full quarters.
- **Fee caps on negotiated accounts.** If a household has a negotiated cap, verify the cap is applied after proration and adjustments, not before.
- **Custodian billing window.** Each custodian has a defined window for accepting fee debit instructions (typically the first 10-15 business days of the quarter). Missing this window delays collection by an entire quarter. Build your billing timeline to complete preview, review, approval, and submission well within the window.
- **Debit rejections.** After submitting debit instructions, the custodian returns a confirmation file showing which debits succeeded and which were rejected (insufficient funds, account closed, etc.). Build a process to review rejections and re-collect rejected amounts.

### Compliance and Documentation

- **Advisory agreement alignment.** Every element of your billing process -- valuation date, proration method, refund policy, household definition, fee schedule -- must match what is documented in the client's advisory agreement. Discrepancies are a common SEC examination finding.
- **ADV Part 2A disclosure.** Item 5 of Form ADV Part 2A must clearly describe your billing methodology: that fees are billed quarterly in advance, based on prior quarter-end AUM, with proration for new accounts and refunds for terminations. The disclosure must be specific enough that a client can independently verify their fee.
- **Audit trail.** Every billing run must produce a complete audit trail: valuation date and source, fee schedule applied (with version), household and per-account AUM, step-by-step calculation detail, any overrides or adjustments, the identity of the person who approved the run, and the timestamp of custodian submission.
- **IRA fee debits.** If you debit fees from retirement accounts, confirm the debit corresponds to investment management services for that account's assets. Debiting an IRA for services unrelated to the IRA (e.g., household financial planning) can trigger a taxable distribution.

### Revenue Recognition

- **Deferred revenue.** Since you bill in advance, you recognize a liability (deferred revenue) at the billing date. Revenue is then recognized ratably over the quarter -- one-third per month. Do not recognize the full fee as revenue on the billing date.
- **Refund impact.** When you issue a termination refund, reverse the corresponding deferred revenue. The refund reduces both the liability and the cash collected, with no impact on already-recognized revenue for the portion of the quarter the client was active.

---

## Recommended Billing Timeline

For a quarterly advance billing cycle (using Q2 as an example):

| Timing | Activity |
|--------|----------|
| Last business day of Q1 (Mar 31) | Valuation snapshot date |
| Business day 1 of Q2 (Apr 1) | Retrieve custodian valuations; begin billing calculation |
| Business days 2-3 | Run billing engine in preview mode; generate preview report |
| Business days 3-5 | Operations reviews preview for anomalies (unusually large fees, zero-dollar fees, large variances from prior quarter, new/terminated accounts) |
| Business days 5-6 | Resolve exceptions; apply adjustments for prior-quarter events (new account proration charges, termination refund credits) |
| Business day 7 | Authorized person approves billing run |
| Business days 7-8 | Generate custodian debit instruction files and invoices |
| Business days 8-10 | Submit debit files to custodians (well within the typical 10-15 business day window) |
| Business days 12-15 | Receive and review custodian confirmation/rejection files; follow up on rejected debits |

This timeline gives you a comfortable buffer before custodian deadlines while keeping the review process disciplined.
