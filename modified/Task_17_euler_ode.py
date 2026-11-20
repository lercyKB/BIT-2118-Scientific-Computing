import numpy as np
# Modified: Step-size convergence study comparing h = 1.0, 0.25, and 0.05 minutes
# with higher cooling coefficient k = 0.18 min^-1
T_ambient = 22.0
T_initial = 95.0
k = 0.18
end_time = 30.0
exact_final = T_ambient + (T_initial - T_ambient) * np.exp(-k * end_time)
print(f"Analytical temperature at t=30 min: {exact_final:.6f} C\n")
for h in [1.0, 0.25, 0.05]:
t = np.arange(0, end_time + h, h)
T = np.zeros_like(t)
T[0] = T_initial
for i in range(len(t) - 1):
T[i + 1] = T[i] + h * (-k * (T[i] - T_ambient))
err = abs(T[-1] - exact_final)
print(f"Step h={h:4.2f} min -> Euler T(30)={T[-1]:.6f} C | Abs Error={err:.6f}
C")