#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
"""
Command line user interface for smart grid.
"""

import os
import sys
from helpers.load_data import create_grid
from helpers.greedy import greedy
from helpers.greedy2 import greedy2
from helpers.random_alg import random
from helpers.hillclimber import hillclimber
from helpers.sim_annealing import sim_ann
from helpers.kmeans import kmeans
from helpers.helpers import save_csv
from helpers.visualizer import plot
from helpers.helpers import upper_bound, lower_bound, distance

ALGORITHMS = {'random': random, 'greedy': greedy, 'greedy2': greedy2,
              'hillclimber': hillclimber, 'simulated_annealing': sim_ann}


def clui():
    """
    Ask for user input.
    :return: none
    """
    print('Type HELP for list of commands')
    district = choose_distr()
    grid = create_grid(0, 50, 50, district)
    do_kmean(grid)
    show_bounds(grid)
    algorithm = prompt_alg()
    new_grid = do_alg(algorithm, grid)
    print('Cost for this configuration:', new_grid.get_cost())
    path = save(new_grid, district, algorithm)
    prompt_plot(path)
    another()


def do_kmean(grid):
    """
    Ask if user wants place batteries using kmeans.
    :param grid: object
    :return:
    """
    print('Place batteries using kmeans? Otherwise you will use the supplied coordinates\n yes: [y] no: [n]')
    user_in = input('> ')
    command(user_in)
    if yn(user_in):
        kmeans(grid)
        print('K means done')
    elif yn(user_in) == '':
        do_kmean(grid)


def show_bounds(grid):
    """
    Aks if user wants to calculate upper and lower bound.
    :param grid: object
    :return: none
    """
    print('Calculate upper and lower bound?\n yes: [y] no: [n]')
    user_in = input('> ')
    command(user_in)
    if yn(user_in):
        print('Upper bound: ', upper_bound(distance(grid)))
        print('Lower bound: ', lower_bound(distance(grid)))
    elif yn(user_in) == '':
        show_bounds(grid)


def another():
    """
    Ask if user wants to calculate another grid.
    :return: none
    """
    print('Another?\n yes: [y], no: [n]')
    user_in = input('> ').lower()
    command(user_in)
    if yn(user_in):
        clui()
    elif yn(user_in) == '':
        another()
    elif not yn(user_in):
        command('quit')


def prompt_plot(path):
    """
    Ask if user wants to plot the solution.
    :param path: string
    :return: none
    """
    print('Plot solution?\n yes: [y], no: [n]')
    user_in = input('> ').lower()
    command(user_in)
    if yn(user_in):
        plot(path)
    elif yn(user_in) == '':
        prompt_plot(path)


def save(new_grid, district, algorithm):
    """
    Ask if user wants to save solution.
    :param new_grid: object
    :param district: int
    :param algorithm: string
    :return: string
    """
    print('Would you like to save this configuration?\n(NOTE: can only plot if configuration is saved)\n yes: [y], no: [n]')
    user_in = input('> ').lower()
    command(user_in)
    if yn(user_in):
        print('Add custom name?\n yes: [y], no: [n]')
        user_in = input('> ').lower()
        command(user_in)
        if yn(user_in):
            name = '_' + input('Name: > ')
            path = save_csv(new_grid, district, algorithm + name)
        elif yn(user_in) == '':
            save(new_grid, district, algorithm)
        else:
            path = save_csv(new_grid, district, algorithm)
        print(f'Saved csv file to {path}')
        return path
    elif yn(user_in) == '':
        save(new_grid, district, algorithm)
    elif not yn(user_in):
        print('Sure?\n yes: [y], no: [n]')
        user_in = input('> ').lower()
        command(user_in)
        if not yn(user_in):
            save(new_grid, district, algorithm)


