import numpy as np
# Modified: Pentagonal polygon vertices, 60-degree rotation, anisotropic scaling
# (3.0x on x-axis, 0.5x on y-axis), and inverse recovery verification
points = np.array([
[0.0, 0.0],
[2.0, 0.0],
[2.5, 1.5],
[1.0, 2.5],
[-0.5, 1.5]
])
angle = np.deg2rad(60)
rotation = np.array([
[np.cos(angle), -np.sin(angle)],
[np.sin(angle), np.cos(angle)]
])
scale = np.array([
[3.0, 0.0],
[0.0, 0.5]
])
transformation = rotation @ scale
transformed_points = points @ transformation.T
# Recover original coordinates using matrix inverse
inv_transform = np.linalg.inv(transformation)
recovered_points = transformed_points @ inv_transform.T
print("Modified Transformation Matrix:\n", np.round(transformation, 4))
print("Transformed Pentagonal Points:\n", np.round(transformed_points, 4))
print("Determinant (Area Scale Factor):", np.linalg.det(transformation))
print("Max Reconstruction Error:", np.max(np.abs(points - recovered_points)))