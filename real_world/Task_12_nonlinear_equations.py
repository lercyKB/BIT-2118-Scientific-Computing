import numpy as np
from scipy.optimize import root
# Real-world case: Find simultaneous equilibrium prices (P1, P2) for two
# interdependent commodities (e.g., electric vehicles and lithium battery packs)
# where demand and supply functions are nonlinear.
# Assumptions:
# Commodity 1: Demand D1 = 120 - 2*P1^1.2 + 0.5*P2, Supply S1 = 15 + 1.8*P1
# Commodity 2: Demand D2 = 90 + 0.4*P1 - 1.5*P2^1.1, Supply S2 = 10 + 2.2*P2
def market_excess_demand(prices):
P1, P2 = prices
excess_1 = (120.0 - 2.0 * (P1 ** 1.2) + 0.5 * P2) - (15.0 + 1.8 * P1)
excess_2 = (90.0 + 0.4 * P1 - 1.5 * (P2 ** 1.1)) - (10.0 + 2.2 * P2)
return [excess_1, excess_2]
sol = root(market_excess_demand, [20.0, 20.0])
print("Market Clearing Equilibrium Prices (P1, P2):", np.round(sol.x, 4))
print("Excess Demand Residuals:", np.round(sol.fun, 10))
print("Solver Converged:", sol.success)