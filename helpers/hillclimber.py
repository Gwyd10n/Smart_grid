from copy import deepcopy
from random import shuffle


def hillclimber(grid, n):
    # Get cable, house and battery dicts
    cables = grid.get_cables()
    batteries = grid.get_batteries()
    houses = grid.get_houses()
    # Get keys from the cable dictionary
    us_ckeys = list(cables.keys())
    ckeys = []

    for bkey in batteries:
        group = []
        for ckey in us_ckeys:
            if cables[ckey].get_batt() == bkey:
                group.append(ckey)
        ckeys.append(group)

    for i in range(n):
        score = grid.tot_len()
        shuffle(ckeys)
        shuffle(ckeys[0])
        shuffle(ckeys[1])

        orgA = cables[ckeys[0][0]]
        orgB = cables[ckeys[1][0]]
        newA = deepcopy(orgA)
        newB = deepcopy(orgB)

        houseA = houses[orgA.get_id()]
        houseB = houses[orgB.get_id()]

        battA = batteries[orgA.get_batt()]
        battB = batteries[orgB.get_batt()]

        newA.change_route(houseA.get_coord(), battB.get_coord())
        newA.add_batt(battB.get_id())
        newB.change_route(houseB.get_coord(), battA.get_coord())
        newB.add_batt(battA.get_id())

        new_score = score - (orgA.get_length() + orgB.get_length()) + (newA.get_length() + newB.get_length())

        if score > new_score:
            grid.rem_cable(orgA.get_id())
            grid.rem_cable(orgB.get_id())
            grid.add_cable(newA)
            grid.add_cable(newB)

        print('iteration:', i, 'best:', score, 'current:', new_score)

    return grid
