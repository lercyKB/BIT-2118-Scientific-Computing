import numpy as np
from scipy.linalg import lu_factor, lu_solve
# Real-world case: Linearized hydraulic conductance matrix G for a 4-junction
# municipal water pipe network. Pipe conductances remain fixed across the day,
# while hourly consumer demand vectors q(t) change every hour.
# Assumptions: Steady-state linearized flow G * h = q.
G = np.array([
[ 8.5, -3.0, -2.5, 0.0],
[-3.0, 9.0, -2.0, -2.0],
[-2.5, -2.0, 7.5, -1.5],
[ 0.0, -2.0, -1.5, 6.0]
])
hourly_demands = {
"06:00 Morning Peak": np.array([45.0, 60.0, 50.0, 35.0]),
"13:00 Midday": np.array([25.0, 30.0, 28.0, 20.0]),
"20:00 Evening Peak": np.array([50.0, 65.0, 55.0, 40.0])
}
# Pre-factor hydraulic network matrix once
factored_G = lu_factor(G)
for period, q in hourly_demands.items():
heads = lu_solve(factored_G, q)
print(f"{period} -> Nodal Pressure Heads (m): {np.round(heads, 2)}")