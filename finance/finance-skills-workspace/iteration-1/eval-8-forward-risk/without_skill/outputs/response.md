# Estimating Shortfall Probability for a 70/30 Portfolio Against a 6% Real Return Target

## Problem Setup

You need to estimate the probability that a 70% equity / 30% bond portfolio fails to achieve a 6% annualized real (inflation-adjusted) return over 15 years. This is a classic **shortfall risk** or **goal-based risk** problem.

## Recommended Risk Models

### 1. Monte Carlo Simulation (Primary Approach)

Monte Carlo simulation is the most flexible and widely used method for this type of analysis. The process:

1. **Define capital market assumptions (CMAs):** Specify expected real returns, volatilities, and correlations for equities and bonds. For example:
   - US equities: expected real return ~5-7%, volatility ~15-17%
   - US investment-grade bonds: expected real return ~1-2%, volatility ~5-7%
   - Correlation between stocks and bonds: typically -0.1 to +0.3 historically

2. **Model return dynamics:** Choose a return-generating process:
   - **Geometric Brownian Motion (GBM):** The simplest model. Assumes log-normal returns with constant drift and volatility. Easy to implement but ignores fat tails and time-varying volatility.
   - **Regime-switching models:** Model two or more market regimes (e.g., bull/bear or low-vol/high-vol) with a Markov chain governing transitions. This captures clustering of bad returns and varying correlations during crises.
   - **Vector autoregression (VAR):** Models the joint dynamics of stock and bond returns along with predictor variables like dividend yield, term spread, and inflation. Captures mean reversion in valuations.

3. **Run simulations:** Generate 10,000+ paths of 15-year portfolio returns. For each path, compound the annual returns and check whether the terminal wealth exceeds the 6% real annualized target.

4. **Estimate shortfall probability:** The fraction of paths that fail to meet the target is your shortfall probability estimate.

**Key implementation details:**
- Use **geometric** (compound) returns, not arithmetic. Arithmetic averages overstate long-horizon expected growth.
- Apply the **volatility drag** correction: expected compound return is approximately E[r] - sigma^2 / 2.
- Rebalance the portfolio annually (or at whatever frequency the client expects) within each simulation path.
- Account for **parameter uncertainty** by using Bayesian or bootstrap methods for the CMAs rather than point estimates.

### 2. Historical Bootstrap Simulation

Rather than assuming a parametric distribution, draw blocks of historical returns (with replacement) to build simulated 15-year paths.

- **Block bootstrap:** Draw contiguous blocks of 1-3 year returns to preserve autocorrelation and cross-asset correlation structure.
- **Stationary bootstrap:** Use random-length blocks drawn from a geometric distribution to avoid artifacts from fixed block size.

**Advantages:** Captures the actual joint distribution including fat tails, skewness, and time-varying correlations without imposing a model.

**Limitations:** Limited to the historical sample. If your history is 50 years, you have limited data for 15-year outcomes. Does not allow you to condition on current valuations.

### 3. Analytical Approximation (Quick Check)

For a rough estimate, you can use the closed-form log-normal model:

- Portfolio expected real return (arithmetic): 0.70 * E[r_eq] + 0.30 * E[r_bond]
- Portfolio volatility: sqrt(w_eq^2 * sigma_eq^2 + w_bond^2 * sigma_bond^2 + 2 * w_eq * w_bond * sigma_eq * sigma_bond * rho)
- Expected compound return: mu_c = mu_a - sigma_p^2 / 2
- Over T=15 years, log terminal wealth is approximately Normal(mu_c * T, sigma_p^2 * T)
- Shortfall probability: P(compound return < 6%) = Phi((ln(1.06)*T - mu_c*T) / (sigma_p * sqrt(T)))

This gives a quick baseline but understates tail risk because it assumes normality.

### 4. Fat-Tail Models

To capture extreme events more realistically:

- **Student-t copula:** Model marginal distributions with fat tails (Student-t with 4-6 degrees of freedom) and use a copula for the dependence structure. This captures both individual fat tails and tail dependence (correlations increasing during crises).
- **GARCH models:** Allow volatility to cluster and mean-revert, producing fatter tails endogenously. An EGARCH or GJR-GARCH specification captures the leverage effect (volatility rising more after negative returns).
- **Stable distributions:** Levy-stable or tempered stable distributions for returns. Computationally more complex but theoretically motivated.

## Practical Recommendations

### Recommended Workflow

1. **Start with the analytical approximation** to get a baseline shortfall probability. With typical CMAs (portfolio real return ~4.5%, volatility ~11%), the shortfall probability for a 6% real target over 15 years is likely in the 40-60% range -- the target is aggressive.

2. **Run a Monte Carlo simulation with GBM** as the primary model. Use 50,000+ paths for stable estimates.

3. **Run a regime-switching Monte Carlo** as a stress test. Calibrate to historical bull/bear regimes. This typically increases the shortfall probability by 5-15 percentage points relative to GBM.

4. **Run a historical block bootstrap** as a model-free cross-check.

5. **Report the range** of shortfall probabilities across methods, not a single number. The spread itself communicates model uncertainty.

### Capital Market Assumptions to Consider

Your CMAs are the single largest driver of the result. Be explicit about:

- **Current valuations:** If equity CAPE ratios are elevated, consider conditioning expected returns downward. A building-block approach (dividend yield + earnings growth + valuation change) is more defensible than raw historical averages.
- **Bond yields:** Use current real yields on TIPS as the bond return anchor, not historical averages. As of recent years, real yields have varied between -1% and +2%.
- **Inflation assumption:** If your target is 6% real, make sure all return inputs are also real (or model nominal returns and inflation separately).

### Sensitivity Analysis

Run the simulation across a grid of assumptions:
- Expected equity real return: 4%, 5%, 6%, 7%
- Equity volatility: 14%, 16%, 18%
- Bond real return: 0%, 1%, 2%
- Stock-bond correlation: -0.2, 0.0, +0.2

This produces a sensitivity table showing how the shortfall probability changes with assumptions, which is far more informative for the client than a single number.

### Additional Considerations

- **Sequence-of-returns risk:** If the client will be making contributions or withdrawals during the 15 years, the order of returns matters significantly. A standard Monte Carlo naturally captures this, but make sure your simulation includes the cash flow schedule.
- **Rebalancing assumptions:** Specify whether the portfolio is rebalanced annually, quarterly, or at drift thresholds. Rebalancing frequency has a modest but measurable effect on compound returns.
- **Tax drag:** If this is a taxable account, rebalancing triggers capital gains. Consider after-tax return adjustments.
- **Fees:** Deduct expected management fees from return assumptions.

## Summary

A 6% real return target over 15 years is ambitious for a 70/30 portfolio given typical capital market assumptions. The most rigorous approach combines Monte Carlo simulation (using both parametric and bootstrap methods), regime-switching models for stress testing, and sensitivity analysis across CMAs. Report a range of shortfall probabilities rather than a point estimate, and ensure the client understands that the CMAs themselves are the dominant source of uncertainty.
