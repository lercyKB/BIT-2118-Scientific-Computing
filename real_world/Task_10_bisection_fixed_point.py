import numpy as np
from scipy.optimize import root_scalar
# Real-world case: Solve for equilibrium fractional conversion X in [0, 1] for a
# reversible exothermic reaction governed by K_eq(X) - X / ((1 - X)^2) = 0.
# Assumptions: Equilibrium constant K_eq = 3.5 at operating temperature.
K_eq = 3.5
def reaction_residual(X):
return X - K_eq * ((1.0 - X) ** 2)
sol = root_scalar(reaction_residual, bracket=[0.0, 0.99], method="bisect", xtol=1e12)
# Contractive fixed-point formulation: X = 1 - sqrt(X / K_eq)
X_fp = 0.5
for k in range(1, 150):
X_next = 1.0 - np.sqrt(X_fp / K_eq)
if abs(X_next - X_fp) < 1e-12:
X_fp = X_next
break
X_fp = X_next
print(f"Equilibrium conversion (Bisection): {sol.root:.6%}")
print(f"Equilibrium conversion (Fixed-Point): {X_fp:.6%} in {k} iterations")