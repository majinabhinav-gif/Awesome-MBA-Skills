# Assessing Risk-Adjusted Returns: A Framework

A raw 12% annualized return tells you nothing in isolation. You need to measure how much risk was taken to earn that return and whether the benchmark delivered similar returns with less (or more) risk. Here are the key metrics.

## 1. Sharpe Ratio

The most common starting point. It measures excess return per unit of total risk:

    Sharpe = (R_portfolio - R_f) / StdDev_portfolio

With your numbers, assuming a risk-free rate of roughly 2% over the period:

    Sharpe = (12% - 2%) / 18% = 0.56

A Sharpe above 0.5 is decent, above 1.0 is strong. But you must compare it to the benchmark's Sharpe over the same period. If the S&P 500 delivered 14% with 16% volatility, its Sharpe would be 0.75 -- meaning the benchmark was actually more efficient despite your fund's respectable absolute number.

## 2. Sortino Ratio

Standard deviation penalizes both upside and downside volatility equally. The Sortino ratio fixes this by using only downside deviation:

    Sortino = (R_portfolio - R_f) / DownsideDev

If your fund's volatility is skewed to the upside (big gains, smaller losses), the Sortino will be meaningfully higher than the Sharpe and gives a fairer picture. You will need the downside deviation figure from the fund's fact sheet or calculate it from monthly returns.

## 3. Maximum Drawdown and Calmar Ratio

Your -32% max drawdown is significant. The Calmar ratio contextualizes it:

    Calmar = Annualized Return / |Max Drawdown| = 12% / 32% = 0.375

This means you earned 0.375 units of return for every unit of peak-to-trough loss. Compare this to the benchmark: the S&P 500 drew down roughly -34% during COVID, so if the benchmark returned 14% its Calmar would be about 0.41 -- slightly better. A Calmar below 0.5 generally signals that drawdowns are large relative to the return earned.

## 4. Information Ratio

This measures whether the fund's active bets (deviations from benchmark) are adding value:

    IR = (R_portfolio - R_benchmark) / TrackingError

If the fund returned 12% vs. a benchmark at 14%, the excess return is -2%. Even with low tracking error, a negative information ratio means active management destroyed value. This is the single most important metric for evaluating an active fund against its benchmark.

## 5. Alpha and Beta (Jensen's Alpha)

Run a regression of the fund's returns against the benchmark:

- **Beta** tells you the fund's sensitivity to benchmark moves. A beta of 1.1 means 10% more market exposure, which partly explains higher volatility.
- **Alpha** is the intercept -- return earned above what beta exposure alone would predict. Positive alpha after adjusting for beta is genuine skill; negative alpha means the manager is not compensating you for the risk taken.

Formula:

    Jensen's Alpha = R_portfolio - [R_f + Beta * (R_benchmark - R_f)]

## 6. Capture Ratios

These are intuitive and often overlooked:

- **Upside capture**: what percentage of the benchmark's positive months does the fund capture?
- **Downside capture**: what percentage of the benchmark's negative months does the fund participate in?

A fund with 90% upside capture and 70% downside capture is genuinely adding value through asymmetry, even if its raw return is slightly lower.

## Putting It Together for Your Fund

With 12% return, 18% volatility, and -32% drawdown:

- The Sharpe of ~0.56 is moderate. Not bad, not exceptional.
- The -32% drawdown is roughly in line with broad equity benchmarks during COVID, so the fund did not protect capital during the crisis.
- You need the benchmark's numbers over the identical period to draw any conclusion. If the benchmark returned more with similar or less risk, the fund underperformed on a risk-adjusted basis regardless of the 12% headline.

## What to Ask For From the Fund

- Monthly return series (not just annualized summary statistics)
- Downside deviation and Sortino ratio
- Upside/downside capture ratios vs. stated benchmark
- Rolling 12-month alpha and information ratio
- Maximum drawdown recovery time (how many months to recover from the -32% trough)

Recovery time matters: a -32% drawdown that took 18 months to recover is far worse than one that recovered in 6 months, even though the drawdown magnitude is identical.

## Bottom Line

A 12% return with 18% vol and -32% drawdown is plausible for a fund with equity-like risk. Whether it is "good" depends entirely on the benchmark comparison. If you cannot beat a low-cost index fund's Sharpe ratio and information ratio over the same window, the risk-adjusted returns are not justifying active management fees.
