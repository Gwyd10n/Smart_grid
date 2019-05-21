#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert

import string
import sys
from helpers.load_data import create_grid
from helpers.greedy import greedy
from helpers.greedy2 import greedy2
from helpers.random_alg import random
from helpers.hillclimber import hillclimber
from helpers.sim_annealing import sim_ann
from helpers.helpers import save_csv
from helpers.visualizer import plot

ALGORITHMS = {'random': random, 'greedy': greedy, 'greedy2': greedy2,
              'hillclimber': hillclimber, 'simulated_annealing': sim_ann}

def CLUI(path):
    print('Type help for list of commands')
    version = choose_distr()
    grid = create_grid(0, 50, 50, version)
    algorithm = prompt_alg()
    new_grid = do_alg(algorithm, grid)
    save(path, new_grid)
    # prompt plot
    # anther?
        # same distr
        # new distr

def save(path, new_grid):
    pass

def do_alg(alg, grid):
    if alg == 'hillclimber' or alg == 'simulated_annealing':
        print('How many iterations')
        n = input('>')
        try:
            n = int(n)
        except ValueError:
            print("invalid number, negatives and decimals are not allowed")
            return do_alg(alg, grid)
        print('algorithm to create initial solution\nrandom: [0], greedy: [1], greedy2: [2]')
        user_in = input('>')
        algorithms = {0: 'random', 1: 'greedy', 2: 'greedy2'}
        try:
            user_in = int(user_in)
        except ValueError:
            print('invalid number, choose one from list below')
            return do_alg(alg, grid)
        if user_in < 2 or user_in > 0:
            new_grid = ALGORITHMS[algorithms[user_in]](grid)
            return ALGORITHMS[alg](new_grid, n)
    else:
        return ALGORITHMS[alg](grid)

def prompt_alg():
    algorithms = {0: 'random', 1: 'greedy', 2: 'greedy2', 3: 'hillclimber', 4: 'simulated_annealing'}
    print("What algorithm should be used (type INFO to get description of algorithms)")
    print(''.join(['{0}{1}'.format(str(key) + ': ', value + '  ') for key, value in algorithms.items()]), end=' ')
    user_in = input('\n>')
    basic_command(user_in)
    try:
        user_in = int(user_in)
    except ValueError:
        print('invalid number, choose one from list below')
        return prompt_alg()
    if not user_in in algorithms:
        print('invalid algorithm, choose one from list below')
        return prompt_alg()
    else:
        return algorithms[user_in]

def back():
    print("go back?\nyes: [y], no: [n]")
    user_in = input('>')
    basic_command(user_in)
    if user_in == 'n':
        basic_command('quit')
    elif user_in != 'y':
        print('YES OR NO')
        return back()

def basic_command(user_in):
    user_in = user_in.lower()
    if user_in == 'quit':
        sys.exit("This conversation can serve no purpose anymore. Good-bye.")
    elif user_in == 'help':
        print("""
    There is no distinction between upper and lower case.
    QUIT: stops program
    INFO: short description of each algorithm
                """)
        back()
    elif user_in == 'info':
        print("""Available algorithms:
    RANDOM: connects each house to battery in random order
    GREEDY: connects each house to the closest battery in a random order
    GREEDY2: connect each battery to the closest house in a random order
    HILLCLIMBER: for a valid solution, switch battery for two houses, keep better state
    SIMULATED ANNEALING: for a valid solution, switch battery for two houses, keep better state respecting local minima""")
        back()


def choose_distr():
    print("district to solve:\n[1] [2] [3]")
    user_in = input('>')
    basic_command(user_in)
    try:
        int(user_in)
    except ValueError:
        print('not a valid number, choose from numbers below')
        return choose_distr()
    return user_in
