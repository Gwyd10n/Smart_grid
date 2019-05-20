# #!/usr/bin/env python
# # Gwydion Oostvogel, Sophie Schubert

from classes.Cable import Cable
from random import shuffle


def random(grid):
    max_iterations = 1000
    for i in range(max_iterations):
        try:
            grid.clear_cables()
<<<<<<< HEAD:helpers/random_alg.py
            random_grid = random_grid(grid)
=======
            random_grid = random(grid)
>>>>>>> c84d0b76e01f6a9a5773877851f564b8069fc6e1:helpers/random.py
            return random_grid
        except KeyError:
            print(f"grid not solved, trying again for the {i}th time")
    print("no solution found")


<<<<<<< HEAD:helpers/random_alg.py
def random_grid(grid):
=======
def random(grid):
>>>>>>> c84d0b76e01f6a9a5773877851f564b8069fc6e1:helpers/random.py
    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)

    houses = grid.get_houses()
    hkeys = list(houses.keys())
    shuffle(hkeys)

    j = 0
    for i in range(len(hkeys)):
        if batteries[bkeys[j]].get_cap() > houses[hkeys[i]].get_max():
            batteries[bkeys[j]].red_cap(houses[hkeys[i]].get_max())
            cable = Cable(houses[hkeys[i]].get_id())
            cable.add_batt(batteries[bkeys[j]].get_id)
            cable.add_route(houses[hkeys[i]].get_coord(), batteries[bkeys[j]].get_coord())
            grid.add_cable(cable)
            i += 1

        else:
            i -= 1
            j += 1
            if j >= len(bkeys):
                j = 0
    return grid
