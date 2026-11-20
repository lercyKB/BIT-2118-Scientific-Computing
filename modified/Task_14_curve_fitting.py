import numpy as np
from scipy.optimize import curve_fit
# Modified: Higher load regime up to 500 users, plus comparison between
# a quadratic model and an exponential queuing saturation model
users = np.array([50, 100, 150, 200, 250, 300, 350, 400, 450], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305, 392, 505], dtype=float)
def quad_model(x, a, b, c):
return a * x**2 + b * x + c
def exp_model(x, a, b, c):
return a * np.exp(b * x) + c
p_quad, _ = curve_fit(quad_model, users, response_ms)
p_exp, _ = curve_fit(exp_model, users, response_ms, p0=[20.0, 0.006, 60.0])
rmse_quad = np.sqrt(np.mean((response_ms - quad_model(users, *p_quad)) ** 2))
rmse_exp = np.sqrt(np.mean((response_ms - exp_model(users, *p_exp)) ** 2))
print(f"Quadratic RMSE: {rmse_quad:.2f} ms | Pred at 500 users: {quad_model(500,
*p_quad):.2f} ms")
print(f"Exponential RMSE: {rmse_exp:.2f} ms | Pred at 500 users: {exp_model(500,
*p_exp):.2f} ms")