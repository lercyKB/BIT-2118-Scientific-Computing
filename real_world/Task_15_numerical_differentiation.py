import numpy as np
# Real-world case: Monitor lithium-ion battery pack temperature every 15 seconds
# and compute dT/dt (deg C/min) using central differences to trigger safety
cooling.
# Assumptions: Threshold alert triggers if dT/dt exceeds 2.5 C/min.
time_min = np.array([0.0, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50])
temp_c = np.array([28.0, 28.4, 29.0, 29.9, 31.1, 32.6, 34.4])
dT_dt = np.zeros_like(temp_c)
dT_dt[0] = (temp_c[1] - temp_c[0]) / (time_min[1] - time_min[0])
for i in range(1, len(time_min) - 1):
dT_dt[i] = (temp_c[i + 1] - temp_c[i - 1]) / (time_min[i + 1] - time_min[i -
1])
dT_dt[-1] = (temp_c[-1] - temp_c[-2]) / (time_min[-1] - time_min[-2])
for t, temp, rate in zip(time_min, temp_c, dT_dt):
status = "ALERT: High Heating Rate" if rate > 2.5 else "Normal"
print(f"t={t:4.2f} min | T={temp:4.1f} C | dT/dt={rate:4.2f} C/min [{status}]")