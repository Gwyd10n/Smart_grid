#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
from classes.Cable import Cable
from helpers.helpers import get_man
from random import shuffle


def greedy2(grid):
    max_iterations = 1000
    for i in range(max_iterations):
        try:
            grid.clear_cables()
            return greedy_alg_2(grid)
        except KeyError:
            pass
    exit("Greedy not solved")

def find_closest_house(grid):

    batteries = grid.get_batteries()
    houses = grid.get_houses()
    original_houses = houses

    closest_houses = []

    get_max = grid.get_max()

    for battery in batteries:
        # Save best option
        shortest_distance = get_max[0] + get_max[1]
        best_house = ""
        coupled_houses = []
        battery_coord = batteries[battery].get_coord()
        for house in houses:
            house_coord = houses[house].get_coord()
            if get_man(house_coord, battery_coord) <= shortest_distance and batteries[battery].get_cap() >= houses[house].max_out():
                best_house = house


def greedy_alg_2(grid):
    """
    This is a greedy algorithm which connects the closest house to the battery
    by looping through the batteries.
    """
    # Shuffle the list with battery keys
    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)

    # Shuffle the list with house keys
    houses = grid.get_houses()
    hkeys = list(houses.keys())
    shuffle(hkeys)

    print(find_closest_house(grid))
