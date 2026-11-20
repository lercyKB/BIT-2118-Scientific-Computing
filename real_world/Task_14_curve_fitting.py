import numpy as np
from scipy.optimize import curve_fit
# Real-world case: Estimate elimination rate constant (k_e) and initial plasma
# concentration (C0) from clinical blood samples using C(t) = C0 * exp(-k_e * t).
# Assumptions: First-order single-compartment elimination kinetics.
time_hr = np.array([0.5, 1.0, 2.0, 4.0, 6.0, 8.0, 12.0], dtype=float)
conc_mg_L = np.array([44.2, 39.5, 31.1, 19.8, 12.4, 7.9, 3.1], dtype=float)
def pk_decay(t, C0, ke):
return C0 * np.exp(-ke * t)
params, pcov = curve_fit(pk_decay, time_hr, conc_mg_L, p0=[50.0, 0.2])
C0_fit, ke_fit = params
half_life = np.log(2.0) / ke_fit
rmse = np.sqrt(np.mean((conc_mg_L - pk_decay(time_hr, C0_fit, ke_fit)) ** 2))
print(f"Estimated C0: {C0_fit:.2f} mg/L")
print(f"Elimination rate constant k_e: {ke_fit:.4f} hr^-1")
print(f"Biological half-life (t_1/2): {half_life:.2f} hours")
print(f"Fit RMSE: {rmse:.3f} mg/L")