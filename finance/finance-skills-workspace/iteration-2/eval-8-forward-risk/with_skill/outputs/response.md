# Estimating the Probability of Missing a 6% Real Return Target for a 70/30 Portfolio Over 15 Years

## Framing the Problem

You need to estimate P(annualized real return < 6%) for a 70/30 stock/bond allocation over a 15-year horizon. This is a forward-looking risk analysis problem that requires modeling the full distribution of cumulative portfolio outcomes, not just a single-period VaR. The tools below, drawn from forward-looking risk methodology, build on each other in increasing sophistication.

## Recommended Approach: Monte Carlo Simulation

Monte Carlo simulation is the right primary tool here because your question involves a multi-year horizon with compounding, which makes parametric (variance-covariance) VaR insufficient. Parametric VaR assumes normality and works best for short horizons; over 15 years, compounding effects, fat tails, and regime changes dominate.

### Step 1: Specify Capital Market Assumptions

Define forward-looking expected returns, volatilities, and correlations for your two asset classes in real (inflation-adjusted) terms. A reasonable starting point:

| Parameter | Equities | Bonds |
|-----------|----------|-------|
| Expected real return (mu) | 5.0-7.0% | 1.0-2.5% |
| Volatility (sigma) | 16-20% | 4-7% |
| Correlation (rho) | -0.1 to +0.2 | -- |

Use multiple sets of assumptions (optimistic, base, pessimistic) to understand sensitivity. The portfolio parameters for a 70/30 allocation are:

```
mu_p    = 0.70 * mu_equity + 0.30 * mu_bond
sigma_p = sqrt(0.70^2 * sigma_eq^2 + 0.30^2 * sigma_bd^2 + 2 * 0.70 * 0.30 * rho * sigma_eq * sigma_bd)
```

For example, with mu_eq = 6%, mu_bd = 2%, sigma_eq = 18%, sigma_bd = 5%, rho = 0.0:

```
mu_p    = 0.70 * 0.06 + 0.30 * 0.02 = 4.8%
sigma_p = sqrt(0.49 * 0.0324 + 0.09 * 0.0025 + 0) = sqrt(0.01611) = 12.69%
```

### Step 2: Run Monte Carlo Simulation (10,000+ Paths)

For each simulation path:

1. Construct the covariance matrix from your volatilities and correlation.
2. Use Cholesky decomposition to generate correlated annual return pairs for equities and bonds.
3. Compute the portfolio return each year: R_p,t = 0.70 * R_eq,t + 0.30 * R_bd,t.
4. Compound over 15 years to get the terminal wealth: W_15 = W_0 * product(1 + R_p,t) for t = 1..15.
5. Compute the annualized real return: r_annualized = (W_15 / W_0)^(1/15) - 1.

After generating 10,000+ paths, the probability of missing the 6% target is simply:

```
P(shortfall) = count(r_annualized < 0.06) / N
```

### Step 3: Use Fat-Tailed Distributions

Standard Monte Carlo with multivariate normal returns will underestimate tail risk. Financial returns exhibit fat tails and skewness, and over a 15-year horizon, a few extreme years can dominate outcomes. Enhance the simulation by:

- **Student-t distributed returns** (e.g., 5-8 degrees of freedom) to capture fat tails.
- **Regime-switching models**: alternate between a "normal" regime (moderate vol, positive drift) and a "crisis" regime (high vol, negative drift, spiking correlations). This captures the empirical fact that correlations break down in crises -- correlations spike toward 1.0 during market stress, precisely when diversification is most needed.
- **Block bootstrap from historical data**: resample actual annual return pairs to preserve the empirical joint distribution without imposing a parametric form.

### Step 4: Stress Testing and Scenario Analysis

Complement the Monte Carlo with specific stress scenarios to understand what drives failure:

