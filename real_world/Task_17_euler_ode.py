import numpy as np
# Real-world case: Simulate bacterial colony growth in a nutrient-limited
bioreactor
# governed by the logistic ODE: dP/dt = r * P * (1 - P / K).
# Assumptions: Intrinsic growth rate r = 0.45 hr^-1, carrying capacity K = 1000
mg/L,
# initial biomass P(0) = 25 mg/L, step size h = 0.1 hr over 15 hours.
r = 0.45
K = 1000.0
P0 = 25.0
h = 0.1
t = np.arange(0.0, 15.0 + h, h)
P = np.zeros_like(t)
P[0] = P0
for i in range(len(t) - 1):
P[i + 1] = P[i] + h * (r * P[i] * (1.0 - P[i] / K))
exact_P = K / (1.0 + ((K - P0) / P0) * np.exp(-r * t))
print(f"Euler biomass at 15 hr: {P[-1]:.2f} mg/L")
print(f"Exact biomass at 15 hr: {exact_P[-1]:.2f} mg/L")
print(f"Absolute error: {abs(P[-1] - exact_P[-1]):.4f} mg/L")