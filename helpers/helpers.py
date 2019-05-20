from classes.Grid import Grid
from classes.Battery import Battery
from classes.House import House
from classes.Cable import Cable
import csv
import os


def get_man(coord_start, coord_end):
    return abs(coord_start[0] - coord_end[0]) + abs(coord_start[1] - coord_end[1])


def save_csv(grid, distr, alg):
    """
    Saves grid to CSV file.
    :param grid: object
    :param distr: int
    :param algorithm: string
    :return: int
    """
    houses = grid.get_houses()
    batteries = grid.get_batteries()
    cables = grid.get_cables()
    path = os.path.dirname(__file__).replace("helpers", f"data\\District_{distr}_{alg}.csv")
    rows = []

    rows.append([distr, alg, grid.tot_len()])
    for bkey in batteries:
        battery = batteries[bkey]
        rows.append([battery.get_id(), battery.get_coord()[0], battery.get_coord()[1], battery.get_cap()])
        for ckey in cables:
            if battery.get_id() == cables[ckey].get_batt():
                house = houses[ckey]
                rows.append([house.get_id(), house.get_coord()[0], house.get_coord()[1]])
                for point in cables[ckey].get_route():
                    rows.append(point)

    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
