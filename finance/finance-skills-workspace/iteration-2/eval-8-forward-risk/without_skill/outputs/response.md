# Estimating Shortfall Probability for a 70/30 Portfolio Against a 6% Real Return Target

## Problem Setup

You need the probability that a 70/30 stock/bond portfolio fails to achieve a 6% annualized real return over 15 years. This is a **shortfall risk** problem -- specifically, the probability that the terminal real wealth ratio falls below (1.06)^15 = 2.397.

## Step 1: Capital Market Assumptions

Before running any model you need forward-looking estimates of:

- **Expected real returns** for equities and bonds (arithmetic and geometric)
- **Volatilities** (annualized standard deviation of real returns)
- **Correlation** between equities and bonds
- **Autocorrelation structure** (mean reversion or momentum over multi-year horizons)

Common sources for these assumptions include Research Affiliates, AQR, Vanguard Capital Markets Model, JP Morgan Long-Term Capital Market Assumptions, and BlackRock. For a 15-year horizon today, reasonable ballpark estimates might be:

| Parameter | US Equities | US Agg Bonds |
|---|---|---|
| Expected real return (arithmetic) | 5.0--7.0% | 1.0--2.5% |
| Volatility | 16--18% | 4--6% |
| Correlation | -0.1 to +0.3 | -- |

The blended 70/30 portfolio expected real return (arithmetic) would then be roughly 3.8--5.7%, and the geometric (compound) return would be lower due to volatility drag. This immediately signals that a 6% real target is ambitious for this allocation -- the shortfall probability is likely material.

## Step 2: Risk Models

### 2a. Parametric (Closed-Form) Approach

If returns are i.i.d. lognormal:

- Portfolio arithmetic mean: mu_p = 0.70 * mu_eq + 0.30 * mu_bond
- Portfolio variance: sigma_p^2 = 0.70^2 * sigma_eq^2 + 0.30^2 * sigma_bond^2 + 2 * 0.70 * 0.30 * rho * sigma_eq * sigma_bond
- Geometric mean: mu_g = mu_p - sigma_p^2 / 2
- Over T = 15 years, the annualized compound return is approximately normal with mean mu_g and standard deviation sigma_p / sqrt(T)
- Shortfall probability: P(r_compound < 6%) = Phi((0.06 - mu_g) / (sigma_p / sqrt(T)))

This is fast and useful as a sanity check but assumes normality, independence across time, and constant parameters.

### 2b. Monte Carlo Simulation

This is the standard approach for realistic modeling. At minimum:

1. **Draw correlated annual real returns** from a bivariate distribution (stocks, bonds) for 15 years
2. **Compound them** to get the terminal portfolio value
3. **Repeat 10,000--100,000 times**
4. **Count** the fraction of paths where the annualized compound return is below 6%

Key modeling choices within Monte Carlo:

- **Return distribution**: Lognormal is the baseline. For fatter tails, use a Student-t copula or skewed-t marginals. Equity returns exhibit negative skewness and excess kurtosis, which a normal model understates.
- **Correlation structure**: Use a constant correlation, a DCC-GARCH model for time-varying correlation, or a copula (Gaussian or Clayton for tail dependence).
- **Regime switching**: A two-regime (bull/bear) Markov model captures the clustering of bad returns. In the bear regime, equity volatility is higher, expected returns lower, and stock-bond correlation may shift. This materially affects multi-year shortfall probability.
- **Mean reversion**: Over 15 years, equity valuations tend to mean-revert. You can model this by conditioning expected returns on starting CAPE or by introducing negative autocorrelation at the 3--7 year horizon.

### 2c. Block Bootstrap

Instead of assuming a parametric distribution:

1. Sample (with replacement) contiguous blocks of 1--3 year historical real returns for both asset classes simultaneously (preserving cross-asset correlation and short-term autocorrelation)
2. Chain blocks together to form 15-year paths
3. Compute terminal wealth and shortfall frequency

This respects the empirical joint distribution without imposing normality, but is limited to historically observed scenarios.

### 2d. Scenario-Based / Stress Testing

Complement the statistical models with deterministic scenarios:

- **Secular stagnation**: Equities return 3% real, bonds 0% real for 15 years
- **1970s stagflation replay**: High inflation erodes both asset classes
- **Japan analog**: Extended equity drawdown with near-zero bond yields
- **2000--2015 actual**: US equities returned ~4% real, bonds ~3% real -- a 70/30 portfolio delivered ~3.7% real, well below your 6% target

## Step 3: Recommended Simulation Framework

For a rigorous answer, I would recommend a layered approach:

### Layer 1 -- Parametric Quick Estimate
Compute the closed-form shortfall probability under lognormal assumptions. This takes minutes and gives you a baseline.

### Layer 2 -- Monte Carlo with Fat Tails
Run a Monte Carlo with:
- Skewed-t marginal distributions for equity and bond returns (calibrated to historical moments)
- Gaussian or t-copula for dependence
- 50,000+ paths
- Report the shortfall probability, plus the conditional expected return in the shortfall scenarios (expected shortfall / CVaR equivalent)

### Layer 3 -- Regime-Switching Monte Carlo
Fit a 2-regime Hidden Markov Model to historical real returns:
- Regime 1 (expansion): higher equity mean, lower vol
- Regime 2 (contraction): lower equity mean, higher vol, potentially different correlation

Simulate regime transitions and returns jointly. This typically produces higher shortfall probabilities than the i.i.d. model because bad regimes cluster.

### Layer 4 -- Sensitivity Analysis
Vary capital market assumptions across a reasonable range and report a matrix of shortfall probabilities. Key sensitivities:
- Equity risk premium (+/- 1%)
- Bond real yield (+/- 0.5%)
- Equity volatility (15% vs 20%)
- Correlation (-0.1 vs +0.3)
- Starting valuation (CAPE adjustment)

## Step 4: Implementation Notes

**Data**: Use real (inflation-adjusted) total returns. Shiller dataset (1871--present) for long history; CRSP/Bloomberg for post-1926. For bonds, use duration-matched index data or construct synthetic returns from yield curve data.

**Inflation modeling**: If your capital market assumptions are in nominal terms, you need to model inflation separately. A simple AR(1) process for CPI or breakeven inflation expectations works for most purposes.

**Rebalancing**: Assume annual or quarterly rebalancing to the 70/30 target. Drift without rebalancing changes the risk profile over time.

**Fees and taxes**: A 6% real target is even harder after advisory fees (say 50--100 bps) and taxes. Model net-of-fee returns for realism.

**Software**: Python with NumPy/SciPy is standard. The `arch` package handles GARCH and regime-switching models. R's `PerformanceAnalytics` and `rmgarch` packages are also well-suited.

## Expected Findings

Given current capital market assumptions (as of early 2026), a 70/30 US stock/bond portfolio has an expected real geometric return in the range of 4--5%. The probability of failing to achieve 6% real over 15 years is likely **55--75%** depending on your assumptions. Under regime-switching or fat-tailed models, the probability may be higher due to the asymmetric impact of clustered drawdowns on compound returns.

This suggests the client either needs to:
- Accept a lower return target
- Increase equity allocation (accepting more short-term volatility)
- Add return-enhancing diversifiers (international equities, value/small-cap tilts, alternatives)
- Extend the time horizon
