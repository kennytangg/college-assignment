# K-Means Algorithm

#### 1. Placement of Centroids
After fitting K-Means, each cluster centroid represents the "average" image of all points assigned to that cluster.
When I visualize, most centroids show blurry but a little bit recognizable digit shapes (0-9), showing that k-means has group similar handwriting styles together.

#### 2. How Data Points Moved During Iterations
K-means start with random chosen centroids and then it iteratively update them to minimize the inertia (the sum of squared distances of each data point to its cluster center).​

In the first few iterations, inertia dropped sharply ( from 2,085,000+ to around 1,165,000), which shows that many data points changed their cluster assignments as the centroids adjusted positions.

Strict convergence was reached when assignments stabilized and the decrease in inertia became negligible, usually by iteration 10–23 in different initializations.

During early iterations, many data points were reassigned between clusters as centroids shifted. Data near boundaries (digits with similar handwriting) tended to move the most before clusters stabilized. Movement slowed until each data point was closest to its assigned centroid.

#### 3. Final Cluster Quality, Intuitive or Surprising?
- Cluster Quality:

Most digits were grouped intuitively, with clusters matching visible digit patterns.Some digits with similar shapes (like 1 and 7, or 3 and 5) were mixed, which is expected since clustering is unsupervised.

- Intuitive or Surprising?

The results are partly intuitive: centroids show digit prototypes, and clusters mostly reflect true digit classes. It is surprising how much overlap occurs for digits with similar features
