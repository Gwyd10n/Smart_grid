#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert

import sys
from helpers.clui import clui
from helpers.clui_test import clui_test
from helpers.load_data import create_grid
from helpers.helpers import distance, lower_bound, upper_bound, move
from helpers.kmeans import kmeans_algorithm

if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        clui_test()
    else:
        clui()

    # grid = create_grid(0, 50, 50, 2)
    # g = distance(grid)
    # lower_bound(g)
    # upper_bound(g)
    # move(grid)
    #
    # kmeans_algorithm(grid)
