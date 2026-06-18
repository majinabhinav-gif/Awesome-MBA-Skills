# Rebalancing an $800K Taxable Portfolio with Tax-Loss Harvesting Coordination

## Should You Rebalance?

**Yes -- your portfolio has triggered a rebalance.**

Your 60/40 target has drifted to 68/32. Applying the threshold test:

- Equity drift: 68% - 60% = **+8%**, which exceeds your +5% band
- Bond drift: 32% - 40% = **-8%**, which exceeds your -5% band

Both asset classes are outside tolerance. Under a threshold-based rebalancing framework, this is a clear trigger.

## Required Trades (Before Tax Coordination)

| Asset Class | Current ($) | Current (%) | Target (%) | Target ($) | Trade |
|---|---|---|---|---|---|
| Equities | $544,000 | 68% | 60% | $480,000 | Sell $64,000 |
| Bonds | $256,000 | 32% | 40% | $320,000 | Buy $64,000 |

You need to sell $64,000 in equities and redirect the proceeds into bonds.

## Coordinating with Tax-Loss Harvesting

You have approximately $15,000 in unrealized losses across certain equity positions. This is a meaningful opportunity, and the rebalancing event is the ideal time to harvest because the TLH sells and rebalance sells can overlap, reducing total transaction count.

### Step 1: Identify TLH Candidates Within the Equity Sell List

Since you need to sell $64,000 in equities anyway, prioritize selling the positions with unrealized losses first. For each losing position:

- Confirm the loss exceeds a materiality threshold (e.g., at least $1,000-$2,000 per position). With $15,000 total, individual losses are likely material.
- Use Specific Identification (HIFO -- Highest In, First Out) to select the highest-cost-basis lots, maximizing the realized loss.
- Rank by tax benefit: short-term losses are more valuable (offset gains at ordinary income rates up to 37%) than long-term losses (offset at 15-20%).

### Step 2: Calculate the Tax Benefit

Assuming a combined federal + state rate of roughly 28.8% for long-term losses (20% federal LTCG + 3.8% NIIT + 5% state) or up to 45.8% for short-term losses (37% + 3.8% + 5%):

| Loss Type | Amount | Rate | Tax Savings |
|---|---|---|---|
| Short-term losses | Varies | ~45.8% | Higher per dollar |
| Long-term losses | Varies | ~28.8% | Lower per dollar |
| **Total $15K harvested (blended example)** | **$15,000** | **~30-40%** | **$4,500 - $6,000** |

The harvested losses can offset any realized capital gains you have this year, with up to $3,000 of net losses deductible against ordinary income. Unused losses carry forward indefinitely.

### Step 3: Select Replacement Securities

For each position you sell at a loss, you must immediately purchase a replacement security to maintain your equity market exposure. The replacement must not be "substantially identical" to avoid the wash-sale rule:

- **ETF swaps:** If you sell a Vanguard Total Stock Market ETF (VTI), replace with a Schwab U.S. Broad Market ETF (SCHB) or an iShares Russell 1000 ETF (IWB). Different index methodology is sufficient.
- **Individual stock swaps:** If selling an individual stock at a loss, replace with a sector ETF or a close peer company.
- **Tracking error budget:** Target a correlation of 0.95+ and tracking error under 2% annualized relative to the original holding.

### Step 4: Construct the Combined Trade List

Structure the trades as follows:

1. **TLH sells (losing equity positions):** Sell all positions with unrealized losses, up to $15,000 in harvested losses. These sells contribute toward your $64,000 equity reduction target.
2. **TLH replacement buys (equities):** Immediately buy similar-but-not-identical equity replacements to maintain exposure during the 30-day wash-sale window.
3. **Remaining rebalance sells:** If the TLH sells total less than $64,000 (likely, since the losses are $15K but the position values are larger), sell additional equity positions to reach the $64,000 target. For these sells, use HIFO lot selection to minimize realized gains.
4. **Bond purchases:** Use the net proceeds (after TLH replacement buys) to purchase bonds, bringing your bond allocation back toward 40%.

**Simplified flow:**

- Sell $X of losing equity positions (harvest $15K in losses)
- Buy $X of replacement equities (maintain exposure, avoid wash sale)
- Sell $64,000 of other equity positions (rebalance, choosing lowest-gain lots via HIFO)
- Buy $64,000 of bonds

Note: If any of your losing positions are also overweight holdings, the TLH sell and the rebalance sell are the same trade -- you sell the position, harvest the loss, and do NOT buy an equity replacement for that portion. This is the most efficient scenario.

### Step 5: Wash-Sale Compliance

Critical rules for the 61-day window (30 days before and after each loss sale):

- **Do not repurchase** the same or substantially identical security in any account -- including IRAs, 401(k)s, HSAs, and spouse's accounts.
- **Suspend DRIP** on the sold securities and any substantially identical funds across all household accounts.
- **Check 401(k) contributions:** If your 401(k) auto-invests in a fund that tracks the same index as a position you harvested, temporarily redirect that allocation for 30 days.
- **IRA wash-sale trap:** A wash sale triggered by a purchase in an IRA results in a permanently lost deduction -- the disallowed loss cannot be added to the IRA's cost basis.

### Step 6: Evaluate the After-Tax Cost of Rebalancing

Before executing, compare:

| Factor | Estimate |
|---|---|
| Tax savings from TLH | $4,500 - $6,000 |
| Tax cost of selling appreciated equity (for the remaining rebalance sells) | Depends on gains in those lots -- use HIFO to minimize |
| Transaction costs (spreads) | Minimal for liquid ETFs (~$30-50 round trip) |
| Net tax impact | Likely net positive due to TLH |

The $15,000 in harvested losses may partially or fully offset any gains realized from the rebalancing sells, making this a tax-efficient rebalance overall.

## Summary of Recommendations

1. **Rebalance now** -- the 8% drift exceeds your 5% threshold and exposes the portfolio to unintended equity risk.
2. **Harvest the $15K in losses first** -- sell the losing equity positions, immediately purchase replacement securities to maintain exposure, and use specific lot identification (HIFO) to maximize realized losses.
3. **Then execute remaining rebalance trades** -- sell additional equities (choosing highest-basis lots) and buy bonds to reach your 60/40 target.
4. **Track wash-sale windows** -- maintain a calendar of the 61-day windows for each harvested security and ensure no substantially identical purchases occur in any household account.
5. **Document the before/after allocation** -- record current allocation (68/32), post-rebalance allocation (target 60/40), trades executed, estimated tax impact, and rationale for the combined rebalance-plus-TLH event.
6. **After 31 days**, you may swap replacement securities back to your original holdings if preferred, but evaluate whether the replacement has a gain that would create a new tax liability.

## Important Caveats

- This analysis assumes all positions are in a single taxable account. If you also have tax-deferred accounts (IRA, 401(k)), consider executing appreciated equity sells there instead (no tax impact) and reserving taxable-account sells for the loss-harvesting positions.
- TLH creates a lower cost basis in replacement securities -- the tax is deferred, not eliminated. However, the time value of the deferral and the ability to offset current gains makes it worthwhile.
- Consult your tax advisor regarding your specific marginal rates and any state-specific rules before executing.
