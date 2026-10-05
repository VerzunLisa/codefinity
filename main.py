import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generating synthetic dataset 
data, _ = make_blobs(n_samples=300, centers=3, cluster_std=2.0, random_state=42)

# Initialize the model and predict the labels
gmm = GaussianMixture(n_components=3, random_state=42)
labels = gmm.fit_predict(data)

# Plotting the clustered data 
plt.figure(figsize=(8, 5))

clusters = []
for i in range(3):
    # Extact the points belonging to the cluster `i`
    cluster_points = data[labels==i]
    clusters.append(cluster_points)
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {i}", alpha=0.7)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("GMM Clustering on Synthetic Data")
plt.legend()
plt.show()