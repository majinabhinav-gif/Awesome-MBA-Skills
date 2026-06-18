# Quarterly Fee Billing: Structure and Edge Cases

## Billing Calculation Structure

### 1. Determine the Billing AUM

Use the portfolio market value as of the last business day of the prior quarter. This is your billing basis. For example, billing for Q2 (April-June) uses the valuation as of the last business day of March.

Decide whether you are using a tiered (marginal) or breakpoint (flat) fee schedule, as this significantly affects the calculation:

- **Tiered/marginal**: Each tranche of AUM is billed at the rate for that tier (e.g., first $1M at 1.00%, next $4M at 0.75%, above $5M at 0.50%). The effective rate blends downward as AUM grows.
- **Breakpoint/flat**: The entire balance is billed at the rate corresponding to the highest tier reached.

### 2. Calculate the Quarterly Fee

```
Annual Fee = sum of (each tier amount * tier rate)   [tiered]
           OR
Annual Fee = total AUM * applicable rate             [breakpoint]

Quarterly Fee = Annual Fee / 4
```

Billing in advance means the client pays at the start of the quarter for the upcoming quarter's advisory services.

### 3. Prorate New Accounts

For accounts funded mid-quarter, calculate the fee based on the number of calendar days from the funding date through the end of the quarter, relative to total calendar days in the quarter:

```
Proration Factor = days_remaining_in_quarter / total_days_in_quarter
Prorated Fee = Quarterly Fee * Proration Factor
```

Use the account's funded value (AUM at funding date) as the billing basis since there is no prior quarter-end valuation.

### 4. Calculate Termination Refunds

When a client terminates mid-quarter, refund the unused portion:

```
Days Used = termination_date - quarter_start_date
Days in Quarter = quarter_end_date - quarter_start_date
Unused Fraction = 1 - (Days Used / Days in Quarter)
Refund = Quarterly Fee * Unused Fraction
```

---

## Edge Cases to Handle

### Account and Timing Issues

- **Account funded on the last day of the quarter**: The proration factor is effectively 0 for the current quarter. Either bill nothing and start billing next quarter, or bill for 1 day. Define a policy and document it in the advisory agreement.

- **Account funded and terminated in the same quarter**: Calculate the prorated fee from funding date to termination date. The client should only pay for the days they received service.

- **Termination on the first day of a quarter**: The full advance fee was just billed. Nearly the entire amount should be refunded. Clarify whether day 1 counts as a service day or not.

- **Multiple accounts per household**: If the fee schedule applies at the household (relationship) level, aggregate AUM across all accounts before applying tier breakpoints, then allocate the fee back to individual accounts proportionally.

### Valuation Issues

- **Stale or missing valuations**: Some assets (alternatives, private placements, real estate) may not have a current market price on the billing date. Define a policy for using the most recent available valuation, and document the staleness threshold.

- **Pending trades on the valuation date**: Trades executed on the last business day may not have settled. Decide whether billing AUM reflects trade-date or settlement-date positions.

- **Cash in transit**: Large deposits or withdrawals near quarter-end may or may not be reflected. Define a cutoff policy.

- **Non-billable assets**: Some advisory agreements exclude certain holdings (e.g., legacy positions, 529 plans, held-away assets). Your billing system needs to flag and exclude these.

### Fee Schedule Complications

- **Fee schedule changes mid-quarter**: If the advisory agreement is amended mid-quarter (e.g., a fee reduction), you may need to split the quarter into two billing periods with different rates.

- **Fee caps and minimums**: Some agreements specify a minimum quarterly fee or a maximum annual fee. Apply these after the standard calculation.

- **Family/household aggregation with different fee schedules**: When household members have different agreements or legacy fee schedules, aggregation logic becomes complex. Decide whether to use the primary account's schedule or a blended approach.

- **Performance-based fee adjustments**: If any accounts have performance fee overlays, those are typically calculated separately and often in arrears, not in advance.

### Operational Edge Cases

- **Account transfers (ACAT) mid-quarter**: An incoming transfer is similar to a new account (prorate from receipt date). An outgoing transfer may trigger a termination refund.

- **Account re-registration**: If an account changes registration (e.g., individual to trust) but the advisory relationship continues, this should generally not trigger a new-account proration or termination refund.

- **Billing account vs. managed accounts**: When fees are debited from a specific billing account but calculated across multiple managed accounts, ensure the debit account has sufficient cash. If not, you need a process to raise cash or split the debit.

- **Negative market values**: Accounts with margin loans could theoretically have negative equity. Define whether billable AUM floors at zero.

- **Quarter-end falling on a weekend/holiday**: The "last business day" determination must account for market holidays, not just weekends. Use an authoritative holiday calendar (NYSE calendar for US equities).

### Compliance and Documentation

- **ADV Part 2A consistency**: The billing methodology must match what is disclosed in the firm's Form ADV Part 2A brochure. Any deviation is a compliance risk.

- **Client authorization for fee debit**: Ensure standing authorization exists for direct fee debits from custodial accounts. Some custodians require specific forms.

- **Fee invoices**: Even when fees are auto-debited, provide itemized invoices showing the calculation: beginning AUM, fee rate, billing period, any proration, and the resulting fee amount. This is both a best practice and a regulatory expectation.

- **Audit trail**: Retain the billing inputs (valuation date, AUM snapshot, fee schedule version, proration factors) for each billing cycle. Regulators and auditors will want to reconstruct any fee.

---

## Recommended Process Flow

1. **T-1 (day before billing)**: Pull and lock quarter-end valuations for all accounts. Reconcile against custodian statements.
2. **Billing run**: For each account, determine the applicable fee schedule, calculate the fee (with proration for new accounts), and generate an invoice.
3. **Review**: A second person reviews the billing output, checking for outliers (unusually high/low fees, large AUM changes, new accounts, terminations).
4. **Debit submission**: Submit fee debit instructions to the custodian(s).
5. **Termination refunds**: Process any mid-quarter termination refunds identified since the last billing run.
6. **Reconciliation**: After debits settle, reconcile actual debits against expected fees. Investigate discrepancies (insufficient funds, rejected debits, account closures).
7. **Archive**: Store the complete billing record (inputs, calculations, invoices, debit confirmations) for the retention period required by your compliance program.
