import numpy as np
# Real-world case: Solve for steady-state nodal voltages (V1..V4) in a resistive
# microgrid distribution bus with generator slack boundaries (V0=400 V, V5=380 V).
# Assumptions: Conductance matrix is strictly diagonally dominant due to shunt
loads.
G = np.array([
[ 5.2, -2.0, 0.0, 0.0],
[-2.0, 6.1, -2.5, 0.0],
[ 0.0, -2.5, 5.8, -1.8],
[ 0.0, 0.0, -1.8, 4.9]
])
I_inj = np.array([800.0, -45.0, -60.0, 684.0]) # Boundary currents minus load draw
x = np.full(4, 390.0) # Initial flat-start voltage guess (390 V)
tol = 1e-9
for step in range(1, 200):
old = x.copy()
for i in range(4):
x[i] = (I_inj[i] - G[i, :i] @ x[:i] - G[i, i+1:] @ old[i+1:]) / G[i, i]
if np.linalg.norm(x - old, ord=np.inf) < tol:
print(f"Bus voltages converged in {step} Gauss-Seidel iterations:")
for idx, v in enumerate(x, start=1):
print(f" Bus {idx}: {v:.4f} V")
break