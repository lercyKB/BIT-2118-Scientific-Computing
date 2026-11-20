import numpy as np
from scipy.interpolate import interp1d, CubicSpline
# Real-world case: A survey drone records GPS altitude at irregular time stamps
# (seconds) due to telemetry packet drops. Reconstruct a smooth 1-Hz flight
profile.
# Assumptions: Continuous vertical motion with smooth acceleration (C2 continuity).
t_telemetry = np.array([0.0, 4.0, 9.0, 15.0, 22.0, 30.0])
altitude_m = np.array([0.0, 18.5, 42.0, 55.0, 53.5, 30.0])
alt_linear = interp1d(t_telemetry, altitude_m, kind="linear")
alt_spline = CubicSpline(t_telemetry, altitude_m)
t_1hz = np.arange(0.0, 30.5, 1.0)
profile_spline = alt_spline(t_1hz)
print(f"Reconstructed peak altitude (Spline): {np.max(profile_spline):.2f} m at t=
{t_1hz[np.argmax(profile_spline)]:.0f}s")
print(f"Altitude at t=12s -> Linear: {float(alt_linear(12.0)):.2f} m vs Spline:
{float(alt_spline(12.0)):.2f} m")