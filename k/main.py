import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generating synthetic dataset
data, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Initialize the model and predict cluster labels
kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
labels = kmeans.fit_predict(data)

# Plotting the clustered data
plt.figure(figsize=(8, 5))

clusters = []
for i in range(3):
    # Extract cluster points for cluster `i`
    cluster_points = data[labels==i]
    clusters.append(cluster_points)
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {i}", alpha=0.7)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering on Synthetic Data")
plt.legend()
plt.show()