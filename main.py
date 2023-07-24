import matplotlib.pyplot as plt
import pandas as pd
import random

data = pd.read_csv("Data.csv")
data = data.values.tolist()

def euclidean_distance(a, b):
    return (sum([(a[i] - b[i]) ** 2 for i in range(len(a))])) ** 0.5  # for sqrt

def k_means(data, k):
    centroids = random.sample(data, k) # For choosing of centeroids
    assignments = [0] * len(data)

    while True:
        # Assign points to the nearest centroid
        for i, point in enumerate(data):
            assignments[i] = min(range(k), key=lambda j: euclidean_distance(point, centroids[j]))

        # Calculate the mean of the points in each cluster and update the centroids
        new_centroids = [[0, 0] for _ in range(k)]
        counts = [0] * k

        for i, point in enumerate(data):
            for j in range(2):
                new_centroids[assignments[i]][j] += point[j]
            counts[assignments[i]] += 1

        for i in range(k):
            for j in range(2):
                new_centroids[i][j] /= counts[i]

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids, assignments

def total_within_cluster_sum_of_squares(data, centroids, assignments):
    total = 0
    for i, point in enumerate(data):
        total += euclidean_distance(point, centroids[assignments[i]]) ** 2
    return total

def elbow_method(data, max_k):
    wcss = []
    for k in range(1, max_k + 1):
        centroids, assignments = k_means(data, k)
        wcss.append(total_within_cluster_sum_of_squares(data, centroids, assignments))
    return wcss

def visualize_elbow_method(wcss):
    plt.plot(range(1, len(wcss) + 1), wcss, marker='o')
    plt.xlabel('K')
    plt.ylabel('WCSS')
    plt.title('Elbow Method')
    plt.show()

max_k = 5
wcss = elbow_method(data, max_k)
visualize_elbow_method(wcss)
