import numpy as np
from scipy.optimize import minimize
# Real-world case: Formulate a minimum-cost fertilizer blend using Urea (N=46%,
P=0%)
# and DAP (N=18%, P=46%) to supply at least 92 kg Nitrogen and 46 kg Phosphorus per
hectare.
# Assumptions: Urea costs $0.65/kg, DAP costs $0.82/kg; non-negative quantities.
def blend_cost(weights):
urea_kg, dap_kg = weights
return 0.65 * urea_kg + 0.82 * dap_kg
nutrient_constraints = [
{"type": "ineq", "fun": lambda w: 0.46 * w[0] + 0.18 * w[1] - 92.0}, #
Nitrogen >= 92 kg
{"type": "ineq", "fun": lambda w: 0.46 * w[1] - 46.0} #
Phosphorus >= 46 kg
]
bounds = [(0, None), (0, None)]
res = minimize(blend_cost, x0=[100.0, 100.0], method="SLSQP", bounds=bounds,
constraints=nutrient_constraints)
u_opt, d_opt = res.x
print(f"Optimal Urea: {u_opt:.2f} kg/ha | Optimal DAP: {d_opt:.2f} kg/ha")
print(f"Minimum Fertilizer Cost: ${res.fun:.2f} / hectare")