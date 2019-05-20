#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert

from classes.Cable import Cable
from random import shuffle

def random(grid):
    max_iterations = 1000
    for i in range(max_iterations):
        try:
            grid.clear_cables()
            random_grid = random(grid)
            return random_grid
        except KeyError:
            print(f"grid not solved, trying again for the {i}th time")
    print("no solution found")


def random(grid):
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
            cable.add_batt(batteries[bkeys[j]].get_id)
            cable.add_route(houses[hkeys[i]].get_coord(), batteries[bkeys[j]].get_coord())
            grid.add_cable(cable)
            i += 1

        else:
            i -= 1
            j += 1
            if j >= len(bkeys):
                j = 0
    return grid
