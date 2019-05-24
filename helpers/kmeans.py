from sklearn.cluster import KMeans
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def kmeans(grid):
    coordinates = []

    houses = grid.get_houses()

    for hkey in houses:
        coordinate = houses[hkey].get_coord()
        coordinates.append(coordinate)
    kmeans = KMeans(n_clusters=5, random_state=3)
    kmeans.fit(coordinates)
    centers = kmeans.cluster_centers_
    centers = centers.astype(int)


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def kmeans_algorithm(grid):
    """
    K-Mean algorithm that takes coordinates and constant k and returns
    k centers.
    """
    houses = grid.get_houses()

    # Set lists for x and y and coordinates
    list_x = []
    list_y = []
    list = []
    for hkey in houses:
        x_house = houses[hkey].get_coord()[0]
        y_house = houses[hkey].get_coord()[1]
        list_x.append(x_house)
        list_y.append(y_house)
    # X = np.array(zip(list_x, list_y))
        coords_houses = houses[hkey].get_coord()
        list.append(coords_houses)
        # coord_houses = np.array(list(x_house, y_house))

    # Number of clusters
    k = 5

    list_centres = []
    # X and Y random centroids
    Centroid_x = np.random.randint(0, max(list_x), size=k)
    Centroid_y = np.random.randint(0, max(list_y), size=k)

    # Append X and Y to list
    for i in range(len(Centroid_x)):
        list_centres.append([Centroid_x[i], Centroid_y[i]])
    #
    # print(list_centres)

    # Plot the centres
    plt.scatter(list_x, list_y, marker="^", c='black', s=7)
    plt.scatter(Centroid_x, Centroid_y, marker="*", s=200, c="g")
    plt.title("Grid with houses")
    plt.xlabel("X-coordinates")
    plt.ylabel("Y-coordinates")

    # Store the value of centroids when it updates
    C_old = np.zeros(5)
    clusters = np.zeros(len(list))

    # Distance between new centroids and old centroids
    error = dist(list_centres, C_old)

    # Run till error is zero
    while error > 0:
        # Connect each value to its closest cluster
        for i in range(len(list)):
            distances = dist(list[i], list_centres)
            cluster = np.argmin(distances)
            clusters[i] = cluster

        # Store the old values
        C_old = deepcopy(list_centres)
        # Find new centres y taking the average value
        for i in range(k):
            points = [X[j] for j in range(len(list_centres)) if clusters[j] == i]
            [i] = np.mean(points, axis=0)
        error = dist(list_centres, C_old)
