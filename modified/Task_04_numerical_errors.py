import numpy as np
# Modified: Compare different decimal additions, tighter approximation of pi,
# and push x down to 1e-16 to expose total catastrophic cancellation
calculated = 0.7 + 0.1
expected = 0.8
print("0.7 + 0.1 =", repr(calculated))
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison (rtol=1e-15):", np.isclose(calculated, expected,
rtol=1e-15))
# Absolute and relative error using 355/113 approximation for pi
true_value = np.pi
approx_value = 355 / 113
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error (pi vs 355/113): {absolute_error:.12f}")
print(f"Relative error: {relative_error:.10%}")
# Catastrophic cancellation test down to machine epsilon
for x in [1e-6, 1e-10, 1e-14, 1e-16]:
direct = (np.sqrt(1 + x) - 1) / x
stable = 1 / (np.sqrt(1 + x) + 1)
print(f"x={x:.0e}: direct={direct:.15f}, stable={stable:.15f}")