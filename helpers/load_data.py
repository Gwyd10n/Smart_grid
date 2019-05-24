#!/usr/bin/env python
# Gwydion Oostvogel, Jelle Westerbos, Sophie Schubert
"""
Functions for loading data.
"""

import os
import csv
import re
from classes.grid import Grid
from classes.battery import Battery
from classes.house import House


GRID = {}


def create_grid(grid_id, x, y, version):
    """
    Create grid with given values, add batteries and houses.
    :param id: int
    :param x: int
    :param y: int
    :return: dictionary
    """
    GRID[grid_id] = Grid(grid_id, x, y)
    load_batteries(grid_id, version)
    load_houses(grid_id, version)
    return GRID[grid_id]


def load_batteries(id, version):
    """
    Get battery info from text file and add batteries to grid.
    :param id: int
    :param version: int
    :return: none
    """
    path = os.path.dirname(__file__).replace("helpers", f"data\\wijk{version}_batterijen.txt")
    # Open file
    with open(path, 'r') as b_file:
        batt_nr = 0
        # Iterate over lines in file
        for line in b_file:
            # Clean input
            line = list(filter(None, re.sub('[][\n \t]', ',', line).split(',')))
            # Skip first line.
            if "pos" in line:
                continue
            # Add battery to grid
            batt_id = f"B{batt_nr}"
            battery = Battery(batt_id, int(line[0]), int(line[1]), float(line[2]))
            GRID[id].add_battery(battery)
            batt_nr += 1
    # Close file
    b_file.close()


def load_houses(id, version):
    """
    Get house values from csv file and add houses to grid.
    :param id: int
    :param version: int
    :return: none
    """
    path = os.path.dirname(__file__).replace("helpers", f"data\\wijk{version}_huizen.csv")
    # Open file
    with open(path, 'r') as h_file:
        house_nr = 0
        # Read file
        houses = csv.reader(h_file)
        # Iterate over lines in file
        for house in houses:
            # Skip first line
            if 'x' in house:
                continue
            # Add house to grid.
            house_id = f"H{house_nr}"
            GRID[id].add_house(House(house_id, int(house[0]), int(house[1]), float(house[2])))
            house_nr += 1
    # Close file
    h_file.close()
