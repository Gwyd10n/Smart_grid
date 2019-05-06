from Grid import Grid
from Battery import Battery
from House import House
from Cable import Cable

def manhatten_distance (house, battery):

    coordinates_h = house.get_coord()
    coordinates_b = battery.get_coord()
    length = abs(coordinates_h[0] - coordinates_b[0]) + abs(coordinates_h[1] - coordinates_b[1])

    return length


if __name__ == "__main__":
    print(manhatten_distance(House.get_coord(), Battery.get_coord()))
