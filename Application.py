#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert


import os
import sys
from helpers.load_data import create_grid
from helpers.greedy import greedy
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

    greedy_grid = greedy(grid)

    # cables = list(greedy_grid.get_cables().keys())
    # print(type(greedy_grid.get_cables()))
    # for idx, key in enumerate(cables):
    #     if not idx % 2:
    #         greedy_grid.rem_cable(key)

    # print(greedy_grid)
    # save_csv(greedy_grid, sys.argv[1], "greedy")


    hill_grid = hillclimber(greedy_grid)
    # print(hill_grid)
    save_csv(hill_grid, sys.argv[1], "hillclimber")


if __name__ == "__main__":
    main()
