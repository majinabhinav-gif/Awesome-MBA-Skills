# Assessing Risk-Adjusted Returns: A Framework

## Your Fund's Profile

- Annualized return: 12%
- Annualized standard deviation: 18%
- Maximum drawdown: -32% (COVID period)

These numbers alone tell you very little. Risk-adjusted analysis requires context -- a benchmark, a risk-free rate, and several complementary metrics.

## Key Metrics to Calculate

### 1. Sharpe Ratio

The Sharpe ratio measures excess return per unit of total risk:

    Sharpe = (R_p - R_f) / sigma_p

Assuming a risk-free rate of roughly 2% over the period:

    Sharpe = (12% - 2%) / 18% = 0.56

**Interpretation:** A Sharpe ratio of 0.56 is decent but not exceptional. General rules of thumb:
- Below 0.5: mediocre
- 0.5 to 1.0: acceptable
- Above 1.0: strong
- Above 1.5: exceptional (and worth scrutinizing for sustainability)

The Sharpe ratio uses standard deviation, which treats upside and downside volatility equally. If the fund's returns are skewed, this can be misleading.

### 2. Sortino Ratio

The Sortino ratio replaces total volatility with downside deviation, penalizing only harmful volatility:

    Sortino = (R_p - R_f) / downside_deviation

You need the actual return series to compute downside deviation (standard deviation of returns below a target, typically the risk-free rate). If the fund's upside volatility is large relative to its downside, the Sortino ratio will be meaningfully higher than the Sharpe, which is a good sign.

### 3. Maximum Drawdown and Calmar Ratio

The -32% max drawdown is a concrete measure of the worst pain an investor experienced. The Calmar ratio contextualizes this:

    Calmar = annualized_return / |max_drawdown|
    Calmar = 12% / 32% = 0.375

**Interpretation:** A Calmar ratio below 0.5 suggests the fund took significant peak-to-trough risk relative to its return. Recovery time matters too -- how many months did it take to recover from the -32% trough? A fast recovery (say, under 12 months) is less concerning than a slow one.

### 4. Information Ratio (Benchmark-Relative)

The information ratio measures active return per unit of tracking error:

    IR = (R_p - R_b) / tracking_error

Where tracking error is the standard deviation of the difference between fund and benchmark returns. This is the single most important metric for comparing against the benchmark, because it tells you whether the fund's deviations from the benchmark are consistently rewarded.

- IR above 0.5: good active management
- IR above 1.0: exceptional (rare over sustained periods)

### 5. Alpha and Beta (CAPM Regression)

Regress the fund's excess returns against the benchmark's excess returns:

    R_p - R_f = alpha + beta * (R_b - R_f) + epsilon

- **Beta** tells you the fund's sensitivity to the benchmark. A beta of 1.2 means the fund amplifies benchmark moves by 20%, which partly explains both the 12% return and the 18% volatility.
- **Alpha** is the return unexplained by market exposure. Positive alpha after adjusting for beta is genuine skill (or luck, over short periods).
- **Statistical significance** matters. Over only 5 years (60 monthly observations), alpha estimates have wide confidence intervals. A t-statistic above 2.0 on alpha is meaningful; below that, you cannot confidently distinguish skill from noise.

### 6. Treynor Ratio

If beta is your risk measure (systematic risk only), the Treynor ratio is:

    Treynor = (R_p - R_f) / beta

This is useful when the fund is part of a diversified portfolio, since diversification eliminates idiosyncratic risk and only systematic (beta) risk remains.

## Benchmark Comparison Process

### Step 1: Choose the Right Benchmark

The benchmark must be investable, representative, and specified in advance. If this is a US large-cap equity fund, the S&P 500 total return index is standard. Using the wrong benchmark will make every subsequent calculation meaningless.

### Step 2: Compare Raw Numbers

Over the same 5-year period, get the benchmark's annualized return, standard deviation, and max drawdown. For example, if the S&P 500 returned 10% with 16% volatility and a -34% max drawdown over the same window, your fund delivered 2% higher return with 2% more volatility and slightly less drawdown -- a reasonable profile.

### Step 3: Compute Relative Metrics

- **Excess return**: 12% - benchmark return
- **Tracking error**: standard deviation of the return difference series
- **Information ratio**: excess return / tracking error
- **Up/down capture ratios**: In months the benchmark was up, what fraction of the upside did the fund capture? In down months, what fraction of the downside? A fund with up-capture above 100% and down-capture below 100% is genuinely adding value.

### Step 4: Assess Statistical Significance

Five years is a relatively short evaluation period. With monthly data you have about 60 observations. Be cautious about drawing strong conclusions:
- Alpha estimates will have wide standard errors
- A fund could outperform by 2% annualized purely by chance
- Look at rolling 3-year periods to see if performance is consistent or driven by one exceptional year

### Step 5: Examine Return Distribution Properties

- **Skewness**: Negative skew (fat left tail) means the standard deviation understates true risk. Many equity strategies have negative skew.
- **Kurtosis**: Excess kurtosis (fat tails) means extreme events happen more often than a normal distribution predicts. The -32% drawdown during COVID is a tail event worth examining.
- If the return distribution is significantly non-normal, the Sharpe ratio becomes less reliable, and metrics like the Sortino ratio, Omega ratio, or conditional VaR (expected shortfall) become more informative.

## Putting It All Together

For your fund specifically:

1. A 12% return with 18% volatility produces a Sharpe around 0.56 -- acceptable but not compelling on its own.
2. The -32% drawdown is significant. How quickly did the fund recover? Was the drawdown comparable to or better than the benchmark's?
3. The real question is whether the extra return (vs. benchmark) compensates for the extra risk taken. The information ratio answers this directly.
4. Five years is barely enough data to draw conclusions. If most of the outperformance came from one exceptional year (e.g., 2020 recovery), the result is fragile.
5. Consider whether you could have achieved a similar risk-return profile with a lower-cost index fund plus leverage or a simple factor tilt (value, momentum, quality). If so, the fund's active management may not be worth its fees.

## Summary of Recommended Metrics

| Metric | What It Measures | Key Threshold |
|---|---|---|
| Sharpe Ratio | Return per unit of total risk | > 0.5 acceptable, > 1.0 strong |
| Sortino Ratio | Return per unit of downside risk | Higher than Sharpe is favorable |
| Calmar Ratio | Return relative to worst drawdown | > 0.5 preferred |
| Information Ratio | Active return per unit of tracking error | > 0.5 good, > 1.0 exceptional |
| Alpha (CAPM) | Benchmark-adjusted excess return | Positive with t-stat > 2.0 |
| Beta | Sensitivity to benchmark | Context-dependent |
| Up/Down Capture | Asymmetry of participation | Up > 100%, Down < 100% |
| Max Drawdown Recovery | Time to recoup peak losses | Shorter is better |
