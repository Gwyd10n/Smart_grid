from copy import deepcopy
import numpy as np
from helpers.helpers import get_man, move


def kmeans(grid):
    """
    K-Mean algorithm that takes coordinates and constant k and returns
    k centers.
    """
    houses = grid.get_houses()

    # Set lists for x and y and coordinates
    list_x = []
    list_y = []
    list = []

    # Append the coordinates to the lists
    for hkey in houses:
        x_house = houses[hkey].get_coord()[0]
        y_house = houses[hkey].get_coord()[1]
        list_x.append(x_house)
        list_y.append(y_house)
        coords_houses = houses[hkey].get_coord()
        list.append(coords_houses)

    # Number of clusters
    k = 5

    list_centres = []
    # X and Y random centroids
    Centroid_x = np.random.randint(min(list_x), max(list_x), size=k)
    Centroid_y = np.random.randint(min(list_y), max(list_y), size=k)

    # Append X and Y to list
    for i in range(k):
        list_centres.append([Centroid_x[i], Centroid_y[i]])

    # Store the value of centroids when it updates
    list_centres = np.matrix(list_centres)
    C_old = np.zeros(list_centres.shape)

    # Distance between new centroids and old centroids
    error = np.sum(get_man(list_centres, C_old))

    # Run till error is zero
    while error > 0:
        assigned_clusters = [[], [], [], [], []]
        # Connect each value to its closest cluster
        for i in range(len(list)):
            distances = np.sum(np.abs(list_centres - list[i]), axis=1)
            cluster = np.argmin(distances)
            assigned_clusters[cluster].append(list[i])
        # Store the old values
        C_old = deepcopy(list_centres)
        # Find new centres y taking the average value
        for i in range(len(assigned_clusters)):
            if len(assigned_clusters[i]):
                list_centres[i] = np.mean(assigned_clusters[i], axis=0)
            else:
                list_centres[i] = C_old[i]

        error = np.sum(get_man(list_centres, C_old))

    # Move the batteries to new coordinates
    move(grid, list_centres.tolist())
