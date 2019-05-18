from classes.Grid import Grid
from classes.Battery import Battery
from classes.House import House
from classes.Cable import Cable

def manhatten_distance(house, battery):

    coordinates_h = house.get_coord()
    coordinates_b = battery.get_coord()
    return abs(coordinates_h[0] - coordinates_b[0]) + abs(coordinates_h[1] - coordinates_b[1])


def save_csv(grid):
    """
    Saves grid to CSV file.
    :param grid: Object
    :return: int
    """
