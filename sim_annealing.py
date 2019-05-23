from copy import deepcopy
from random import shuffle
import numpy as np
from helpers.hillclimber import hillclimber

from helpers.load_data import create_grid
from helpers.random_alg import random



def sim_ann(grid, n_alg):
    Ts = 100
    Te = 0

    score = grid.get_cost()
    accept = 0

    for i in range(n_alg):
        score = grid.get_cost()
        prob_grid = swap_one(deepcopy(grid))
        score_new = prob_grid.get_cost()

        if score >= score_new:
            accept = 1

        elif score < score_new:
            # linear cooling scheme
            accept = max(0, min(1, np.exp(-(score_new - score) / T)))

        if np.random.rand() < accept:
            grid = prob_grid

        T = Ts - i * (Ts - Te) / n_alg

    return grid

def swap_one(grid):
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

    # new_score = score - (orgA.get_length() + orgB.get_length()) + (newA.get_length() + newB.get_length())

    if battA.get_cap() > houseB.get_max() and battB.get_cap() > houseA.get_max():
        grid.rem_cable(orgA.get_id())
        grid.rem_cable(orgB.get_id())
        grid.add_cable(newA)
        grid.add_cable(newB)

    # print('iteration:', i, 'best:', score, 'current:', new_score)

    return grid


# def hillclimber(grid, n_alg):
#     """
#     bereken aantal opties, stop optie in lijst
#     geef elke optie een prob
#     kies optie met random.choose
#     maak van grid de gegeven optie
#     """
#
#     # Get cable, house and battery dicts
#     cables = grid.get_cables()
#     batteries = grid.get_batteries()
#     houses = grid.get_houses()
#     # Get keys from the cable dictionary
#     us_ckeys = list(cables.keys())
#     ckeys = []
#
#     for bkey in batteries:
#         group = []
#         for ckey in us_ckeys:
#             if cables[ckey].get_batt() == bkey:
#                 group.append(ckey)
#         ckeys.append(group)
#
#     for i in range(n_alg):
#         score = grid.tot_len()
#         shuffle(ckeys)
#         shuffle(ckeys[0])
#         shuffle(ckeys[1])
#
#         orgA = cables[ckeys[0][0]]
#         orgB = cables[ckeys[1][0]]
#         newA = deepcopy(orgA)
#         newB = deepcopy(orgB)
#
#         houseA = houses[orgA.get_id()]
#         houseB = houses[orgB.get_id()]
#
#         battA = batteries[orgA.get_batt()]
#         battB = batteries[orgB.get_batt()]
#
#         newA.change_route(houseA.get_coord(), battB.get_coord())
#         newA.add_batt(battB.get_id())
#         newB.change_route(houseB.get_coord(), battA.get_coord())
#         newB.add_batt(battA.get_id())
#
#         new_score = score - (orgA.get_length() + orgB.get_length()) + (newA.get_length() + newB.get_length())
#
#         if score > new_score and battA.get_cap() > houseB.get_max() and battB.get_cap() > houseA.get_max():
#             grid.rem_cable(orgA.get_id())
#             grid.rem_cable(orgB.get_id())
#             grid.add_cable(newA)
#             grid.add_cable(newB)
#
#         print('iteration:', i, 'best:', score, 'current:', new_score)
#
#     return grid


if __name__ == '__main__':
    print(sim_ann(random(create_grid(0, 50, 50, 1)), 1000).get_cost())