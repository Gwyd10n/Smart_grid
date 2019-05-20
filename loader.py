import csv
from house import House
from battery import Battery


class Data():
    """
    This class contains the necessary functions to load in
    the data that is needed for the smartgrid.
    """

    def __init__(self, number):
        """
        Create houses and batteries for the smartgrid
        """
        self.houses = self.load_houses(f"data/wijk{number}_huizen.csv")
        self.batteries = self.load_batteries(f"data/wijk{number}_batterijen.txt")

    def load_houses(self, filename):
        """
        Loads houses and returns a dictionary with number of houses
        as key and house as object
        """
        # Create house objects
        houses = {}
        with open(filename, "r") as f:
            reader = csv.reader(f)
            # Skip header
            next(reader)
            id = 1
            for rows in reader:
                x_house = int(rows[0])
                y_house = int(rows[1])
                max_output = float(rows[2])
                # Initialize a house object and put it in a dictionary with its
                # id as key.
                house = House(id, x_house, y_house, max_output)
                houses[id] = house
                id += 1

        f.close()

        # Print each house with description
        # self.houses = houses
        # for house in houses:
        #     print(houses[house])

        return houses

    def load_batteries(self, filename):
        """
        Loads batteries and returns dictionary with id and batteries
        as object.
        """
        batteries = {}
        with open(filename, "r") as f:
            # Skip headers
            next(f)
            id = 1
            for line in f:
                # Clean the file
                line = line.replace("[", "").replace("]", "")
                line = line.replace(",", "").replace('\n', '')
                line = line.replace('\t\t', ' ').replace('\t', ' ')
                line = line.split(" ")
                # Set variables
                x_battery = int(line[0])
                y_battery = int(line[1])
                capacity = float(line[2])
                # Initialize battery object and put it in dictionary with
                # id as a key
                battery = Battery(id, x_battery, y_battery, capacity)
                batteries[id] = battery
                id += 1

        f.close()

        # Print the batteries with capacity
        self.batteries = batteries
        for battery in batteries:
            print(batteries[battery])

        return batteries
