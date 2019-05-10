#!/usr/bin/env python
# Gwydion Oostvogel, Jelle Westerbos, Sophie Schubert

#####################
import Battery
import House

######################
import sys
from helpers.load_data import create_grid


def main():
    # Check for correct number of arguments.
    if len(sys.argv) != 2:
        print("Usage: Python Application.py <1, 2 or 3>")
        sys.exit(1)
    version = sys.argv[1]

    # Create grid
    grid = create_grid(0, 50, 50, version)
    # Check
    #######################
    batteries = grid.get_batteries()
    houses = grid.get_houses()
    # for battery in batteries:
    #     for house in houses:
    #         print(manhatten_distance(houses[house], batteries[battery]))

def manhatten_distance(house, battery):

    coordinates_h = house.get_coord()
    coordinates_b = battery.get_coord()
    length = abs(coordinates_h[0] - coordinates_b[0]) + abs(coordinates_h[1] - coordinates_b[1])

    return length

def connect(house, battery):
    """
    Connects the houses with batteries with capacity in mind
    """
    # Check whether battery hasnt enough capacity
    if battery.get_av() + house.get_max() < 0:
        return False
    else:
        battery.get_av() = battery.get_av() - house.get_max()

def disconnect(house, battery):
    return "TODO"


if __name__ == "__main__":
    main()
