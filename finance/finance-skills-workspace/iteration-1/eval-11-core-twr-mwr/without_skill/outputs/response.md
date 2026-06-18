# Time-Weighted Return (TWR) vs. Money-Weighted Return (MWR/IRR)

## Setup

- **t=0**: Client invests $100,000
- **t=6 months**: Fund is up 15%, so portfolio value = $115,000. Client adds $50,000. Portfolio value after contribution = $165,000.
- **t=12 months**: Total portfolio value = $178,000

---

## Time-Weighted Return (TWR)

The TWR eliminates the effect of external cash flows by breaking the measurement period into sub-periods at each cash flow event, calculating the return for each sub-period, and then geometrically linking them.

### Sub-period 1 (months 0-6)

- Beginning value: $100,000
- Ending value (before cash flow): $115,000
- Return: R1 = ($115,000 / $100,000) - 1 = **0.15 (15.0%)**

### Sub-period 2 (months 6-12)

- Beginning value (after cash flow): $115,000 + $50,000 = $165,000
- Ending value: $178,000
- Return: R2 = ($178,000 / $165,000) - 1 = **0.07879 (7.88%)**

### Geometric Linking

TWR = (1 + R1) x (1 + R2) - 1

TWR = (1.15) x (1.07879) - 1

TWR = 1.24061 - 1

**TWR = 24.06%**

---

## Money-Weighted Return (MWR / IRR)

The MWR is the internal rate of return (IRR) that equates the present value of all cash flows (in and out) to the ending value. It accounts for the timing and size of cash flows.

We need to find the rate r (annualized) such that:

$100,000 x (1 + r) + $50,000 x (1 + r)^0.5 = $178,000

Here, the first investment compounds for 1 full year, and the second investment (made at the 6-month mark) compounds for half a year.

### Solving by iteration

Let me try r = 0.2206 (22.06%):

- $100,000 x (1.2206) = $122,060
- $50,000 x (1.2206)^0.5 = $50,000 x 1.10481 = $55,241
- Total = $177,301 -- too low

Let me try r = 0.2350:

- $100,000 x (1.2350) = $123,500
- $50,000 x (1.2350)^0.5 = $50,000 x 1.11131 = $55,566
- Total = $179,066 -- too high

Let me try r = 0.2280:

- $100,000 x (1.2280) = $122,800
- $50,000 x (1.2280)^0.5 = $50,000 x 1.10815 = $55,408
- Total = $178,208 -- slightly high

Let me try r = 0.2268:

- $100,000 x (1.2268) = $122,680
- $50,000 x (1.2268)^0.5 = $50,000 x 1.10761 = $55,381
- Total = $178,061 -- very close

Let me try r = 0.2264:

- $100,000 x (1.2264) = $122,640
- $50,000 x (1.2264)^0.5 = $50,000 x 1.10743 = $55,372
- Total = $178,012 -- essentially converged

**MWR (IRR) is approximately 22.6% annualized.**

---

## Why Do They Differ?

The TWR (24.06%) is higher than the MWR (22.6%). The key reasons:

1. **TWR measures the fund's performance; MWR measures the investor's experience.** The TWR reflects what $1 invested at the start would have earned over the full period, regardless of cash flows. The MWR reflects the actual return earned on the investor's capital, weighted by when that capital was deployed.

2. **The timing of the cash flow was unfavorable for the investor.** The fund earned 15% in the first half and only 7.88% in the second half. The client added $50,000 right before the lower-return period. This means more of the investor's capital was exposed to the weaker period, dragging down the MWR relative to the TWR.

3. **General rule:**
   - If an investor adds money before a period of **strong** performance, MWR > TWR (good timing).
   - If an investor adds money before a period of **weak** performance, MWR < TWR (poor timing).
   - In this case, the second period (7.88%) was weaker than the first (15%), so the additional contribution at the midpoint hurt the investor's dollar-weighted return.

### When to Use Each

| Metric | Best Use Case |
|--------|--------------|
| **TWR** | Evaluating fund manager performance, since the manager does not control when clients add or withdraw money |
| **MWR/IRR** | Evaluating the investor's actual experience, since it reflects the impact of their contribution and withdrawal decisions |

The GIPS (Global Investment Performance Standards) require TWR for reporting investment manager performance precisely because it removes the distortion caused by client-directed cash flows.
