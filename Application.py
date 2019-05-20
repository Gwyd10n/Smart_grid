#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert


import sys
from helpers.load_data import create_grid
from helpers.greedy import greedy
from helpers.greedy2 import greedy2
from helpers.random import random
from helpers.hillclimber import hillclimber
from helpers.helpers import save_csv


def main():
    # Check for correct number of arguments.
    if len(sys.argv) != 2:
        print("Usage: Python Application.py <1, 2 or 3>")
        sys.exit(1)
    version = sys.argv[1]

    # Create grid
    grid = create_grid(0, 50, 50, version)
    # random_grid = random(grid)

    # test if there are any cables
    # print(random_grid)

    greedy_grid = greedy2(grid)
    print(greedy_grid)
    #save_csv(greedy_grid, sys.argv[1], "greedy2")
    # print(greedy_grid)
    # save_csv(greedy_grid, sys.argv[1], "greedy")

    # hill_grid = hillclimber(greedy_grid)


if __name__ == "__main__":
    main()
