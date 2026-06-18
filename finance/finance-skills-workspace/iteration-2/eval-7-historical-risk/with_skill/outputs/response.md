# Assessing Risk-Adjusted Returns: A Framework for Your Fund

## Starting Point: What You Have

- Annualized return: 12%
- Annualized standard deviation: 18%
- Maximum drawdown: -32% (during COVID, roughly Feb-Mar 2020)

These are useful starting figures, but each one tells only part of the story. Here is how to turn them into a proper risk-adjusted assessment and benchmark comparison.

---

## Step 1: Compute Risk-Adjusted Ratios

### Sharpe Ratio

The Sharpe ratio divides excess return over the risk-free rate by total volatility:

```
Sharpe = (R_p - R_f) / sigma_p
```

Assuming a risk-free rate of roughly 2% (a reasonable average over the last 5 years):

```
Sharpe = (12% - 2%) / 18% = 0.556
```

**Interpretation:** A Sharpe ratio of ~0.56 is moderate. As a rule of thumb, below 0.5 is mediocre, 0.5-1.0 is acceptable, and above 1.0 is strong. Your fund sits in the acceptable range, but it is not exceptional on a pure volatility-adjusted basis.

### Sortino Ratio (Uses Downside Deviation, Not Total Volatility)

Standard deviation penalizes both upside and downside moves equally. The Sortino ratio isolates downside risk by using downside deviation as the denominator:

```
Sortino = (R_p - MAR) / sigma_downside
```

where downside deviation is:

```
sigma_d = sqrt( (1/n) * sum( min(R_i - MAR, 0)^2 ) )
```

You would need the actual return series to compute this, but the key insight is: if the fund's return distribution is positively skewed (more upside than downside), the Sortino ratio will be higher than the Sharpe, indicating the volatility figure overstates the true downside risk. If negatively skewed (which the -32% drawdown hints at), the Sortino could be lower than Sharpe, which is a warning sign.

### Calmar Ratio (Return / Max Drawdown)

```
Calmar = Annualized Return / |Max Drawdown|
       = 12% / 32%
       = 0.375
```

**Interpretation:** A Calmar of 0.375 means you earned 37.5 cents of return for every dollar of worst-case peak-to-trough loss. Calmar ratios above 1.0 are strong; below 0.5 suggests the tail risk may not be adequately compensated. Your fund is on the weaker side here. That -32% drawdown is a substantial event relative to the 12% annual return -- it would take nearly 3 years of returns to recover from the worst decline.

---

## Step 2: Benchmark Comparison Metrics

To determine whether the fund is "actually good," you must compare it to an appropriate benchmark (e.g., S&P 500 for a US large-cap equity fund, MSCI ACWI for global equity).

### Excess Return

```
Excess Return = R_fund - R_benchmark
```

If the benchmark also returned 12% annualized with lower volatility, your fund is not adding value. If the benchmark returned 10% with 20% volatility, your fund looks much better.

### Tracking Error

Tracking error measures how consistently the fund deviates from the benchmark:

```
TE = std(R_fund - R_benchmark) * sqrt(N)
```

where N is the annualization factor (12 for monthly data, 252 for daily). A low tracking error (2-4%) means the fund closely follows the benchmark. A high tracking error (8%+) means it takes very different bets.

### Information Ratio

The information ratio measures excess return per unit of tracking error:

```
IR = (R_fund - R_benchmark) / TE
```

An IR above 0.5 is good; above 1.0 is exceptional. This tells you whether the fund's active bets (the deviations from the benchmark) are paying off.

### Relative Drawdown

Compare the fund's -32% max drawdown to the benchmark's max drawdown over the same period. During COVID, the S&P 500 dropped roughly 34%. If your fund dropped 32% versus a benchmark drop of 34%, that is essentially benchmark-like behavior -- the drawdown is not evidence of poor risk management, just market exposure. If the benchmark only dropped 20%, then the fund took on meaningfully more tail risk.

---

## Step 3: Deeper Risk Diagnostics

### Historical VaR

Compute the 5th percentile of the fund's monthly (or daily) return distribution:

```
VaR_95% = -Percentile(returns, 5)
```

This gives a non-parametric estimate of the loss you should expect to exceed only 5% of the time. Compare this to the benchmark's VaR over the same period.

### Drawdown Duration and Recovery Time

The -32% drawdown tells you the depth of the worst decline, but equally important is:

- **How long did it take to hit the trough?** (drawdown duration)
- **How long to recover to the prior peak?** (recovery time)

A fund that drew down 32% but recovered in 4 months is very different from one that took 2 years to recover. Fast recovery indicates resilience; slow recovery compounds the pain through opportunity cost.

### Volatility Regime Sensitivity

An 18% annualized volatility is a single-number summary of 5 years. Consider whether that volatility was stable or concentrated in crisis periods. If 80% of the volatility came from the COVID crash and the fund was calm otherwise, the 18% figure understates the fund's typical risk profile but may understate tail risk as well. Examining rolling volatility (e.g., trailing 3-month or 6-month windows) gives a more nuanced picture.

---

## Step 4: Putting It All Together

| Metric | Your Fund | What to Compare Against |
|--------|-----------|------------------------|
| Annualized Return | 12% | Benchmark return over same period |
| Annualized Volatility | 18% | Benchmark volatility |
| Sharpe Ratio | ~0.56 | Benchmark Sharpe |
| Calmar Ratio | 0.375 | Benchmark Calmar |
| Max Drawdown | -32% | Benchmark max drawdown |
| Sortino Ratio | Needs return series | Benchmark Sortino |
| Tracking Error | Needs return series | Lower = closer to index |
| Information Ratio | Needs return series | > 0.5 is good |
| Historical VaR (95%) | Needs return series | Benchmark VaR |

**The bottom line:** A 12% return with 18% volatility and a -32% drawdown is not inherently good or bad -- it depends entirely on what the benchmark delivered over the same window. If you are paying active management fees for performance that matches a passive index on both return and risk, the fund is not earning its keep. The metrics above give you the tools to make that judgment precisely.

---

## Key Pitfalls to Avoid

- **Do not annualize volatility incorrectly.** Volatility scales with the square root of time. Multiply daily standard deviation by sqrt(252), not by 252.
- **Lookback period matters.** Five years captures COVID but may miss other regime types. Always state the evaluation window.
- **Survivorship bias.** If you are comparing against peer funds, ensure the dataset includes funds that closed during the period, not just survivors.
- **Log returns for volatility, simple returns for performance.** Use log returns (r = ln(P_t / P_{t-1})) when computing volatility estimates, as they are additive across time. Use simple returns for reporting cumulative performance.
