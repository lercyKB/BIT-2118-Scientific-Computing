import numpy as np
# Modified: 5-node asymmetric weighted citation/routing network
# Nodes: Server1, Server2, Server3, Server4, Server5
A = np.array([
[0., 2., 1., 0., 1.],
[2., 0., 2., 1., 0.],
[1., 2., 0., 2., 1.],
[0., 1., 2., 0., 2.],
[1., 0., 1., 2., 0.]
])
eigenvalues, eigenvectors = np.linalg.eig(A)
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()
nodes = ["Server1", "Server2", "Server3", "Server4", "Server5"]
print(f"All eigenvalues: {np.round(np.real(eigenvalues), 4)}")
print(f"Dominant eigenvalue (spectral radius): {dominant_value:.4f}")
for node, score in zip(nodes, centrality):
print(f" {node}: {score:.4f}")