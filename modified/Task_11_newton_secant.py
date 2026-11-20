from scipy.optimize import root_scalar
# Modified: Larger capital outlay (-25,000) over 5 years with higher late inflows
# and comparison of iteration counts between Newton-Raphson and Secant
cash_flows = [-25000, 5000, 6500, 8000, 9500, 7000]
def npv(r):
return sum(cf / ((1.0 + r) ** t) for t, cf in enumerate(cash_flows))
def d_npv(r):
return sum(-t * cf / ((1.0 + r) ** (t + 1)) for t, cf in enumerate(cash_flows)
if t > 0)
newton = root_scalar(npv, fprime=d_npv, x0=0.12, method="newton", xtol=1e-14)
secant = root_scalar(npv, x0=0.08, x1=0.18, method="secant", xtol=1e-14)
print(f"Modified IRR (Newton): {newton.root:.6%} in {newton.iterations}
iterations")
print(f"Modified IRR (Secant): {secant.root:.6%} in {secant.iterations}
iterations")
print(f"Residual NPV: {npv(newton.root):.3e}")