import numpy as np
# Real-world case: Hourly solar panel power output (kW) over 24 hours
# Assumptions: 10 kW peak rooftop PV system, 1-hour sampling intervals,
# zero generation overnight (hours 0-5 and 19-23).
hourly_power_kw = np.array([
0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.4, 1.8, 3.9, 6.1, 7.8, 8.9,
9.4, 9.1, 8.2, 6.7, 4.5, 2.1,
0.5, 0.0, 0.0, 0.0, 0.0, 0.0
])
# Vectorized conversion from power (kW) to energy (kWh) per 1-hour slot
# and revenue calculation at a feed-in tariff of 0.14 USD/kWh
tariff_usd = 0.14
hourly_energy_kwh = hourly_power_kw * 1.0
total_energy_kwh = np.sum(hourly_energy_kwh)
peak_power_kw = np.max(hourly_power_kw)
active_hours = hourly_power_kw[hourly_power_kw > 0]
mean_active_kw = np.mean(active_hours)
daily_revenue = total_energy_kwh * tariff_usd
print(f"Total daily energy generated: {total_energy_kwh:.2f} kWh")
print(f"Peak solar generation: {peak_power_kw:.2f} kW")
print(f"Mean power during daylight hours: {mean_active_kw:.2f} kW")
print(f"Estimated daily feed-in revenue: ${daily_revenue:.2f}")