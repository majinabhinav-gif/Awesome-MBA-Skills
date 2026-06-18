# TWR vs MWR Analysis: Client Investment Scenario

## Setup

- **t = 0 (start):** Client invests $100,000
- **t = 0.5 (6 months):** Fund is up 15%, so portfolio value = $100,000 x 1.15 = $115,000. Client adds $50,000, bringing the portfolio to $165,000.
- **t = 1.0 (12 months):** Total portfolio value = $178,000

---

## Time-Weighted Return (TWR)

TWR chain-links sub-period returns calculated between each external cash flow, removing the effect of cash flow timing. It measures the fund's investment performance independent of the investor's deposit/withdrawal decisions.

### Sub-period returns

**Sub-period 1 (months 0-6):**

```
R_1 = (V_end - V_begin) / V_begin
R_1 = (115,000 - 100,000) / 100,000
R_1 = +15.00%
```

**Sub-period 2 (months 6-12):**

After the $50,000 contribution, the starting value for this sub-period is $165,000.

```
R_2 = (V_end - V_begin) / V_begin
R_2 = (178,000 - 165,000) / 165,000
R_2 = 13,000 / 165,000
R_2 = +7.88% (approximately)
```

### Chain-linking

```
1 + R_TWR = (1 + R_1) x (1 + R_2)
1 + R_TWR = 1.15 x 1.0788
1 + R_TWR = 1.24061
R_TWR = +24.06% (cumulative over 1 year)
```

Since the total period is exactly one year, the annualized TWR is also **+24.06%**.

---

## Money-Weighted Return (MWR / IRR)

MWR is the internal rate of return that sets the net present value of all cash flows to zero. It reflects the investor's actual experience because it is sensitive to the timing and magnitude of cash flows.

### Cash flows (from the investor's perspective)

| Time (years) | Cash Flow |
|--------------|-----------|
| t = 0.0 | -$100,000 (initial investment) |
| t = 0.5 | -$50,000 (additional contribution) |
| t = 1.0 | +$178,000 (terminal value / withdrawal) |

### IRR equation

Solve for the annual rate r:

```
0 = -100,000 + (-50,000) / (1 + r)^0.5 + 178,000 / (1 + r)^1
```

### Numerical solution (iterative)

**Try r = 0.2406 (24.06%, the TWR):**

```
-100,000 + (-50,000) / (1.2406)^0.5 + 178,000 / 1.2406
= -100,000 + (-50,000) / 1.1139 + 178,000 / 1.2406
= -100,000 - 44,889 + 143,479
= -1,410
```

NPV is negative, so the MWR is slightly lower than the TWR. Try a lower rate.

**Try r = 0.2200 (22.00%):**

```
-100,000 + (-50,000) / (1.22)^0.5 + 178,000 / 1.22
= -100,000 + (-50,000) / 1.10454 + 178,000 / 1.22
= -100,000 - 45,267 + 145,902
= +635
```

**Try r = 0.2300 (23.00%):**

```
-100,000 + (-50,000) / (1.23)^0.5 + 178,000 / 1.23
= -100,000 + (-50,000) / 1.10905 + 178,000 / 1.23
= -100,000 - 45,084 + 144,715
= -369
```

**Interpolating between 22.00% and 23.00%:**

```
r = 22.00% + (23.00% - 22.00%) x 635 / (635 + 369)
r = 22.00% + 1.00% x 0.632
r = approximately 22.63%
```

**Verify r = 0.2263 (22.63%):**

```
-100,000 + (-50,000) / (1.2263)^0.5 + 178,000 / 1.2263
= -100,000 + (-50,000) / 1.10739 + 178,000 / 1.2263
= -100,000 - 45,152 + 145,153
= +1 (essentially zero)
```

The MWR (IRR) is approximately **22.63% annualized**.

---

## Summary of Results

| Metric | Value |
|--------|-------|
| Time-Weighted Return (TWR) | **+24.06%** (annualized) |
| Money-Weighted Return (MWR/IRR) | **+22.63%** (annualized) |
| Difference | TWR exceeds MWR by approximately 1.4 percentage points |

---

## Why TWR and MWR Differ

The TWR (24.06%) exceeds the MWR (22.63%) in this scenario, and the reason comes down to the timing and size of the cash flow relative to the fund's performance in each sub-period.

**The fund earned a higher return in the first half (15.00%) than in the second half (7.88%).** The client added $50,000 at the midpoint -- *after* the stronger performance period and *before* the weaker one.

- **TWR treats both sub-periods equally.** It simply chain-links the 15% and 7.88% returns, giving no weight to how much capital was invested in each period. TWR answers: "How well did the fund perform?"

- **MWR weights each period by the amount of capital at work.** In the first half, $100,000 was invested and earned the higher 15% return. In the second half, $165,000 was invested but earned only the lower 7.88% return. Because more dollars were exposed during the weaker-performing period, the dollar-weighted return (MWR) is pulled down relative to the TWR.

**Key takeaway:** TWR is the appropriate measure for evaluating the fund manager's investment skill, since the manager does not control when clients deposit or withdraw money. MWR is the appropriate measure for evaluating the client's personal investment experience, since it captures the actual dollars earned on the actual dollars invested at each point in time.

If the client had instead added the $50,000 *before* the stronger first half (rather than after it), the MWR would have exceeded the TWR, because more capital would have been at work during the higher-return period.
