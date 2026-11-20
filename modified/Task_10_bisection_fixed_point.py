import numpy as np
from scipy.optimize import root_scalar
# Modified: Higher ambient baseline (30 C), stronger exponential heat source
(18.0),
# wider bracket [25, 50], and stricter tolerance (1e-13)
def heat_balance_mod(T):
return T - 30.0 - 18.0 * np.exp(-T / 25.0)
sol_bisect = root_scalar(heat_balance_mod, bracket=[25, 50], method="bisect",
xtol=1e-13)
def g_mod(T):
return 30.0 + 18.0 * np.exp(-T / 25.0)
T = 35.0
iters = 0
while iters < 200:
T_next = g_mod(T)
iters += 1
if abs(T_next - T) < 1e-13:
T = T_next
break
T = T_next
print(f"Modified Bisection root: {sol_bisect.root:.8f} C (bisect evals:
{sol_bisect.function_calls})")
print(f"Modified Fixed-point root: {T:.8f} C (iterations: {iters})")