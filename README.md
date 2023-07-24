# Cluster-Analysis-Elbow-Method

## Introduction

This repository implements the elbow method to determine the optimal number of clusters (k) for a given dataset using the K-means clustering algorithm. The elbow method is a common technique to find the ideal value of k by plotting the total within-cluster sum of squares (WCSS) against different k values.

## Dataset

The dataset used for this project is available in the "Data.csv" file.

## Code Explanation

The code is written in Python and uses the following functions:

- `euclidean_distance(a, b)`: Calculates the Euclidean distance between two points `a` and `b`.
- `k_means(data, k)`: Implements the K-means clustering algorithm with `k` clusters.
- `total_within_cluster_sum_of_squares(data, centroids, assignments)`: Calculates the total within-cluster sum of squares (WCSS) for a given set of data points, centroids, and cluster assignments.
- `elbow_method(data, max_k)`: Uses the K-means algorithm to find WCSS for different values of `k` and returns a list of WCSS values.
- `visualize_elbow_method(wcss)`: Plots the WCSS values against different `k` values to visualize the elbow method.

## Usage

1. Clone the repository to your local machine.
2. Make sure you have Python and the required libraries installed (NumPy, Pandas, and Matplotlib).
3. Run the Python script `main.py`.
4. The script will output the optimal value of k and plot the elbow method graph.

## Screenshot

![image](https://github.com/SaadARazzaq/Cluster-Analysis-Elbow-Method/assets/123338307/06ba16d9-bb30-4903-9bbc-c2d1950bf28c)

## Results

After running the code, the elbow method graph will be displayed showing the WCSS values for different k values. The optimal number of clusters (k) can be identified at the "elbow point" in the graph where the rate of WCSS reduction starts to slow down.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open a pull request or submit an issue.

## Contact
For any questions or inquiries, you can reach me at sabdurrazzaq124@gmail.com.
