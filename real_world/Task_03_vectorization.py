import numpy as np
import timeit
# Real-world case: Compute log-returns and squared volatility terms across
# 2,000,000 tick-by-tick equity price observations.
# Assumptions: Prices follow a positive continuous stream around 150.00 USD.
rng = np.random.default_rng(2026)
price_changes = rng.normal(loc=0.0001, scale=0.002, size=2_000_000)
prices = 150.0 * np.exp(np.cumsum(price_changes))
def loop_log_returns():
sq_returns = []
for i in range(1, len(prices)):
r = np.log(prices[i] / prices[i - 1])
sq_returns.append(r ** 2)
return sq_returns
def vectorized_log_returns():
r = np.log(prices[1:] / prices[:-1])
return r ** 2
t_loop = timeit.timeit(loop_log_returns, number=1)
t_vec = timeit.timeit(vectorized_log_returns, number=5) / 5
sq_ret = vectorized_log_returns()
realized_vol = np.sqrt(np.sum(sq_ret))
print(f"Realized volatility over period: {realized_vol:.6f}")
print(f"Loop execution time: {t_loop:.4f} s")
print(f"Vectorized execution time: {t_vec:.4f} s")
print(f"Speed-up factor: {t_loop / t_vec:.1f}x")