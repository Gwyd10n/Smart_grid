#!/usr/bin/env python
# Needed libraries
import csv
import pandas as pd
import sys

# Test classes
from Classes.Grid import Grid
from Classes.Battery import Battery
from Classes.House import House
from Classes.Cable import Cable


class Smartgrid():

    def __init__(self, districts):

        self.houses = self.load_houses(f"Huizen&Batterijen/wijk{districts}_huizen.csv")
        self.batteries = self.load_batteries(f"Huizen&Batterijen/wijk{districts}_batterijen.txt")

    def load_houses(self, filename):
        """
        Read csv files and return as a dictionary with index as key
        """
        df = pd.read_csv(filename)
        houses = df.transpose().to_dict()
        print(houses)

    def load_batteries(self, filename):

        dataframe = pd.read_csv(filename, sep=" ")
        print(dataframe)



        # batteries = {}
        # with open(filename, "r") as f:
        #     print(f)
        #     # id = 1
        #     # for line in f:
        #     #     line = line.replace("[", "").replace("]", "").replace(",", "")
        #     #     line = line.split(" ")
        #     #     xpos = int(line[0])
        #     #     ypos = int(line[1])
        #     #     capacity = float(line[2])
        #     #     battery = Battery(id, xpos, ypos, capacity)
        #     #     batteries[id] = battery
        #     #     id += 1
        #
        # return batteries

        #
        # houses = {}
        # with open(filename, "r") as f:
        #     reader = csv.reader(f)
        #
        #     counter = 0
        #     for house in reader:
        #         x_place = int(rows[0])
        #     houses = {}
        #     for house in f:
        #         if not house == "\n":
        #             houses.append(house.strip())
        #         else:
        #             houses.append(houses)
        #             houses = {}
        # houses.append(houses)
        # print(houses)

    # def load_batteries():
    #     batteries = {}
    #     with open(filename, "r") as f:
    #         batt

#
#
# def get_batteries():
#
#     batteries = {}
#     with open()
#     textfile_1 = pd.read_csv("wijk1_batterijen.txt", header = None)
#     print(textfile_1)
#
# def main():
#     kanaleneiland = Grid(1, 500, 500)
#     coord_bat = [50, 100, 200, 300, 400, 450]
#     for i in range(len(coord_bat)):
#         kanaleneiland.add_battery(Battery(i, coord_bat[i], coord_bat[i], 1500), i)
#
#     coord_house = [5, 10, 20, 30, 40, 60, 80, 90, 110, 120, 130, 140, 150, 160, 170, 180, 190]
#     for i in range(len(coord_house)):
#         kanaleneiland.add_house(House(i, coord_house[i], coord_house[i], 300), i)
#
#     kanaleneiland.add_cable(Cable(1), 1)
#     kanaleneiland.get_cable(1).add_route(10, 50)
#     kanaleneiland.get_cable(1).add_route(10, 10)
#
#     print(kanaleneiland)

if __name__ == "__main__":
    # main()

    Smartgrid(2)
