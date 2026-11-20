import numpy as np
from scipy.integrate import simpson
# Real-world case: Hydrological stream gauging across a 12-meter wide river
channel.
# Depth (m) and flow velocity (m/s) are measured every 2 meters from bank to bank.
# Total discharge Q = integral( depth(x) * velocity(x) dx ) in m^3/s.
width_m = np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0])
depth_m = np.array([0.0, 1.1, 2.3, 2.8, 2.1, 0.9, 0.0])
velocity_ms = np.array([0.0, 0.45, 0.82, 0.95, 0.76, 0.38, 0.0])
unit_discharge = depth_m * velocity_ms # m^2/s at each vertical station
Q_trap = np.trapezoid(unit_discharge, width_m)
Q_simp = simpson(unit_discharge, x=width_m)
print(f"River discharge (Trapezoidal): {Q_trap:.3f} m^3/s")
print(f"River discharge (Simpson's): {Q_simp:.3f} m^3/s")
print(f"Daily water volume (Simpson): {Q_simp * 86400:,.0f} m^3/day")