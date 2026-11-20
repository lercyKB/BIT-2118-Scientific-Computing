import numpy as np
# Real-world case: Ecological age-structured wildlife population model (3 age
classes:
# Juveniles, Sub-adults, Adults) using a Leslie matrix L.
# Assumptions: Fecundity rates = [0.0, 1.1, 2.4]; survival rates = [0.55, 0.70].
L = np.array([
[0.0, 1.1, 2.4],
[0.55, 0.0, 0.0],
[0.0, 0.70, 0.0]
])
eigvals, eigvecs = np.linalg.eig(L)
dom_idx = np.argmax(np.abs(eigvals))
growth_rate = np.real(eigvals[dom_idx])
stable_age_dist = np.abs(np.real(eigvecs[:, dom_idx]))
stable_age_dist /= stable_age_dist.sum()
print(f"Asymptotic population growth factor (lambda_1): {growth_rate:.4f}")
print("Status:", "Growing population" if growth_rate > 1.0 else "Declining
population")
print(f"Stable age distribution (Juv, Sub, Adult): {np.round(stable_age_dist * 100,
2)} %")