def do_alg(alg, grid):
    """
    Calculate solution with specified algorithm.
    :param alg: string
    :param grid: object
    :return: object
    """
    # Set posiible algorithms
    algorithms = {0: 'random', 1: 'greedy', 2: 'greedy2'}
    cooling_schemes = {0: 'linear', 1: 'exponential', 2: 'sigmoidal', 3: 'geman&geman'}

    # Ask for hillclimber parameters
    if alg == 'hillclimber':
        print('How many iterations')
        user_in = input('> ')
        command(user_in)
        # Check if input is valid
        try:
            n = int(user_in)
        except ValueError:
            print("Invalid number, negatives and decimals are not allowed")
            return do_alg(alg, grid)

        print('Algorithm to create initial solution\nrandom: [0], greedy: [1], greedy2: [2]')
        user_in = input('> ')
        # Check if input is valid
        try:
            user_in = int(user_in)
        except ValueError:
            print('Invalid number, choose one from list below')
            return do_alg(alg, grid)
        if 0 <= user_in <= 2:
            new_grid = ALGORITHMS[algorithms[user_in]](grid)
            return ALGORITHMS[alg](new_grid, n)

    # Ask for parameters for simmulated annealing
    elif alg == 'simulated_annealing':
        print('How many iterations')
        n = input('> ')
        # Check if input is valid
        try:
            n = int(n)
        except ValueError:
            print("Invalid number, negatives and decimals are not allowed")
            return do_alg(alg, grid)

        print('Algorithm to create initial solution\nrandom: [0], greedy: [1], greedy2: [2]')
        user_in = input('> ')
        command(user_in)
        # Check if input is valid
        try:
            user_in = int(user_in)
        except ValueError:
            print('Invalid number, choose one from list')
            return do_alg(alg, grid)
        # Input validation
        if 0 <= user_in <= 2:
            new_grid = ALGORITHMS[algorithms[user_in]](grid)
            print('Set annealing parameters?\nyes: [y], no: [n]\n(default is linear cooling scheme, with Tstart = 10 and Tend = 1)')
            user_in = (input('> '))
            command(user_in)
            # User wants to set parameters for algorithm
            if yn(user_in):
                # Get start temperature
                user_in = input('Tstart:\n(must be integer greater than 0)\n> ')
                command(user_in)
                # Input validation
                try:
                    Ts = int(user_in)
                except ValueError:
                    print('Invalid start temperature')
                    return do_alg(alg, grid)
                if Ts < 0:
                    print('Tstart must be positive number')
                    return do_alg(alg, grid)

                # Get end temperature
                user_in = input('Tend:\n(must be integer smaller than Tstart and greater than 0)\n> ')
                command(user_in)

                # Input validation
                try:
                    Te = int(user_in)
                except ValueError:
                    print('Invalid end temperature')
                    return do_alg(alg, grid)
                if Te < 0:
                    print('Tend must be positive number')
                    return do_alg(alg, grid)

                if Te >= Ts:
                    print('Invalid end temperature')
                    return do_alg(alg, grid)
                print('Select cooling scheme')
                print(''.join(['{0}{1}'.format(str(key) + ': ', value + '  ') for key, value in cooling_schemes.items()]),
                      end=' ')
                user_in = input('\n> ')
                command(user_in)

                try:
                    user_in = int(user_in)
                except ValueError:
                    print('Invalid number, choose one from list')
                    return do_alg(alg, grid)

                if user_in not in cooling_schemes:
                    print('Invalid algorithm, choose one from list')
                    return do_alg(alg, grid)
                else:
                    cooling = cooling_schemes[user_in]

                # Ask for geman&geman parameter
                if cooling == 'geman&geman':
                    print('Choose d value (value must be greater than 0\n default d = 1')
                    user_in = input('> ')
                    command(user_in)
                    try:
                        d = int(user_in)
                    except ValueError:
                        print('Not a number')
                        do_alg(alg, grid)
                    if d < 0:
                        print('d must be greater than 0')
                        do_alg(alg, grid)
                    # Return new grid
                    return ALGORITHMS[alg](new_grid, n, cooling, Ts, Te, d)
                else:
                    # Return new grid
                    return ALGORITHMS[alg](new_grid, n)

            elif yn(user_in) == '':
                return do_alg(alg, grid)
            elif not yn(user_in):
                return ALGORITHMS[alg](new_grid, n)

    # No parameters required for chosen algorithm
    else:
        # Return new grid
        return ALGORITHMS[alg](grid)


def prompt_alg():
    """
    Ask user which algorithm should be used.
    :return: string
    """
    algorithms = {0: 'random', 1: 'greedy', 2: 'greedy2', 3: 'hillclimber', 4: 'simulated_annealing'}
    print("What algorithm should be used (type INFO to get description of algorithms)")
    print(''.join(['{0}{1}'.format(str(key) + ': ', value + '  ') for key, value in algorithms.items()]), end=' ')
    user_in = input('\n> ')
    command(user_in)
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


def back():
    """
    Go back to 'main menu'
    :return: none
    """
    print("Go back?\nyes: [y], no: [n]")
    user_in = input('> ').lower()
    command(user_in)
    if yn(user_in) == '':
        back()
    elif not yn(user_in):
        command('quit')


def yn(u_in):
    """
    Check if answer is yes, no or faulty answer
    :param u_in: string
    :return: bool
    """
    u_in = u_in.lower()
    if u_in == 'y':
        return True
    elif u_in == 'n':
        return False
    else:
        return ''


def command(user_in):
    """
    Check if user input is a command.
    :param user_in: string
    :return: none
    """
    user_in = user_in.lower()
    if user_in == 'quit':
        sys.exit('Good-bye.')
    elif user_in == 'help':
        print("""
    There is no distinction between upper and lower case.
    QUIT: stops program
    INFO: short description of each algorithm
    PLOT: plot file in provided path
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
    elif user_in == 'plot':
        print("Provide filename (without file extension):")
        path = os.path.dirname(__file__).replace("helpers", f"data\\results\\{input('> ')}.csv")
        plot(path)


def choose_distr():
    """
    Ask user which district should be calculated.
    :return:
    """
    print("District to solve:\n[1] [2] [3]")
    user_in = input('> ')
    command(user_in)
    try:
        user_in = int(user_in)
    except ValueError:
        print('Not a valid number, choose from numbers below')
        return choose_distr()
    if user_in <= 3:
        return user_in
    else:
        return choose_distr()
