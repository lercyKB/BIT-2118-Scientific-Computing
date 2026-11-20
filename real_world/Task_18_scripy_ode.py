import numpy as np
from scipy.integrate import solve_ivp
# Real-world case: Simulate an infectious outbreak in a population of N = 10,000
# using the coupled nonlinear SIR ODE system:
# dS/dt = -beta * S * I / N, dI/dt = beta * S * I / N - gamma * I, dR/dt = gamma
* I
# Assumptions: Transmission rate beta = 0.35 day^-1, recovery rate gamma = 0.10
day^-1
# (Basic reproduction number R0 = 3.5), initial infected I(0) = 15.
N = 10_000.0
beta = 0.35
gamma = 0.10
def sir_model(t, y):
S, I, R = y
dS = -beta * S * I / N
dI = beta * S * I / N - gamma * I
dR = gamma * I
return [dS, dI, dR]
t_days = np.linspace(0, 90, 91)
sol = solve_ivp(sir_model, (0, 90), [N - 15.0, 15.0, 0.0], t_eval=t_days, rtol=1e8)
peak_idx = np.argmax(sol.y[1])
print(f"Peak active infections: {sol.y[1, peak_idx]:.0f} people on Day
{sol.t[peak_idx]:.0f}")
print(f"Total recovered by Day 90: {sol.y[2, -1]:.0f} people")
print(f"Population conservation check: {np.sum(sol.y[:, -1]):.2f} (exact N=
{N:.0f})")