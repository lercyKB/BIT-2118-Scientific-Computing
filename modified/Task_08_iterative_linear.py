import numpy as np
# Modified: Stronger diagonal dominance (diagonal = 4.0) with internal heat sources
# and tighter tolerance (1e-11) to observe faster convergence rate
A = np.array([
[ 4., -1., 0., 0., 0.],
[-1., 4., -1., 0., 0.],
[ 0., -1., 4., -1., 0.],
[ 0., 0., -1., 4., -1.],
[ 0., 0., 0., -1., 4.]
])
b = np.array([150., 25., 25., 25., 40.])
def compare_solvers(A, b, tol=1e-11, max_iter=500):
D = np.diag(A)
R = A - np.diagflat(D)
x_j = np.zeros_like(b)
iter_j = 0
for k in range(1, max_iter + 1):
x_new = (b - R @ x_j) / D
if np.linalg.norm(x_new - x_j, ord=np.inf) < tol:
iter_j = k
x_j = x_new
break
x_j = x_new
x_gs = np.zeros_like(b)
iter_gs = 0
for k in range(1, max_iter + 1):
old = x_gs.copy()
for i in range(len(b)):
x_gs[i] = (b[i] - A[i, :i] @ x_gs[:i] - A[i, i+1:] @ old[i+1:]) / A[i,
i]
if np.linalg.norm(x_gs - old, ord=np.inf) < tol:
iter_gs = k
break
return x_j, iter_j, x_gs, iter_gs
xj, kj, xgs, kgs = compare_solvers(A, b)
print(f"Jacobi converged in {kj} iterations: {np.round(xj, 6)}")
print(f"Gauss-Seidel converged in {kgs} iterations: {np.round(xgs, 6)}")