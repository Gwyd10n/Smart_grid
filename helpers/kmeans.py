from sklearn.cluster import KMeans


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

def kmeans_algorithm(grid):
    """
    Looking for locations for the batteries where the distance
    between battery and house is the lowest
    """
