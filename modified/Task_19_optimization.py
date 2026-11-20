import numpy as np
from scipy.optimize import minimize
# Modified: Higher required capacity (1,850 units), additional maximum power-draw
# constraint (<= 140 kW), and upper bound of 12 units per server type
def cost(z):
x, y = z
return 12.0 * x + 18.0 * y
constraints = [
{"type": "ineq", "fun": lambda z: 100.0 * z[0] + 170.0 * z[1] - 1850.0}, # Min
capacity
{"type": "ineq", "fun": lambda z: 140.0 - (8.0 * z[0] + 11.0 * z[1])} # Max
power
]
bounds = [(0, 12), (0, 12)]
sol = minimize(cost, x0=[6.0, 6.0], method="SLSQP", bounds=bounds,
constraints=constraints)
x, y = sol.x
print(f"Constrained Continuous Solution: A={x:.3f}, B={y:.3f} |
Cost=${sol.fun:.2f}")
print(f"Capacity: {100*x + 170*y:.1f} | Power: {8*x + 11*y:.1f} kW")