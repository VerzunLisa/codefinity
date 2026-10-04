import scipy.spatial.distance as dist
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generating synthetic dataset
data, _ = make_blobs(n_samples=10, centers=3, cluster_std=1.0, random_state=42)

# Write your code below
distance_matrix = dist.pdist(data, metric='euclidean')
linkage_matrix = sch.linkage(distance_matrix, method='single')

# Plotting the dendrogram
plt.figure(figsize=(8, 5))
sch.dendrogram(linkage_matrix, labels=range(len(data)))
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.title("Hierarchical Clustering Dendrogram")
plt.show()