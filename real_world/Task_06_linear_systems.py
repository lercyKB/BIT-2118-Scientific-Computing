import numpy as np
# Real-world case: Solve for three mesh currents (I1, I2, I3 in Amperes) in a
# 3-loop resistive DC circuit using Kirchhoff's Voltage Law (R * I = V).
# Assumptions: Shared resistors between loops create off-diagonal negative terms.
# Loop 1: R1=10 ohm, shared R12=4 ohm, V1=24 V
# Loop 2: R2=12 ohm, shared R12=4 ohm, shared R23=3 ohm, V2=0 V
# Loop 3: R3=8 ohm, shared R23=3 ohm, V3=12 V
R_matrix = np.array([
[14.0, -4.0, 0.0],
[-4.0, 19.0, -3.0],
[ 0.0, -3.0, 11.0]
])
V_vector = np.array([24.0, 0.0, 12.0])
currents = np.linalg.solve(R_matrix, V_vector)
residual = V_vector - R_matrix @ currents
for idx, current in enumerate(currents, start=1):
print(f"Mesh Current I{idx}: {current:.4f} A")
print(f"KVL Residual Norm: {np.linalg.norm(residual):.3e} V")