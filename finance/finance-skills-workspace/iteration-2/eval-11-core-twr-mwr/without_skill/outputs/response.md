# Time-Weighted Return (TWR) vs. Money-Weighted Return (MWR/IRR)

## Setup

- **t=0:** Invest $100,000
- **t=6 months:** Fund is up 15%, so value = $115,000. Client adds $50,000, bringing the total to $165,000.
- **t=12 months:** Total value = $178,000.

---

## Time-Weighted Return (TWR)

TWR measures the fund's performance independent of cash flows by compounding sub-period returns.

**Sub-period 1 (months 0-6):**

- Beginning value: $100,000
- Ending value (before cash flow): $115,000
- Return: (115,000 - 100,000) / 100,000 = **+15.00%**

**Sub-period 2 (months 6-12):**

- Beginning value (after cash flow): $115,000 + $50,000 = $165,000
- Ending value: $178,000
- Return: (178,000 - 165,000) / 165,000 = **+7.88%**

**TWR (compounded):**

TWR = (1 + 0.15) x (1 + 0.0788) - 1
TWR = 1.15 x 1.0788 - 1
TWR = 1.24061 - 1
**TWR = 24.06%**

This is the annualized-equivalent one-year return since the two sub-periods conveniently sum to exactly one year.

---

## Money-Weighted Return (MWR / IRR)

MWR is the internal rate of return that equates the present value of all cash flows to the final value. We solve for the annual rate r in:

- -100,000 at t=0
- -50,000 at t=0.5 years
- +178,000 at t=1.0 year

The IRR equation (using annual compounding):

100,000 x (1 + r) + 50,000 x (1 + r)^0.5 = 178,000

**Solving by iteration:**

Try r = 0.24 (24%):
- 100,000 x 1.24 = 124,000
- 50,000 x (1.24)^0.5 = 50,000 x 1.1136 = 55,678
- Total = 179,678 (too high)

Try r = 0.22 (22%):
- 100,000 x 1.22 = 122,000
- 50,000 x (1.22)^0.5 = 50,000 x 1.1045 = 55,227
- Total = 177,227 (too low)

Try r = 0.226 (22.6%):
- 100,000 x 1.226 = 122,600
- 50,000 x (1.226)^0.5 = 50,000 x 1.1073 = 55,363
- Total = 177,963 (very close)

Try r = 0.2265:
- 100,000 x 1.2265 = 122,650
- 50,000 x (1.2265)^0.5 = 50,000 x 1.1075 = 55,375
- Total = 178,025 (essentially spot on)

**MWR (IRR) is approximately 22.6% - 22.7%**

---

## Why They Differ

The TWR is **24.06%** while the MWR is approximately **22.6%**. The MWR is lower, and the reason comes down to the timing of the cash flow relative to performance:

1. **TWR ignores cash flow timing.** It treats each sub-period equally by geometrically linking returns. It answers: "How did the fund itself perform?"

2. **MWR is sensitive to cash flow timing.** It weights periods by the amount of money invested. It answers: "How did the investor's actual dollars perform?"

3. **In this case, the client added $50,000 right before the weaker period** (7.88% in the second half vs. 15% in the first half). The larger dollar amount ($165,000) was exposed to the lower-return period, while the smaller amount ($100,000) benefited from the higher-return period. This cash-flow weighting drags the MWR below the TWR.

**General rule:** When an investor adds money before a period of relatively lower returns (or withdraws before a period of higher returns), the MWR will be lower than the TWR. The reverse is also true -- adding money before strong periods makes the MWR exceed the TWR.

This is why TWR is the industry standard (per GIPS) for evaluating fund manager performance, since managers typically do not control the timing of client deposits and withdrawals. MWR, on the other hand, better reflects the actual investor experience.
