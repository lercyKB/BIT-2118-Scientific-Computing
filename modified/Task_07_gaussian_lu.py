import numpy as np
from scipy.linalg import lu_factor, lu_solve, lu
# Modified: 4x4 structural stiffness matrix, 4 load vectors, and explicit
# inspection of P, L, and U factors
A = np.array([
[ 6.0, -2.0, 0.0, 0.0],
[-2.0, 6.0, -2.0, 0.0],
[ 0.0, -2.0, 6.0, -2.0],
[ 0.0, 0.0, -2.0, 5.0]
])
load_cases = [
np.array([10.0, 20.0, 15.0, 5.0]),
np.array([25.0, 10.0, 10.0, 20.0]),
np.array([ 5.0, 5.0, 30.0, 15.0]),
np.array([12.0, 18.0, 12.0, 18.0])
]
P, L, U = lu(A)
lu_piv = lu_factor(A)
print("Upper triangular factor U:\n", np.round(U, 3))
for idx, b in enumerate(load_cases, start=1):
disp = lu_solve(lu_piv, b)
print(f"Load case {idx} displacements: {np.round(disp, 4)} | Residual:
{np.linalg.norm(b - A @ disp):.2e}")