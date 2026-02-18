# 01 — VaR and CTE via Monte Carlo Simulation

## Objective

This module demonstrates the estimation of tail risk measures using Monte Carlo simulation.

Specifically, we:

- Simulate terminal stock prices under a lognormal model
- Price a European put option
- Estimate:
  - Value-at-Risk (VaR)
  - Conditional Tail Expectation (CTE / Expected Shortfall)
- Explore the empirical relationship between VaR and CTE

---

## Model Assumptions

We assume the terminal stock price follows a lognormal distribution:

\[
S_T = S_0 \exp\left((\mu - \tfrac{1}{2}\sigma^2)T + \sigma \sqrt{T} Z\right),
\quad Z \sim N(0,1)
\]

where:

- \( S_0 \) = initial stock price  
- \( \mu \) = drift  
- \( \sigma \) = volatility  
- \( T \) = time horizon  

This implies:

\[
\log(S_T) \sim N\left(\log(S_0) + (\mu - \tfrac{1}{2}\sigma^2)T,\ \sigma^2 T \right)
\]

---

## Option Payoff

We consider a discounted European put option:

\[
C = e^{-rT} \max(0, K - S_T)
\]

where:

- \( K \) = strike price  
- \( r \) = risk-free rate  

---

## Risk Measures

For simulated payoffs \( C_1, \dots, C_n \):

### Value-at-Risk (VaR)

\[
\text{VaR}_{\alpha} = \text{Quantile}_{\alpha}(C)
\]

In this module, we focus on the 95th percentile.

---

### Conditional Tail Expectation (CTE)

\[
\text{CTE}_{\alpha} = \mathbb{E}[C \mid C \ge \text{VaR}_{\alpha}]
\]

CTE measures the average severity of losses beyond the VaR threshold.

---

## Simulation Structure

The Monte Carlo design follows a two-layer structure:

1. For each outer scenario:
   - Generate inner simulations of terminal prices.
   - Compute discounted payoffs.
   - Estimate VaR and CTE.

2. Across scenarios:
   - Analyze the relationship between VaR and CTE.
   - Fit a linear regression model to explore their empirical dependence.

---

## Directory Structure

```
01_var_cte_simulation/
│
├── notebooks/ # Demonstrations and visualizations
├── src/ # Simulation and risk metric implementations
├── figures/ # Exported plots
└── README.md
```

---

## Learning Goals

- Understand how lognormal assumptions generate skewed loss distributions.
- Observe the difference between quantile-based and tail-mean risk measures.
- Explore the statistical relationship between VaR and CTE under simulation.
- Reinforce modular simulation design.

