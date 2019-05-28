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
from helpers.kmeans import kmeans
from helpers.helpers import upper_bound, lower_bound, distance


ALGORITHMS = {'random': random, 'greedy': greedy, 'greedy2': greedy2,
              'hillclimber': hillclimber, 'simulated_annealing': sim_ann}


def clui_test():
    """
    Main menu of clui
    :return: none
    """
    print('TEST INTERFACE')
    district = choose_distr()
    grid = create_grid(0, 50, 50, district)
    kmeans(grid)
    alg = prompt_alg()
    result = do_alg(alg, grid)
    path = save(result, district, alg)
    print('Saved result at: ', path)


def save(result, distr, alg):
    """
    Prompt save result.
    :param result: list
    :param distr: int
    :param alg: string
    :return: string
    """
    path = os.path.dirname(__file__).replace("helpers", f"data\\results\\TEST_District_{distr}_{alg}_n_times.csv")

    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)
    csvfile.close()
    return path


def do_alg(alg, grid):
    """
    Specify algorithm parameters
    :param alg: string
    :param grid: object
    :return: list
    """
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
                results.append([i, grid.get_cost(), ])
            return results
    else:
        results = []
        for i in range(n_sol):
            grid = ALGORITHMS[alg](grid)
            results.append([i, grid.tot_len(), lower_bound(distance(grid)), upper_bound(distance(grid))])
        return results


def prompt_alg():
    """
    Ask user which algorithm should be used.
    :return: string
    """
    algorithms = {0: 'random', 1: 'greedy', 2: 'greedy2', 3: 'hillclimber', 4: 'simulated_annealing'}
    print("What algorithm should be used (type INFO to get description of algorithms)")
    print(''.join(['{0}{1}'.format(str(key) + ': ', value + '  ') for key, value in algorithms.items()]), end=' ')
    user_in = input('\n> ')
    try:
        user_in = int(user_in)
    except ValueError:
        print('Invalid number, choose one from list below')
        return prompt_alg()
    if user_in not in algorithms:
        print('Invalid algorithm, choose one from list below')
        return prompt_alg()
    else:
        return algorithms[user_in]


def choose_distr():
    """
    Ask user which district should be calculated.
    :return:
    """
    print("District to solve:\n[1] [2] [3]")
    user_in = input('> ')
    try:
        user_in = int(user_in)
    except ValueError:
        print('Not a valid number, choose from numbers below')
        return choose_distr()
    if user_in <= 3:
        return user_in
    else:
        return choose_distr()
