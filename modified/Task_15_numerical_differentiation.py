import numpy as np
# Modified: Finer sampling interval (dt = 0.5 s) over 6 seconds, plus second-order
# numerical differentiation to estimate instantaneous vehicle acceleration (m/s^2)
time = np.arange(0.0, 6.5, 0.5)
# Position governed by x(t) = 4.5*t + 0.35*t^2
position = 4.5 * time + 0.35 * (time ** 2)
speed = np.gradient(position, time)
acceleration = np.gradient(speed, time)
for t, x, v, a in zip(time[::2], position[::2], speed[::2], acceleration[::2]):
print(f"t={t:3.1f}s | pos={x:5.2f}m | speed={v:5.2f} m/s | accel={a:4.2f}
m/s^2")