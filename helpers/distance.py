def manhatten_distance (x, y, n):

    coordinates_h = house.get_coord()
    coordinates_b = battery.get_coord()

    length = abs(coordinates_h[0] - coordinates_b[0]) + abs(coordinates_h[1] - coordinates_b[1])
