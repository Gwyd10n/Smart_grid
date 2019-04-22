#!/usr/bin/env python
# District class for smart grid
# Gwydion Oostvogel, Jelle Westerbos, Sophie Schubert

import csv
import sys
import re
from Classes.Grid import Grid
from Classes.Battery import Battery
from Classes.House import House
# from Classes.Cable import Cable


GRIDS = {}


def main():
    # Check for correct number of arguments.
    if len(sys.argv) != 2:
        print("Usage: Python Application0.py <version>")
        sys.exit(1)

    # Create grid
    create_grid(0, 500, 500)
    # Check
    print(GRIDS[0])


def create_grid(id, x, y):
    """
    Create grid with given values, add batteries and houses.
    :param id: int
    :param x: int
    :param y: int
    :return: none
    """
    GRIDS[id] = Grid(id, x, y)
    version = sys.argv[1]
    load_batteries(0, version)
    load_houses(0, version)


def load_batteries(id, version):
    """
    Get battery info from text file and add batteries to grid.
    :param id: int
    :param version: int
    :return: none
    """
    # Open file
    with open(f"Huizen&Batterijen/wijk{version}_batterijen.txt", 'r') as b_file:
        batt_id = 0

        # Iterate over lines in file
        for line in b_file:
            # Clean input
            line = list(filter(None, re.sub('[][\n \t]', ',', line).split(',')))
            # Skip first line.
            if "pos" in line:
                continue
            # Add battery to grid
            GRIDS[id].add_battery(Battery(batt_id, int(line[0]), int(line[1]), float(line[2])), batt_id)
            batt_id += 1
    # Close file
    b_file.close()


def load_houses(id, version):
    """
    Get house values from csv file and add houses to grid.
    :param id: int
    :param version: int
    :return: none
    """
    # Open file
    with open(f"Huizen&Batterijen/wijk{version}_huizen.csv", 'r') as h_file:
        house_id = 0
        # Read file
        houses = csv.reader(h_file)
        # Iterate over lines in file
        for house in houses:
            # Skip first line
            if 'x' in house:
                continue
            # Add house to grid.
            GRIDS[id].add_house(House(house_id, int(house[0]), int(house[1]), float(house[2])), house_id)
            house_id += 1
    # Close file
    h_file.close()


if __name__ == "__main__":
    main()
