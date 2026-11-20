import numpy as np
from scipy.optimize import root
# Modified: Ellipse (x^2 / 9 + y^2 / 4 = 1) intersecting a shifted parabola (y =
0.5*x^2 - 1.5)
# Testing four initial guesses to capture symmetric intersection branches
def modified_system(z):
x, y = z
return [
(x**2) / 9.0 + (y**2) / 4.0 - 1.0,
y - (0.5 * x**2 - 1.5)
]
guesses = ([2.0, 1.0], [-2.0, 1.0], [1.5, -1.0], [-1.5, -1.0])
for g in guesses:
sol = root(modified_system, g, method="hybr")
print(f"Guess {g} -> Root: {np.round(sol.x, 6)} | Residual norm:
{np.linalg.norm(sol.fun):.2e}")