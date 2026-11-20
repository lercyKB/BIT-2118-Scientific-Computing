import numpy as np
# Real-world case: Compute end-effector coordinates of a 2-link planar robotic arm
# using homogeneous transformation matrices (3x3 rotation + translation).
# Assumptions: Link 1 length L1 = 1.2 m at theta1 = 30 deg;
# Link 2 length L2 = 0.8 m at relative angle theta2 = 45 deg.
L1, L2 = 1.2, 0.8
theta1 = np.deg2rad(30)
theta2 = np.deg2rad(45)
def homogeneous_transform(theta, length):
return np.array([
[np.cos(theta), -np.sin(theta), length * np.cos(theta)],
[np.sin(theta), np.cos(theta), length * np.sin(theta)],
[0.0, 0.0, 1.0]
])
T1 = homogeneous_transform(theta1, L1)
T2 = homogeneous_transform(theta2, L2)
# Composite transformation from base frame to end-effector
T_total = T1 @ T2
origin_homogeneous = np.array([0.0, 0.0, 1.0])
end_effector = T_total @ origin_homogeneous
print("Joint 1 position (m):", np.round(T1[:2, 2], 4))
print("End-effector position (x, y) in meters:", np.round(end_effector[:2], 4))
print("Transformation determinant (rigid body = 1.0):", np.linalg.det(T_total))