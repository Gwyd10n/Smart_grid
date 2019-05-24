#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
from classes.cable import Cable
from helpers.helpers import get_man
from random import shuffle


def greedy2(grid):
    """
    This is a greedy algorithm which connects the closest house to the battery
    by looping through the batteries.
    """
    # Shuffle the list with battery keys
    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)

    # Create the list with house keys
    houses = grid.get_houses()
    hkeys = list(houses.keys())

    # For each battery:
    for idx, bkey in enumerate(bkeys):
        # Houses to connect to this battery
        conn_houses = []
        battery = batteries[bkey]
        b_cap = battery.get_cap()

        # Check if there are any houses still available
        if len(hkeys) > 0:
            houses_av = True
        else:
            houses_av = False

        # While houses are still available:
        while houses_av:
            # Initial best distance is max dist of grid
            best = grid.get_max()[0] + grid.get_max()[1]
            # Variable to save closest house
            conn_house = ''
            # Search for closest house:
            for hkey in hkeys:
                # Get house information
                house = houses[hkey]
                h_out = house.get_max()
                # Get manhattan distance current house to battery
                curr_manh = get_man(house.get_coord(), battery.get_coord())

                # Check if the current manhattan distance is less then the best distance
                # Check if the battery has enough capacity to connect the house
                if best >= curr_manh and b_cap >= h_out:
                    conn_house = hkey
                    best = curr_manh

            # If no house is found, stop searching
            if not conn_house or len(hkeys) < 5 - idx:
                houses_av = False
            # Else add found house to houses to connect
            else:
                b_cap -= h_out
                conn_houses.append(conn_house)
                hkeys.remove(conn_house)

        # Connect each house to the current battery
        for house in conn_houses:
            house = houses[house]
            batteries[bkey].red_cap(house.get_max())
            cable = Cable(house.get_id())
            cable.add_batt(bkey)
            cable.add_route(house.get_coord(), batteries[bkey].get_coord())
            grid.add_cable(cable)

    # Return grid with added cables
    return grid