- **Secular stagnation**: equities return 3% real, bonds return 0% real for a decade, then revert.
- **Stagflation**: inflation +5%, GDP -3%, rates +200bp -- both stocks and bonds suffer simultaneously.
- **2008-style crisis early in the horizon**: a -35% equity drawdown in years 1-2 creates a hole that 13 years of normal returns may not fill (sequence-of-returns risk).
- **Japan scenario**: prolonged low returns across both asset classes for the full period.
- **Rising rate environment**: bond returns persistently negative for 5+ years, equity multiples compress.

For each scenario, compute the annualized 15-year real return and whether the 6% target is met.

### Step 5: Factor-Based Risk Decomposition

Break the portfolio's risk into systematic factor exposures to understand what is driving the probability of failure:

```
sigma^2_p = b' * Sigma_f * b + sum(w_i^2 * sigma^2_epsilon_i)
```

Key factors to model for a 70/30 allocation:
- **Equity market risk**: the dominant factor, likely contributing 85-90% of total portfolio variance.
- **Duration / interest rate risk**: the bond allocation's sensitivity to rate changes.
- **Inflation risk**: since your target is in real terms, unexpected inflation is a direct risk to meeting it.
- **Valuation risk**: current CAPE levels affect forward equity return distributions.

This decomposition reveals that missing the 6% real target is overwhelmingly an equity risk problem -- the bond allocation contributes modest return and modest risk.

## Expected Results and Interpretation

Using base-case assumptions (mu_p = 4.8% real, sigma_p = 12.7%), the 6% target exceeds the expected portfolio return. A rough analytical estimate under lognormal assumptions:

```
P(geometric return < 6%) = P(arithmetic return < ~6.8% after volatility drag)
```

With mu_p below the target, the probability of shortfall will be **above 50%** -- likely in the 55-70% range depending on assumptions. This is a critical finding: a 70/30 portfolio may not have a favorable probability of achieving 6% real.

To improve the odds, consider:
- Increasing the equity allocation (accepting more volatility)
- Lowering the return target
- Adding higher-returning asset classes (small-cap value, emerging markets, alternatives)
- Extending the time horizon

## Key Pitfalls to Avoid

- **Do not use parametric VaR alone for this analysis.** VaR says nothing about the shape of the tail, and parametric VaR assumes normality which systematically underestimates tail risk over long horizons.
- **Always compute CVaR / Expected Shortfall alongside VaR.** If the portfolio misses the 6% target, you need to know by how much on average: ES_alpha = E[Loss | Loss > VaR_alpha]. Two portfolios with the same probability of missing the target can have very different expected shortfalls.
- **Do not use a single correlation estimate.** Use crisis-period correlations for stress scenarios and consider regime-switching models. A calm-period stock/bond correlation of -0.2 may flip to +0.5 during stagflationary episodes.
- **Account for volatility drag on compounded returns.** The geometric (compounded) return is approximately mu - sigma^2/2. With sigma_p = 12.7%, the volatility drag is about 0.8%, which means the expected compounded return is meaningfully below the arithmetic mean.
- **Do not scale short-horizon VaR to 15 years using the square-root-of-time rule.** VaR_h = VaR_1 * sqrt(h) assumes i.i.d. returns and breaks down with serial correlation, mean reversion, and volatility clustering over long horizons.

## Summary of Recommended Models

| Model | Purpose | Complexity |
|-------|---------|------------|
| Monte Carlo (multivariate normal) | Baseline probability estimate | Medium |
| Monte Carlo (Student-t or regime-switching) | Fat-tail-adjusted probability | High |
| Block bootstrap from historical data | Non-parametric probability estimate | Medium |
| Scenario analysis (6-8 scenarios) | Understand specific failure modes | Low-Medium |
| Factor decomposition | Identify dominant risk drivers | Medium |
| CVaR analysis | Quantify expected shortfall severity | Medium |

Start with the multivariate normal Monte Carlo for a baseline, then layer in fat tails and regime switching to get a more realistic estimate. The scenario analysis and factor decomposition provide qualitative insight into why and how the portfolio might fail, which is essential for client communication and portfolio design decisions.
