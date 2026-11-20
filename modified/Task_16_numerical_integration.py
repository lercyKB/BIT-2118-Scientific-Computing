import numpy as np
from scipy.integrate import simpson
# Modified: Full 24-hour smart-meter profile sampled every 2 hours (13 points,
# even number of intervals) with sharper evening appliance peak
time_hours = np.arange(0, 25, 2, dtype=float)
power_kw = np.array([0.6, 0.5, 0.5, 0.9, 1.5, 1.3, 1.1, 1.2, 1.8, 2.7, 2.4, 1.4,
0.8])
energy_trap = np.trapezoid(power_kw, time_hours)
energy_simp = simpson(power_kw, x=time_hours)
bill_usd = energy_simp * 0.18 # $0.18 per kWh
print(f"24-hr Energy (Trapezoidal): {energy_trap:.4f} kWh")
print(f"24-hr Energy (Simpson's): {energy_simp:.4f} kWh")
print(f"Discrepancy: {abs(energy_simp - energy_trap):.4f} kWh")
print(f"Estimated daily utility cost: ${bill_usd:.2f}")