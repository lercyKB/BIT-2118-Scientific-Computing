import numpy as np
# Modified: Expanded to a 3-server cluster (Type A, Type B, Type C) with
# CPU, RAM (GB), and Storage IOPS constraints, plus condition number check
A = np.array([
[4.0, 2.0, 6.0], # CPU cores per server
[8.0, 12.0, 16.0], # RAM (GB) per server
[2.0, 5.0, 4.0] # Network bandwidth (Gbps) per server
])
b = np.array([46.0, 132.0, 41.0])
solution = np.linalg.solve(A, b)
residual = b - A @ solution
cond_num = np.linalg.cond(A)
print(f"Active servers -> Type A: {solution[0]:.1f}, Type B: {solution[1]:.1f},
Type C: {solution[2]:.1f}")
print("Verification A @ solution:", A @ solution)
print(f"Residual norm: {np.linalg.norm(residual):.3e}")
print(f"Matrix condition number: {cond_num:.2f}")