# Quarterly Billing Process: Structure and Edge Cases

## Billing Calculation Structure

Your setup -- quarterly billing in advance on prior quarter-end AUM, with proration for new accounts and refunds for mid-quarter terminations -- is the most common RIA billing model. Here is how to structure it systematically.

### Step-by-Step Calculation Process

**1. Determine Household Composition.** Identify all accounts linked to each billing household: individual, joint, IRA, Roth IRA, trust, UGMA/UTMA, entity accounts, and any held-away assets included per the advisory agreement.

**2. Retrieve Account Valuations.** Pull market values as of the last business day of the prior quarter (your valuation date) from the custodian or portfolio management system. Apply any contractual exclusions (cash exclusions, margin debit netting, held-away asset inclusion).

**3. Aggregate Household AUM.** Sum billable market values across all accounts in the household to determine the household-level AUM for fee-tier determination.

**4. Apply Fee Schedule.** Calculate the annual fee using the household's assigned fee schedule. If you use a tiered (declining-rate) schedule, each dollar is billed at the rate for the tier it falls within. For example, on a household with $1,800,000:

| Tier | AUM Range | Rate | Fee |
|------|-----------|------|-----|
| 1 | First $500,000 | 1.00% | $5,000 |
| 2 | Next $500,000 | 0.80% | $4,000 |
| 3 | Remaining $800,000 | 0.60% | $4,800 |
| **Total** | | **Effective: 0.767%** | **$13,800** |

**5. Convert to Quarterly Fee.** Divide the annual fee by 4.

**6. Apply Overrides and Adjustments.** Check for negotiated rate overrides, minimum fee floors, fee caps, waivers, or credits. Apply in this order: calculate standard fee, apply negotiated rate, apply minimum, apply cap, apply waivers.

**7. Allocate to Accounts.** Distribute the household fee across individual accounts pro rata by market value. This ensures each account bears its proportionate share.

**8. Prorate New Accounts.** For accounts funded mid-quarter, calculate:

```
Prorated Fee = Full-Quarter Fee * (Days from Funding Date to Quarter End / Total Days in Quarter)
```

For example, an account funded on day 20 of a 91-day quarter: prorate for 71/91 of the quarter.

**9. Handle Rounding.** Round each account fee to the nearest cent. Allocate any rounding difference (the gap between the sum of rounded account fees and the household fee) to the largest account to ensure the total matches exactly.

**10. Generate Billing Output.** Produce the custodian debit instruction file, billing detail report, and audit trail record.

### Proration for New Accounts

Since you bill in advance, a new account funded mid-quarter should be prorated from its funding date through the end of the quarter. There are two common approaches:

- **Day-count proration (recommended):** Fee proportional to the number of days from funding date to quarter-end divided by total days in the quarter.
- **Midpoint rule (simpler):** Only bill for the partial quarter if the account was funded before the midpoint of the quarter; otherwise, start billing in the next quarter. This is less precise but reduces operational complexity.

The day-count method is standard and preferable for accuracy.

### Termination Refunds

For advance-billed accounts terminated mid-quarter, the refund formula is:

```
Refund = Quarterly Fee * (Remaining Days from Termination to Quarter End / Total Days in Quarter)
```

For example, if a client terminates on day 71 of a 91-day quarter, the unused portion is 20/91 of the quarterly fee. Your advisory agreement should specify this refund methodology explicitly.

Refunds can be processed as a credit on the next billing cycle or as a direct payment, depending on your operational preference. If the account is fully closed, you will need to issue a refund payment since there is no future billing cycle to credit.

## Edge Cases to Handle

### Mid-Quarter Cash Flows

**Large contributions.** Consider prorating additional fees for material contributions received mid-quarter. Define a materiality threshold in your billing policy (e.g., contributions exceeding $10,000 or 10% of account value). Below the threshold, no adjustment is made until the next regular billing cycle. Above the threshold, calculate an additional prorated fee for the remaining days in the quarter and apply it as an adjustment on the next billing run.

