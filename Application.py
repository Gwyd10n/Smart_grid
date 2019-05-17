#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert


import sys
from helpers.load_data import create_grid
from helpers.greedy import greedy
from helpers.random import random


def main():
    # Check for correct number of arguments.
    if len(sys.argv) != 2:
        print("Usage: Python Application.py <1, 2 or 3>")
        sys.exit(1)
    version = sys.argv[1]

    # Create grid
    grid = create_grid(0, 50, 50, version)
    random_grid = random(grid)

    # test if there are any cables
    print(random_grid)


if __name__ == "__main__":
    main()
