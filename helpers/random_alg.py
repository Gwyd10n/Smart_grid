#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
"""
Random 'algorithm' for smart grid
"""

from classes.cable import Cable
from random import shuffle


def random(grid):
    """
    Do random algorithm, if random does not find a solution (not all houses are connected to a battery),
    do random again.
    :param grid: object
    :return: object
    """
    max_iterations = 1000
    for i in range(max_iterations):
        try:
            grid.clear_cables()
            rand_grid = random_grid(grid)
            return rand_grid
        except KeyError:
            print(f"grid not solved, trying again for the {i}th time")
    print("no solution found")


def random_grid(grid):
    """
    Connect each house to a random battery
    :param grid:
    :return:
    """

    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)

    houses = grid.get_houses()
    hkeys = list(houses.keys())
    shuffle(hkeys)

    j = 0
    for i in range(len(hkeys)):
        if batteries[bkeys[j]].get_cap() > houses[hkeys[i]].get_max():
            batteries[bkeys[j]].red_cap(houses[hkeys[i]].get_max())
            cable = Cable(houses[hkeys[i]].get_id())
            cable.add_batt(batteries[bkeys[j]].get_id())
            cable.add_route(houses[hkeys[i]].get_coord(), batteries[bkeys[j]].get_coord())
            grid.add_cable(cable)
            i += 1

        else:
            i -= 1
            j += 1
            if j >= len(bkeys):
                j = 0
    return grid
