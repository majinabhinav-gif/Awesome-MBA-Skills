# Assessing Risk-Adjusted Returns: Your Fund's 12% / 18% / -32% Profile

## Quick Assessment of the Raw Numbers

Your fund returned 12% annualized with 18% standard deviation and a -32% max drawdown during COVID. Let me walk through how to evaluate whether the risk-adjusted returns are actually good, and which metrics to use for benchmark comparison.

## Step 1: Sharpe Ratio -- Return per Unit of Total Risk

The Sharpe ratio is the starting point for any risk-adjusted assessment.

```
SR = (R_p - R_f) / sigma_p
```

Assuming a risk-free rate of around 4% (using a representative 5-year average):

```
SR = (0.12 - 0.04) / 0.18
   = 0.08 / 0.18
   = 0.44
```

A Sharpe of 0.44 falls below the "acceptable" threshold of 0.5. This tells you the fund is generating less than half a unit of excess return per unit of total risk. For context: below 0.5 is considered poor, 0.5-1.0 is acceptable, above 1.0 is strong. On Sharpe alone, this fund is underwhelming.

However, Sharpe penalizes upside and downside volatility equally. If the fund's returns are positively skewed (lots of the 18% vol comes from upside moves), Sharpe understates the quality of the returns. That is where the next metrics come in.

## Step 2: Sortino Ratio -- Isolating Downside Risk

The Sortino ratio replaces total volatility with downside deviation, penalizing only returns below a Minimum Acceptable Return (MAR):

```
Sortino = (R_p - R_f) / sigma_downside
```

You would need the actual return series to compute downside deviation, but here is the key insight: if the fund's downside deviation is meaningfully lower than its 18% total volatility, the Sortino ratio will be substantially higher than the Sharpe. For example, if downside deviation were 12%:

```
Sortino = 0.08 / 0.12 = 0.67
```

A divergence where Sortino significantly exceeds Sharpe suggests the fund's volatility is skewed to the upside -- the "good" kind of volatility -- which is a favorable characteristic that the Sharpe ratio misses.

**Action item:** Request the fund's downside deviation or monthly return series and compute the Sortino directly.

## Step 3: Calmar Ratio -- Return vs. Worst Drawdown

The Calmar ratio directly addresses the -32% max drawdown:

```
Calmar = CAGR / |MaxDrawdown|
       = 0.12 / 0.32
       = 0.375
```

A Calmar below 1.0 means the fund's annualized return does not compensate for the worst peak-to-trough loss. At 0.375, the fund would need roughly 2.7 years of its average return just to recover from the worst drawdown. This is a mediocre result. A Calmar above 1.0 is typically the bar for drawdown-sensitive investors.

That said, COVID was an extraordinary event. Consider two things:

1. **Drawdown duration and recovery time.** If the fund recovered quickly from the -32% trough (say within 6-9 months), the drawdown is less damaging than it appears. A long recovery period (12+ months) makes it worse.
2. **Compare the benchmark's drawdown over the same period.** If the S&P 500 drew down -34% peak-to-trough during COVID, then the fund's -32% is actually slightly better than the market.

## Step 4: Benchmark-Relative Metrics

To compare against a benchmark, you need three additional metrics:

### Information Ratio (Active Return per Unit of Active Risk)

```
IR = (R_p - R_b) / TE
```

where TE (tracking error) = standard deviation of (portfolio return - benchmark return), annualized.

If your benchmark returned 10% with tracking error of 5%:

```
IR = (0.12 - 0.10) / 0.05 = 0.40
```

An IR above 0.5 is considered good; above 1.0 is exceptional. The IR tells you whether the manager is generating consistent alpha or just taking on uncompensated active risk.

### Upside/Downside Capture Ratios

These measure how the fund participates in benchmark up-months and down-months:

- **Up Capture > 100%**: The fund captures more than the benchmark's gains in rising markets.
- **Down Capture < 100%**: The fund loses less than the benchmark in falling markets.
- **Capture Ratio (Up/Down) > 1**: Asymmetric participation favoring the investor.

A fund with, say, 105% up capture and 90% down capture has a capture ratio of 1.17, which is an attractive asymmetric profile.

### M-Squared (Modigliani-Modigliani)

This converts risk-adjusted performance into the same units as return, making it directly comparable to the benchmark return:

```
M^2 = R_f + SR_p * sigma_b
```

If the benchmark volatility is 15%:

```
M^2 = 0.04 + 0.44 * 0.15
    = 0.04 + 0.066
    = 0.106 = 10.6%
```

Interpretation: if your fund were scaled to match the benchmark's 15% volatility, it would have returned 10.6%. If the benchmark returned 10%, the fund is slightly better on a risk-adjusted basis. If the benchmark returned 12%, the fund is actually worse once you account for the higher volatility it took.

## Summary: The Metrics You Need

| Metric | What It Tells You | Your Fund's Estimate | Verdict |
|--------|-------------------|---------------------|---------|
| Sharpe Ratio | Return per unit of total risk | 0.44 | Below acceptable (0.5) |
| Sortino Ratio | Return per unit of downside risk | Need return series | Check if meaningfully higher than Sharpe |
| Calmar Ratio | Return per unit of max drawdown | 0.375 | Weak; drawdown not well compensated |
| Information Ratio | Active return per unit of tracking error | Need benchmark data | Above 0.5 = good |
| Up/Down Capture | Asymmetric market participation | Need monthly data | Capture ratio > 1 is favorable |
| M-Squared | Risk-adjusted return in return units | ~10.6% (est.) | Compare directly to benchmark return |

## Bottom Line

Based on what you have provided, the fund's risk-adjusted returns are mediocre, not poor but not strong. The Sharpe ratio of 0.44 and the Calmar ratio of 0.375 both fall below standard quality thresholds. The 12% return sounds attractive in isolation, but 18% volatility and a -32% drawdown are a high price to pay for it.

Before making a final judgment, you need:

1. The **actual monthly return series** to compute Sortino and capture ratios (the Sharpe alone does not tell the full story if returns are skewed).
2. The **benchmark's return, volatility, and max drawdown** over the same 5-year period. The fund may look better or worse depending on how the benchmark performed through COVID.
3. The **drawdown recovery time**. A fast recovery from the -32% trough significantly changes the practical impact of that drawdown.

The single most informative comparison metric is M-squared, because it converts the fund's risk-adjusted performance into the same units as the benchmark return, eliminating the "apples to oranges" problem of comparing a high-vol fund to a low-vol benchmark.
