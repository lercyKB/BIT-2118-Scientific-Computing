import numpy as np
# Real-world case: Calculating short-range GPS distance between two nearby
# survey markers (10 meters apart) using standard cosine law vs Haversine formula.
# Assumptions: Spherical Earth radius R = 6,371,000 m; coordinates in radians.
R = 6_371_000.0
lat1, lon1 = np.deg2rad(-1.10250000), np.deg2rad(37.01440000) # Thika reference
lat2, lon2 = np.deg2rad(-1.10258993), np.deg2rad(37.01440000) # ~10 m south
# Unstable Spherical Law of Cosines for very small angular separation
cos_angle = np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(lon2
- lon1)
dist_law_of_cosines = R * np.arccos(np.clip(cos_angle, -1.0, 1.0))
# Numerically stable Haversine formulation (avoids 1 - cos(theta) cancellation)
dlat = lat2 - lat1
dlon = lon2 - lon1
a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0)**2
dist_haversine = 2.0 * R * np.arcsin(np.sqrt(a))
abs_diff = abs(dist_haversine - dist_law_of_cosines)
print(f"Law of Cosines distance: {dist_law_of_cosines:.6f} m")
print(f"Haversine distance: {dist_haversine:.6f} m")
print(f"Numerical discrepancy: {abs_diff:.6f} m")