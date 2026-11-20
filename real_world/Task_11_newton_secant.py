import numpy as np
from scipy.optimize import root_scalar
# Real-world case: Solve the implicit Colebrook-White equation for the DarcyWeisbach
# friction factor f in turbulent pipe flow:
# g(f) = 1/sqrt(f) + 2*log10( (eps/D)/3.7 + 2.51/(Re * sqrt(f)) ) = 0
# Assumptions: Relative roughness eps/D = 0.0005, Reynolds number Re = 1.5e5.
rel_roughness = 0.0005
Re = 1.5e5
def colebrook(f):
return 1.0 / np.sqrt(f) + 2.0 * np.log10(rel_roughness / 3.7 + 2.51 / (Re *
np.sqrt(f)))
def d_colebrook(f):
term = rel_roughness / 3.7 + 2.51 / (Re * np.sqrt(f))
d_term = -1.255 / (Re * (f ** 1.5))
return -0.5 * (f ** -1.5) + (2.0 / np.log(10.0)) * (d_term / term)
res_newton = root_scalar(colebrook, fprime=d_colebrook, x0=0.02, method="newton",
xtol=1e-12)
res_secant = root_scalar(colebrook, x0=0.015, x1=0.03, method="secant", xtol=1e-12)
print(f"Darcy friction factor (Newton): {res_newton.root:.8f}
({res_newton.iterations} iters)")
print(f"Darcy friction factor (Secant): {res_secant.root:.8f}
({res_secant.iterations} iters)")