**Large withdrawals.** Mirror the contribution logic. If a client withdraws a material amount mid-quarter and you already billed in advance on the higher AUM, you may owe a partial credit. Whether you do this depends on your advisory agreement -- some firms only adjust for contributions, not withdrawals.

### Intra-Household Transfers

When assets move between accounts within the same household (e.g., from a taxable account to a newly opened Roth IRA), the household AUM does not change. These transfers should be revenue-neutral. No fee adjustment is needed at the household level, though per-account allocations will shift.

### Rounding Discrepancies

When per-account fees are rounded independently, the sum will occasionally differ from the household fee by a few cents. Always allocate the rounding difference to a designated account (typically the largest) so the total debited equals the household fee exactly. Without this, small discrepancies accumulate and create reconciliation problems.

### Retirement Account Billing

If fees are debited from IRAs or other tax-advantaged accounts, ensure the fee corresponds to services for that account's assets specifically. Debiting an IRA for fees covering financial planning or services unrelated to the IRA assets can trigger a taxable distribution. Many clients prefer fees debited from taxable accounts to preserve tax-advantaged balances.

### Custodian Billing Window

Each custodian (Schwab, Fidelity, Pershing, etc.) has a defined window for accepting fee debit instructions, typically the first 10-15 business days of the quarter. Missing this window delays collection by an entire quarter. Build calendar reminders and operational checklists around these deadlines.

### Custodian Confirmation Reconciliation

After submitting debit instructions, the custodian returns a confirmation file showing which debits were processed and which were rejected (insufficient funds, account closed, etc.). Always review this file. Rejected debits that go unnoticed mean uncollected revenue.

### Fee Schedule Misapplication

If you have multiple fee schedules (standard, legacy, negotiated), confirm the correct schedule is assigned to each household before every billing run. When you update your published fee schedule, decide whether existing clients are grandfathered or migrated, and ensure the billing system reflects this.

### Minimum Fees

If your practice applies a minimum quarterly fee (e.g., $250/quarter), apply it at the household level, not the individual account level. Calculate the standard fee first; if it falls below the minimum, charge the minimum instead.

### Billing Preview and Approval

Before submitting debit instructions, run the billing engine in preview mode. Review the output for anomalies: unusually large or small fees, zero-dollar fees, negative fees, and fees that deviate significantly from the prior quarter. Investigate exceptions before an authorized person approves the final run. This catches errors before they reach clients.

## Revenue Recognition Note

Since you bill in advance, fees collected at the start of Q2 represent a deferred revenue liability on your balance sheet. Under GAAP, recognize this revenue ratably over the quarter -- one-third per month. When a client terminates mid-quarter and you issue a refund, reduce the deferred revenue balance and the refund amount accordingly.

## Compliance Disclosure Requirements

Your ADV Part 2A (Item 5) must clearly disclose:

- Your fee schedule and how fees are calculated
- That you bill quarterly in advance based on prior quarter-end AUM
- Your proration methodology for new accounts
- Your refund policy for mid-quarter terminations
- The collection method (custodian direct debit vs. invoice)
- Any other costs clients bear (fund expenses, custodian fees, transaction costs)

If you serve retirement plans, ERISA Section 408(b)(2) requires additional detailed disclosure of all direct and indirect compensation before the engagement begins.

## Summary Checklist

1. Pull valuations as of last business day of prior quarter
2. Aggregate accounts into billing households
3. Apply the correct fee schedule per household (tiered, flat, negotiated)
4. Calculate annual fee, divide by 4 for quarterly
5. Allocate to accounts pro rata by market value
6. Prorate new accounts from funding date (days active / total days)
7. Calculate termination refunds (remaining days / total days)
8. Apply rounding allocation to largest account
9. Run billing preview; investigate exceptions
10. Obtain approval; submit custodian debit files within the billing window
11. Reconcile custodian confirmation files for rejected debits
12. Record deferred revenue and recognize ratably over the quarter
