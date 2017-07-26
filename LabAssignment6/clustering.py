import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

X = np.array([[1,1],[1.1,1.1],[3,3],[4,4],[3,3.5], [3.5,4]])
plt.scatter(X[:,0], X[:,1], s=50)

linkage_matrix = linkage(X, "single")
dendogram = dendrogram(linkage_matrix, truncate_mode='none')
plt.title("Hierarchical clustering")
plt.show()