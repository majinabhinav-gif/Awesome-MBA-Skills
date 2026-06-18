# Quarterly Advance Billing on AUM: Structure and Edge Cases

## Billing Calculation Structure

### 1. Standard Quarterly Bill

For existing accounts billed in advance, the calculation is straightforward:

```
Quarterly Fee = AUM (last business day of prior quarter) x (Annual Fee Rate / 4)
```

For tiered fee schedules, apply each tier's rate to the portion of AUM falling within that tier's range, then sum the results and divide by four.

### 2. New Account Proration

When an account is funded mid-quarter, prorate from the funding date through the end of the current quarter:

```
Prorated Fee = AUM (as of funding date) x (Annual Fee Rate / 4) x (Calendar Days Remaining in Quarter / Total Calendar Days in Quarter)
```

Key decisions to document in your billing policy:
- **Valuation date**: Use the AUM as of the funding date (or the next business day if funded on a non-business day).
- **Day-count convention**: Calendar days is the most common approach. Some firms use business days instead -- pick one and be consistent.
- **Billing trigger**: Define a minimum number of days (e.g., funding must occur at least 5 business days before quarter-end) below which you waive the fee or roll it into the next quarter. Billing a client $12 for three days of management creates more confusion than revenue.

### 3. Mid-Quarter Termination Refund

When a client terminates mid-quarter, refund the unused portion of the advance fee:

```
Refund = Quarterly Fee Already Billed x (Calendar Days Remaining in Quarter from Termination Date / Total Calendar Days in Quarter)
```

Alternatively, some firms calculate the earned portion and refund the difference:

```
Earned Fee = Quarterly Fee x (Calendar Days Elapsed from Quarter Start to Termination Date / Total Calendar Days in Quarter)
Refund = Quarterly Fee Already Billed - Earned Fee
```

Both approaches yield the same result. Use the termination effective date (not the date the client requested termination) for the calculation.

---

## Edge Cases to Handle

### Timing and Calendar Issues

- **Quarter-end falls on a weekend or holiday**: "Last business day of the prior quarter" needs a business day calendar. For Q1 billing (based on Dec 31 AUM), if Dec 31 is a Saturday, you use Dec 30 (Friday) valuations. Maintain a reliable business day calendar that accounts for market holidays.
- **Leap years**: Q1 has different day counts in leap vs. non-leap years. If you prorate by calendar days, your denominator changes. Make sure your day-count logic handles this.
- **Uneven quarter lengths**: Q1 = 90 or 91 days, Q2 = 91 days, Q3 = 92 days, Q4 = 92 days. If your fee schedule says "one-quarter of the annual fee," this is exact. If you prorate within a quarter, the varying lengths matter.

### Valuation Issues

- **Stale or missing prices**: If certain holdings lack a price on the valuation date (illiquid securities, alternatives, private placements), define a fallback -- prior close, manual fair value, or most recent available price. Document the policy.
- **Pending trades**: AUM on the valuation date may include unsettled trades. Decide whether you use trade-date or settlement-date accounting for the AUM snapshot. Trade-date is more common.
- **Cash in transit**: A large wire arriving or departing on the valuation date can materially affect AUM. Your policy should state whether AUM is measured at start-of-day, end-of-day, or at a specific cutoff.

### Account-Level Complications

- **Household billing**: If fees are calculated at the household level (aggregating multiple accounts for tiered pricing), you need to allocate the total fee back to individual accounts. Common methods: pro-rata by AUM, or charge entirely from one designated account.
- **Fee schedule changes mid-quarter**: If a client renegotiates their fee rate effective mid-quarter, decide whether to (a) apply the new rate starting next quarter, (b) prorate between old and new rates, or (c) refund/credit the difference. Option (a) is simplest.
- **Account additions to existing relationships**: A new account for an existing client may get household-level tiering from day one but still needs proration for the partial quarter.
- **Sleeves or sub-accounts**: If a client has multiple sleeves managed by different strategists with different fee rates, each sleeve needs its own calculation against the correct fee schedule.

### Cash Flow Events

- **Large deposits or withdrawals mid-quarter**: Since you bill in advance on beginning-of-quarter AUM, intra-quarter flows do not affect the current quarter's bill. However, your IMA (Investment Management Agreement) may include a threshold clause -- e.g., deposits or withdrawals exceeding $X or Y% of AUM trigger a mid-quarter billing adjustment. Decide whether to implement this or keep it simple.
- **Account transfers (ACAT)**: An incoming transfer that arrives after the billing date but before the next quarter requires clear policy -- typically no mid-quarter adjustment; the transferred assets get billed next quarter.

### Termination Scenarios

- **Partial account termination**: Client withdraws a large portion but keeps the account open. This is not a termination, so no refund applies -- but confirm your IMA language covers this.
- **Termination with illiquid holdings**: If the account cannot be fully liquidated (restricted stock, alternatives with lock-ups), the termination date may be ambiguous. Define whether fees continue on remaining illiquid assets or stop at the termination notice date.
- **Disputed termination date**: The client says they requested termination on March 5; your records show March 12. Use the date of written notice per the IMA, and keep a clear audit trail.
- **Death of account holder**: Triggers a different process -- fees typically continue until the account is re-registered or closed, but practices vary. Check your IMA and applicable regulations.

### Billing Minimums and Waivers

- **Minimum quarterly fee**: If your fee schedule includes a minimum (e.g., $500/quarter), apply it after the AUM-based calculation. For prorated new accounts, decide whether the minimum is also prorated.
- **Fee waivers**: Employee accounts, family accounts, or promotional rates need a way to override the standard calculation. Track these as explicit exceptions with approval documentation.

### Operational and Compliance Considerations

- **Billing in arrears for the proration**: Some firms bill new accounts in arrears for their first partial quarter (since you do not yet know the funding-date AUM when the quarter starts), then switch to advance billing. This hybrid approach adds complexity but is more accurate.
- **Audit trail**: Every billing calculation should be reproducible -- store the AUM snapshot date, the AUM value used, the fee rate, the proration factor, and the resulting fee. Regulators (SEC, state securities divisions) expect to see this documentation.
- **Client reporting**: Invoices or account statements should clearly show the billing period, AUM used, fee rate, any proration, and the calculation. Transparency reduces client disputes.
- **Custodian fee debiting**: If fees are debited directly from the custodian account, you need authorization on file and must transmit billing files in the custodian's required format. Timing matters -- submit the billing file early enough that the debit occurs on your target date.
- **Rounding**: Define a rounding convention (e.g., round to the nearest cent at the final step only). Rounding at intermediate steps can create small discrepancies across accounts.

---

## Recommended Process Flow

1. **T-5 business days before quarter start**: Pull AUM snapshot from custodian(s) as of the last business day of the prior quarter. Reconcile against your portfolio management system.
2. **T-3 business days**: Run billing calculation for all accounts. Flag exceptions: new accounts needing proration, terminated accounts needing refunds, fee schedule overrides, household allocations.
3. **T-2 business days**: Review exceptions. Compliance or operations manager approves the billing run.
4. **T-1 business day**: Generate invoices and/or custodian billing files.
5. **First business day of quarter**: Submit billing files to custodian(s) for fee debiting. Send invoices to direct-billed clients.
6. **T+5 business days**: Reconcile debited fees against expected amounts. Investigate discrepancies (insufficient cash, rejected debits, closed accounts).

This timeline gives you buffers for review and correction before fees are actually collected.
