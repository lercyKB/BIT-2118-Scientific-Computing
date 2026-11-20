import numpy as np
from scipy.integrate import solve_ivp
# Modified: Higher supply voltage (12 V), faster RC time constant (tau = 0.4 s),
# and square-wave pulsed input voltage to test adaptive step-size handling
Vs_peak = 12.0
R = 800.0
C = 0.0005 # tau = R*C = 0.4 s
V0 = 0.0
def pulsed_rc(t, V):
# Supply switches ON (12V) for t < 2.0s, then OFF (0V) for t >= 2.0s
(discharge)
Vs = Vs_peak if t < 2.0 else 0.0
return [(Vs - V[0]) / (R * C)]
t_eval = np.linspace(0, 4, 401)
sol = solve_ivp(pulsed_rc, (0, 4), [V0], t_eval=t_eval, method="RK45", rtol=1e-9,
atol=1e-11)
v_at_2s = sol.y[0, 200]
v_at_4s = sol.y[0, -1]
print(f"Peak voltage at t=2.0 s (end of charge): {v_at_2s:.4f} V")
print(f"Voltage at t=4.0 s (after discharge): {v_at_4s:.4f} V")
print(f"Total right-hand-side evaluations: {sol.nfev}")