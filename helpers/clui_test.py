#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert

import os
import csv
from helpers.load_data import create_grid
from helpers.greedy import greedy
from helpers.greedy2 import greedy2
from helpers.random_alg import random
from helpers.hillclimber import hillclimber
from helpers.sim_annealing import sim_ann
from helpers.clui import prompt_alg, choose_distr


ALGORITHMS = {'random': random, 'greedy': greedy, 'greedy2': greedy2,
              'hillclimber': hillclimber, 'simulated_annealing': sim_ann}


def clui_test():
    print('TEST INTERFACE')
    district = choose_distr()
    grid = create_grid(0, 50, 50, district)
    alg = prompt_alg()
    result = do_alg(alg, grid)
    path = save(result, district, alg)
    print('Saved result at: ', path)


def save(result, distr, alg):
    path = os.path.dirname(__file__).replace("helpers", f"data\\results\\TEST_District_{distr}_{alg}_n_times.csv")

    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)
    csvfile.close()
    return path

def do_alg(alg, grid):
    print('Number of solutions')
    user_in = input('> ')
    try:
        n_sol = int(user_in)
    except ValueError:
        print('Not a valid number')
        return do_alg(alg, grid)

    if alg == 'hillclimber' or alg == 'simulated_annealing':
        print('How many iterations')
        n = input('> ')
        try:
            n = int(n)
        except ValueError:
            print("Invalid number, negatives and decimals are not allowed")
            return do_alg(alg, grid)
        print('Algorithm to create initial solution\nrandom: [0], greedy: [1], greedy2: [2]')
        user_in = input('> ')
        algorithms = {0: 'random', 1: 'greedy', 2: 'greedy2'}
        try:
            user_in = int(user_in)
        except ValueError:
            print('Invalid number, choose one from list below')
            return do_alg(alg, grid)
        if user_in < 2 or user_in > 0:
            results = []
            for i in range(n_sol):
                new_grid = ALGORITHMS[algorithms[user_in]](grid)
                grid = ALGORITHMS[alg](new_grid, n)
                results.append([i, grid.get_cost()])
            return results
    else:
        results = []
        for i in range(n_sol):
            grid = ALGORITHMS[alg](grid)
            results.append([i, grid.tot_len()])
        return results
