# Estimating the Probability of Missing a 6% Real Return Target Over 15 Years (70/30 Stock/Bond Portfolio)

This is a forward-looking risk analysis problem. You need to estimate the probability that your portfolio's annualized real return falls below 6% over a 15-year horizon. Below is a structured approach using the risk models and simulation techniques most appropriate for this question.

---

## 1. Monte Carlo Simulation (Primary Method)

Monte Carlo simulation is the strongest tool here because the 15-year horizon introduces path dependency, non-normal compounding effects, and regime changes that parametric VaR cannot capture.

### Setup

1. **Define asset return distributions.** Estimate expected real returns and volatilities for each asset class:
   - Equities: e.g., mu = 7.0% real, sigma = 18%
   - Bonds: e.g., mu = 2.0% real, sigma = 5%
   - Correlation: rho approximately -0.10 to +0.30 (use a historically calibrated estimate; a reasonable starting point is rho = 0.0 to 0.1 for stocks vs. intermediate bonds in real terms)

2. **Construct the covariance matrix** from the volatilities and correlation:

   ```
   Sigma = | sigma_eq^2                rho * sigma_eq * sigma_bd |
           | rho * sigma_eq * sigma_bd   sigma_bd^2              |
   ```

3. **Use Cholesky decomposition** of Sigma to generate correlated random returns for each simulation year.

4. **Simulate 10,000+ paths** of 15 annual returns. For each path:
   - Draw correlated annual real returns for stocks and bonds
   - Compute the portfolio annual return: R_p = 0.70 * R_eq + 0.30 * R_bd
   - Compound across 15 years to get the terminal wealth
   - Compute the annualized real return: (terminal_wealth / initial_wealth)^(1/15) - 1

5. **Count the proportion of paths** where the annualized real return falls below 6%. That proportion is your estimated shortfall probability.

### Enhancements for Realism

- **Fat tails:** Use a Student-t distribution (degrees of freedom 4-6) or a skewed-t distribution instead of a normal distribution. Financial returns exhibit fat tails, and parametric normality systematically underestimates tail risk.
- **Regime switching:** Consider a two-regime model (bull/bear or normal/crisis) where volatilities, correlations, and expected returns differ by regime. This captures the empirically observed pattern that correlations spike toward 1.0 during market stress.
- **Mean reversion and serial correlation:** For a 15-year horizon, equity valuations (CAPE ratio) tend to mean-revert, which affects long-horizon return distributions. Consider conditioning expected returns on current valuation levels.

---

## 2. Parametric VaR as a Quick Benchmark

Use the variance-covariance method for a rough analytical estimate before running the full simulation.

### Portfolio volatility:

```
sigma_p = sqrt(0.70^2 * 0.18^2 + 0.30^2 * 0.05^2 + 2 * 0.70 * 0.30 * rho * 0.18 * 0.05)
```

With rho = 0.05:

```
sigma_p = sqrt(0.015876 + 0.000225 + 0.000189) = sqrt(0.01629) = 12.76%
```

### Expected real return:

```
mu_p = 0.70 * 7.0% + 0.30 * 2.0% = 5.50%
```

This immediately flags an issue: the expected return of 5.50% is already below the 6% target. The probability of underperformance is therefore greater than 50% under these assumptions. This is a critical finding that should be discussed with the client before proceeding.

### Annualized shortfall probability (normal approximation):

Over 15 years, the standard error of the annualized return is approximately sigma_p / sqrt(15) = 12.76% / 3.87 = 3.30%. The z-score for the 6% target:

```
z = (6.0% - 5.50%) / 3.30% = 0.15
```

The probability of falling below 6% annualized is approximately Phi(0.15) = 56%.

Note: This is a rough estimate. The parametric approach assumes normality, ignores compounding effects, and uses the square-root-of-time scaling that becomes unreliable over long horizons. Use it as a sanity check, not the final answer.

---

## 3. Scenario Analysis and Stress Testing

Complement the Monte Carlo simulation with specific stress scenarios to understand worst-case outcomes:

| Scenario | Equity Shock | Bond Shock | Correlation Assumption | Notes |
|----------|-------------|------------|----------------------|-------|
| 2008 GFC replay | -37% first year, slow recovery | +5% flight to quality | Correlation spikes to +0.8 for credit-sensitive bonds | Tests deep drawdown and recovery path |
| Stagflation (1970s-style) | Real returns -5% to 0% for 5 years | Real returns -3% (rates rise, bond prices fall) | Correlation goes positive | Both asset classes suffer simultaneously |
| Japan-style deflation | Equity returns 0-2% real for 15 years | Bond returns 0-1% real | Low correlation | Secular stagnation scenario |
| 2022 rate shock | -18% equities, -13% bonds | Simultaneous drawdown | Correlation spikes positive | Modern stress scenario for 70/30 |

For each scenario, compute the terminal wealth and annualized return to determine whether the 6% target is met. The stagflation and Japan scenarios are particularly important for a 15-year horizon because they represent sustained underperformance rather than a single shock followed by recovery.

---

## 4. Factor-Based Risk Decomposition

Decompose the portfolio risk into factor exposures to understand what is driving the return and risk profile:

```
sigma^2_p = b' * Sigma_f * b + sum(w_i^2 * sigma^2_epsilon_i)
```

Key factors for a 70/30 portfolio:
- **Equity risk premium:** The dominant return driver (approximately 70-80% of total risk)
- **Duration / interest rate risk:** Drives bond returns and partially affects equity valuations
- **Inflation risk:** Critical for a real return target -- unexpected inflation erodes both stock and bond real returns
- **Valuation (CAPE):** Current equity valuations affect the forward equity risk premium

This decomposition helps identify whether the shortfall risk is concentrated in a single factor (equity beta) or spread across multiple sources.

---

## 5. CVaR / Expected Shortfall for Tail Severity

Beyond the probability of missing the target, compute the Expected Shortfall to answer: "If the portfolio does miss the 6% target, how badly does it miss?"

```
ES = E[annualized return | annualized return < 6%]
```

From the Monte Carlo simulation, average the annualized returns across all paths that fall below 6%. If the probability of shortfall is 56% but the average shortfall return is 4.5%, the magnitude of the miss is moderate. If the average shortfall return is 1%, the consequences are severe and may require a different allocation or a revised target.

---

## Recommendations

1. **Run the Monte Carlo simulation** with at least 10,000 paths, using fat-tailed distributions and historically calibrated parameters. This is the most informative analysis for a 15-year horizon.

2. **Challenge the capital market assumptions.** The parametric estimate suggests the expected return (5.50% real for 70/30) is below the 6% target. Validate your expected return assumptions carefully -- small changes in assumed equity risk premium (e.g., 7% vs. 8% real) will substantially shift the shortfall probability.

3. **Consider the current valuation regime.** If equity valuations are elevated (high CAPE), the forward equity risk premium may be lower than historical averages, increasing shortfall probability further.

4. **Run stress tests with crisis-period correlations.** Stock-bond correlation has been positive in inflationary environments (2022 is a recent example). A 70/30 portfolio provides less diversification benefit when both asset classes decline together.

5. **Present both the probability and severity.** Give the client the shortfall probability and the CVaR (expected return conditional on missing the target) so they can make an informed decision about whether to accept the risk, increase the equity allocation, extend the time horizon, or reduce the return target.

6. **Use Component VaR** to show the client that roughly 85-90% of the portfolio's risk comes from the equity allocation. If they want to reduce shortfall probability without reducing the return target, the primary lever is increasing expected return (more equity, alternative assets) -- not reducing risk (more bonds), which would lower expected return further below the target.
