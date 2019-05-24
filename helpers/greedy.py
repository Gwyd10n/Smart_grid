#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
"""
Greedy algorithm for smart grid (from house to battery)
"""

from classes.cable import Cable
from helpers.helpers import get_man
from random import shuffle


def greedy(grid):
    """
    Do greedy algorithm, if greedy does not find a solution (not all houses are connected to a battery),
    do greedy again.
    :param grid: object
    :return: object
    """
    max_iterations = 1000
    for i in range(max_iterations):
        try:
            grid.clear_cables()
            greedy_grid = greedy_alg(grid)
            batt_cost = 0
            batteries = greedy_grid.get_batteries()
            for key in batteries:
                batt_cost += batteries[key].get_price()
            if greedy_grid.get_cost() > batt_cost:
                return greedy_grid
        except KeyError:
            pass
    exit("Greedy not solved")


def greedy_alg(grid):
    """
    Greedy algorithm, for each house, find closest battery with enough available capacity
    and add a cable from house to this battery
    :param grid: object
    :return: object
    """
    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)
    houses = grid.get_houses()
    hkeys = list(houses.keys())
    shuffle(hkeys)
    grid_max = grid.get_max()

    # For each house:
    for hkey in hkeys:
        best = grid_max[0] + grid_max[1]
        house = houses[hkey]
        to_batt = ''

        # Search for battery with enough capacity
        for bkey in bkeys:
            battery = batteries[bkey]
            curr_manh = get_man(house.get_coord(), battery.get_coord())
            h_out = house.get_max()
            b_cap = battery.get_cap()

            if curr_manh < best and h_out <= b_cap:
                best = curr_manh
                to_batt = bkey

        # Add cable from house to battery
        batteries[to_batt].red_cap(house.get_max())
        cable = Cable(house.get_id())
        cable.add_batt(to_batt)
        cable.add_route(house.get_coord(), batteries[to_batt].get_coord())
        grid.add_cable(cable)

    return grid
