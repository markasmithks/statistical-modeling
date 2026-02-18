from src.simulation import simulate_terminal_stock_prices, discounted_put_payoff

S = simulate_terminal_stock_prices(
    S0=100,
    mu=0.10,
    sigma=0.15,
    T=10,
    n_scenarios=5,
    n_inner=10,
    seed=42
)

C = discounted_put_payoff(S, K=110, r=0.06, T=10)

print(S.shape)
print(C.shape)
print(C[:2])
