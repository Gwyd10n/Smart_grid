from classes.Cable import Cable

def kmeans(grid):
    coordinates = []
    # Shuffle the list with battery keys
    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    print(bkeys)
