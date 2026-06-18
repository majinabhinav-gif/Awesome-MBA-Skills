# Rebalancing and Tax-Loss Harvesting Coordination

## Should You Rebalance?

Yes. Your portfolio has triggered the rebalancing threshold and you should act.

**Drift analysis:**

| Asset Class | Target | Current | Drift | Threshold | Triggered? |
|-------------|--------|---------|-------|-----------|------------|
| Stocks      | 60%    | 68%     | +8%   | +/- 5%    | Yes        |
| Bonds       | 40%    | 32%     | -8%   | +/- 5%    | Yes        |

Both asset classes have drifted beyond your +/- 5% tolerance band. The equity overweight exposes you to more risk than your target allocation intended.

**Required trades:**

- Equity target: 60% x $800,000 = $480,000 (currently $544,000)
- Bond target: 40% x $800,000 = $320,000 (currently $256,000)
- Sell equities: $544,000 - $480,000 = **$64,000**
- Buy bonds: $320,000 - $256,000 = **$64,000**

## How to Coordinate with Tax-Loss Harvesting

You have a valuable opportunity here because both actions -- rebalancing and harvesting -- require selling equity positions. Coordinating them reduces total trade count and maximizes after-tax benefit. Here is the step-by-step approach:

### Step 1: Identify TLH Candidates Within the Equity Sell List

You need to sell $64,000 in equities to rebalance. Start by identifying which of your equity positions contain the $15,000 in unrealized losses. These positions should be sold first because:

- The rebalance and the harvest are the same trade -- one transaction accomplishes both goals.
- You realize losses that generate a direct tax benefit.
- You avoid selling appreciated positions (which would generate taxable gains) for as much of the $64,000 as possible.

### Step 2: Quantify the Tax Benefit

Assuming a combined federal long-term capital gains rate of 15-20% plus state taxes (and potentially 3.8% NIIT if your MAGI exceeds $250,000 MFJ / $200,000 single):

| Scenario | Rate | Tax Savings on $15K Loss |
|----------|------|--------------------------|
| 15% LTCG only | 15% | $2,250 |
| 20% LTCG + 3.8% NIIT | 23.8% | $3,570 |
| 20% LTCG + 3.8% NIIT + 5% state | 28.8% | $4,320 |

If these are short-term losses (held one year or less), the benefit is even larger since they offset gains taxed at ordinary income rates (up to 37% federal).

Even without other realized gains to offset this year, up to $3,000 of net capital losses can offset ordinary income, with the remaining $12,000 carrying forward indefinitely to offset future gains.

### Step 3: Select Lots and Replacement Securities

**Lot selection:** Use Specific Identification with HIFO (Highest In, First Out) to sell the highest-cost-basis lots first. This maximizes the realized loss per dollar sold.

**Replacement securities:** To maintain equity exposure during the 30-day wash-sale window, immediately purchase a similar but not substantially identical replacement. Examples:

- If selling an S&P 500 ETF (e.g., VOO), replace with a total market ETF (e.g., ITOT) or a Russell 1000 ETF
- If selling individual stocks, replace with a sector ETF covering the same industry
- Aim for 0.95+ correlation and under 2% annualized tracking error between original and replacement

### Step 4: Execute the Trades

Structure the $64,000 equity sell in this priority order:

1. **First: Sell losing positions (~$15,000 in market value with embedded losses).** These accomplish rebalancing AND harvest losses. Buy replacement securities immediately.
2. **Second: Sell positions at or near cost basis.** These generate minimal tax impact.
3. **Last resort: Sell appreciated positions.** Use HIFO lot selection. Prefer lots held over one year (long-term capital gains rate). Sell only enough to reach the $64,000 target.

Use the full $64,000 in sale proceeds to purchase bonds, completing the rebalance.

### Step 5: Wash-Sale Compliance

This is critical. After selling positions to harvest losses:

- Do NOT repurchase the same or substantially identical securities within 30 days before or after the sale (61-day total window).
- Check ALL accounts: taxable brokerage, IRA, Roth IRA, 401(k), HSA, and any spouse accounts.
- Suspend DRIP (automatic dividend reinvestment) on the sold securities across all accounts during the window.
- If your 401(k) holds a fund tracking the same index as a harvested position, temporarily redirect that allocation to a different fund during the wash-sale window.
- After 31 days, you may swap back to the original securities if desired (evaluate whether the replacement has gained, which would trigger a taxable event on the swap-back).

### Step 6: Before/After Summary

Prepare a comparison for your records:

| Metric | Before | After |
|--------|--------|-------|
| Stock allocation | 68% ($544K) | 60% ($480K) |
| Bond allocation | 32% ($256K) | 40% ($320K) |
| Realized losses | $0 | Up to $15,000 |
| Estimated tax savings | $0 | $2,250 - $4,320 (rate dependent) |
| Trades executed | -- | Sell equity (2-3 lots), buy replacement equity, buy bonds |

## Key Considerations

- **Do not over-harvest.** Harvesting losses reduces cost basis on replacement securities, meaning you will owe more tax when those replacements are eventually sold. The benefit is the time value of deferring that tax liability plus the ability to control when gains are realized.
- **If you have upcoming cash flows** (contributions, dividends, distributions), you can direct those toward bonds to partially close the remaining drift, reducing the amount you need to sell.
- **If you also have tax-deferred accounts** (IRA, 401k), consider whether some of the rebalancing can happen there instead. Selling appreciated equities in an IRA has zero tax consequence, which further reduces the taxable account's gain exposure.
- **Document the rebalance** with date, trigger reason (threshold breach), trades executed, and resulting allocation for compliance and future reference.

## Bottom Line

Rebalance now -- the 8% drift exceeds your 5% threshold. Prioritize selling the equity positions with $15,000 in unrealized losses first, which serves double duty as both a rebalancing trade and a tax-loss harvest. Replace harvested positions with similar-but-not-identical securities to maintain exposure. Use the proceeds to buy bonds. The combined approach reduces your trade count, restores your target allocation, and generates $2,250-$4,320 in tax savings depending on your marginal rate.
