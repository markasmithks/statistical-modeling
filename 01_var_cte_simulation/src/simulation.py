import numpy as np


def simulate_terminal_stock_prices(
    S0: float,
    mu: float,
    sigma: float,
    T: float,
    n_scenarios: int,
    n_inner: int,
    seed: int | None = None
) -> np.ndarray:
    """
    Simulate terminal stock prices under a lognormal model.

    Returns
    -------
    S : ndarray of shape (n_scenarios, n_inner)
        Simulated terminal stock prices.
    """

    rng = np.random.default_rng(seed)

    Z = rng.standard_normal(size=(n_scenarios, n_inner))
    # 2D standard normal

    drift = (mu - 0.5 * sigma**2) * T
    diffusion = sigma * np.sqrt(T) * Z

    S = S0 * np.exp(drift + diffusion)

    return S


def discounted_put_payoff(
    S: np.ndarray,
    K: float,
    r: float,
    T: float
) -> np.ndarray:
    """
    Compute discounted European put payoff.
    """

    discount = np.exp(-r * T)
    payoff = np.maximum(0.0, K - S)

    return discount * payoff
