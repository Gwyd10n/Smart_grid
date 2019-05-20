#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
from classes.Cable import Cable
from helpers.helpers import get_man
from random import shuffle


def greedy2(grid):
    greedy_alg_2(grid)

    # max_iterations = 10
    # for i in range(max_iterations):
    #     try:
    #         grid.clear_cables()
    #         return greedy_alg_2(grid)
    #     except KeyError:
    #         pass
    # exit("Greedy not solved")


def greedy_alg_2(grid):
    """
    This is a greedy algorithm which connects the closest house to the battery
    by looping through the batteries.
    """
    # Shuffle the list with battery keys
    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)

    # Shuffle the list with house keys
    houses = grid.get_houses()
    hkeys = list(houses.keys())

    for bkey in bkeys:
        conn_houses = []
        shuffle(hkeys)
        battery = batteries[bkey]
        b_cap = battery.get_cap()
        while 1:
            best = grid.get_max()[0] + grid.get_max()[1]
            conn_house = ''
            for hkey in hkeys:
                house = houses[hkey]
                curr_manh = get_man(house.get_coord(), battery.get_coord())
                h_out = house.get_max()


                if best >= curr_manh and b_cap >= h_out:
                    b_cap -= h_out
                    conn_house = hkey
                    best = curr_manh

            if conn_house == '':
                break
            else:
                conn_houses.append(conn_house)
                hkeys.remove(conn_house)

        # print(conn_houses)

        for house in conn_houses:
            house = houses[house]
            batteries[bkey].red_cap(house.get_max())
            cable = Cable(house.get_id())
            cable.add_batt(bkey)
            cable.add_route(house.get_coord(), batteries[bkey].get_coord())
            grid.add_cable(cable)
    print(grid)
    return grid
