# import numpy as np
# import matplotlib.pyplot as plt
import csv
import os


def plot(path):

    with open(path, "r") as csvfile:
        result = csv.reader(csvfile)

        firstln = next(result)
        # Number of the district
        district = firstln[0]


if __name__ == "__main__":
    path = os.path.dirname(os.path.realpath(__file__)).replace("helpers", "data\\results\\District_1_greedy.csv")
    print(path)
    plot(path)

#
# colors = {1: 'green', 2: 'red'}
#
# for house in house_list:
#     x = house.x_house
#     y = house.y_house
#     battery_number = house.connected_battery
#
#     plt.scatter(x, y, marker='^', color=colors[battery_number])
#
#     # voor de horizontale lijn
#     plt.plot((x, battery.x), (y, y), color=colors[battery_number])
#
#     # Voor de verticale lijn
#     plt.plot((battery.x, battery.x), (y, battery.y), color=colors[battery_number])
#
#
# for battery in battery_list:
#     x ...
#     y ...
#     battery_number = battery.battery_id
#
#     plt.scatter(x, y, marker='s', color=colors[battery_number])
#
# plt.show()
#
# for battery in battery_list:
#     for house in battery.connected_houses:
#         een manier om de xs en ys te verzamelen
#
#     battery_number = battery.battery_id
#     plt.scatter(xs, ys, marker='^', color=colors[battery_number])
#
#     plt.scatter(x, y, marker='s', color=colors[battery_number])
