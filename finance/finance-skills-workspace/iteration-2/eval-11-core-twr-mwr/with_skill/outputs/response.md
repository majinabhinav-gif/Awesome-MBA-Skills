# TWR vs MWR Analysis: Client Investment Scenario

## Setup

- **t = 0 (start):** Client invests $100,000
- **t = 0.5 (6 months):** Fund is up 15%, so portfolio value = $100,000 x 1.15 = **$115,000**. Client adds $50,000, bringing the portfolio to $165,000.
- **t = 1.0 (12 months):** Total portfolio value = **$178,000**

---

## Time-Weighted Return (TWR)

TWR chain-links sub-period returns calculated between each external cash flow, removing the effect of cash flow timing. It measures the fund's investment performance independent of the client's deposit decisions.

### Sub-Period Returns

**Sub-period 1 (months 0-6):**

```
R_1 = (V_end - V_begin) / V_begin
R_1 = (115,000 - 100,000) / 100,000
R_1 = +15.00%
```

**Sub-period 2 (months 6-12):**

The beginning value for this sub-period is the portfolio value after the cash flow: $115,000 + $50,000 = $165,000.

```
R_2 = (V_end - V_begin) / V_begin
R_2 = (178,000 - 165,000) / 165,000
R_2 = 13,000 / 165,000
R_2 = +7.88%
```

### Chain-Linking

```
1 + R_TWR = (1 + R_1) x (1 + R_2)
1 + R_TWR = 1.15 x 1.0788
1 + R_TWR = 1.24061
R_TWR = +24.06% (cumulative over 1 year)
```

Since the measurement period is exactly one year, the **annualized TWR is 24.06%**.

---

## Money-Weighted Return (MWR / IRR)

MWR is the internal rate of return that sets the NPV of all cash flows to zero. It reflects the client's actual dollar-weighted experience because it accounts for how much capital was deployed and when.

### Cash Flow Schedule

From the client's perspective (outflows are negative, terminal value is positive):

| Time (years) | Cash Flow |
|---|---|
| t = 0.0 | -$100,000 |
| t = 0.5 | -$50,000 |
| t = 1.0 | +$178,000 |

### IRR Equation

Solve for the annual rate r:

```
0 = -100,000 + (-50,000) / (1 + r)^0.5 + 178,000 / (1 + r)^1.0
```

### Numerical Solution

**Test r = 0.2200 (22.00%):**

```
(1 + 0.22)^0.5 = 1.1045
(1 + 0.22)^1.0 = 1.22

NPV = -100,000 + (-50,000 / 1.1045) + (178,000 / 1.22)
NPV = -100,000 - 45,270.26 + 145,901.64
NPV = +631.38
```

Slightly positive, so the rate is slightly above 22%.

**Test r = 0.2240 (22.40%):**

```
(1 + 0.224)^0.5 = 1.1063
(1 + 0.224)^1.0 = 1.224

NPV = -100,000 + (-50,000 / 1.1063) + (178,000 / 1.224)
NPV = -100,000 - 45,194.07 + 145,424.84
NPV = +230.77
```

**Test r = 0.2280 (22.80%):**

```
(1 + 0.228)^0.5 = 1.1081
(1 + 0.228)^1.0 = 1.228

NPV = -100,000 + (-50,000 / 1.1081) + (178,000 / 1.228)
NPV = -100,000 - 45,118.67 + 144,951.14
NPV = -167.53
```

By interpolation between 22.40% and 22.80%, the IRR is approximately **22.63%**.

More precisely, interpolating linearly:

```
r = 0.2240 + (230.77 / (230.77 + 167.53)) x (0.2280 - 0.2240)
r = 0.2240 + (0.5794) x (0.0040)
r = 0.2240 + 0.0023
r = 0.2263 = 22.63%
```

The **annualized MWR (IRR) is approximately 22.63%**.

---

## Comparison

| Metric | Value |
|---|---|
| Time-Weighted Return (TWR) | 24.06% |
| Money-Weighted Return (MWR/IRR) | 22.63% |

---

## Why They Differ

The TWR and MWR differ because the client added $50,000 *after* the strong first half (+15%) and *before* the weaker second half (+7.88%). The key dynamics:

1. **TWR treats each sub-period equally.** It chain-links the 15% and the 7.88% returns without regard to how much capital was invested in each period. TWR reflects the fund manager's pure investment skill.

2. **MWR weights periods by capital deployed.** In the second half, the client had $165,000 at work (vs. $100,000 in the first half), but the second half return was only 7.88% compared to 15% in the first half. Because more dollars were exposed during the lower-returning period, the MWR is pulled below the TWR.

3. **General principle:** When additional capital is contributed before periods of *below-average* returns (relative to other sub-periods), MWR will be lower than TWR. Conversely, if the client had added capital before the stronger period, MWR would have exceeded TWR.

In this case the difference is modest (about 1.4 percentage points) because both sub-periods were positive. The divergence would be far more dramatic if one period had been negative -- as illustrated in the classic example where a large deposit before a losing period can produce a negative MWR even when TWR is positive.

**Bottom line:** Use TWR to evaluate the fund manager's performance. Use MWR to understand the client's actual investment experience given their specific cash flow timing.
