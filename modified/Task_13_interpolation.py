import numpy as np
from scipy.interpolate import interp1d, CubicSpline
# Modified: Sharper midday thermal spike and 5-minute (1/12 hr) resampling grid,
# comparing natural vs clamped boundary conditions on CubicSpline
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([17.0, 19.5, 23.0, 27.5, 28.0, 24.5, 21.0])
linear = interp1d(hours, temperature, kind="linear")
cubic_not_a_knot = CubicSpline(hours, temperature, bc_type="not-a-knot")
cubic_natural = CubicSpline(hours, temperature, bc_type="natural")
five_min_grid = np.arange(8, 14 + 1/12, 1/12)
print(f"Total resampled points (5-min intervals): {len(five_min_grid)}")
for t_check in [10.5, 11.5, 12.25]:
print(
f"Time {t_check:5.2f}h -> Linear: {float(linear(t_check)):.2f} C | "
f"Cubic(not-a-knot): {float(cubic_not_a_knot(t_check)):.2f} C | "
f"Cubic(natural): {float(cubic_natural(t_check)):.2f} C"
)