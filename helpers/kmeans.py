def kmeans(grid):
    coordinates = []
    # Shuffle the list with battery keys
    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    print(bkeys)

    for bkey in bkeys:
        coordinates.append(batteries[bkey].get_coord())

    print(coordinates)
