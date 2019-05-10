#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert

from classes.Cable import Cable
from random import shuffle


def greedy(grid):
    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)
    houses = grid.get_houses()
    hkeys = list(houses.keys())
    shuffle(hkeys)
    grid_max = grid.get_max()

    for hkey in hkeys:
        best = grid_max[0] + grid_max[1]
        house = houses[hkey]
        to_batt = ""

        for bkey in bkeys:
            battery = batteries[bkey]
            curr_manh = get_man(house.get_coord(), battery.get_coord())
            h_out = house.get_max()
            b_cap = battery.get_cap()

            if curr_manh < best and h_out <= b_cap:
                best = curr_manh
                to_batt = bkey

        batteries[to_batt].red_cap(house.get_max())
        cable = Cable(house.get_id())
        cable.add_batt(batteries[to_batt].get_id)
        cable.add_route(house.get_coord(), batteries[to_batt].get_coord())
        grid.add_cable(cable)

    return grid


def get_man(coord_house, coord_battery):
    manhattan_dist = abs(coord_house[0] - coord_battery[0]) + abs(coord_house[1] - coord_battery[1])
    return manhattan_dist
