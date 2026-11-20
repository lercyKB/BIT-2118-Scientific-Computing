import numpy as np
from scipy.stats import norm
# Modified: Increased sample size N = 500,000, higher demand volatility (std =
160),
# upgraded server capacity (1,100), and comparison against exact Gaussian CDF
rng = np.random.default_rng(101)
capacity = 1100.0
mean_demand = 850.0
std_demand = 160.0
N = 500_000
demand = rng.normal(mean_demand, std_demand, N)
mc_prob = np.mean(demand > capacity)
exact_prob = 1.0 - norm.cdf(capacity, loc=mean_demand, scale=std_demand)
print(f"Monte Carlo overload probability (N=500k): {mc_prob:.4%}")
print(f"Exact analytical probability: {exact_prob:.4%}")
print(f"Monte Carlo estimation error: {abs(mc_prob -
exact_prob):.4%}")