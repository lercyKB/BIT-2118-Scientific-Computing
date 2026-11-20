import numpy as np
# Modified: Cold-front weather profile with 24 lower hourly readings (Celsius)
# Added standard deviation and diurnal temperature range metrics
temperatures_c = np.array([
10.2, 9.8, 9.4, 9.0, 9.3, 10.5,
12.8, 14.6, 16.2, 17.5, 18.4, 19.1,
19.5, 19.0, 18.2, 17.1, 15.8, 14.4,
13.1, 12.2, 11.5, 11.0, 10.6, 10.1
])
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)
std_temp = np.std(temperatures_c)
temp_range = max_temp - min_temp
# Vectorized conversion to Fahrenheit and Kelvin
temperatures_f = 1.8 * temperatures_c + 32
temperatures_k = temperatures_c + 273.15
print(f"Daily mean temperature: {mean_temp:.2f} C ({np.mean(temperatures_f):.2f}
F)")
print(f"Minimum temperature: {min_temp:.2f} C | Maximum: {max_temp:.2f} C")
print(f"Diurnal range: {temp_range:.2f} C | Std Dev: {std_temp:.2f} C")
print("First six Kelvin readings:", np.round(temperatures_k[:6], 2))