#!/usr/bin/python
# District class for smart grid
# Gwydion Oostvogel, Jelle Westerbos, Sophie Schubert


from classes.Battery import Battery
from classes.House import House
from classes.Cable import Cable


class Grid(object):

    def __init__(self, id, x_max, y_max):
        """
        Initialize object with parameters.
        :param id: int
        :param x_max: int
        :param y_max: int
        """
        self._id = id
        self._x_max = x_max
        self._y_max = y_max
        self._cables = {}
        self._batteries = {}
        self._houses = {}
        self._grid = []
        for i in range(y_max + 1):
            row = []
            for j in range(x_max + 1):
                row.append('')
            self._grid.append(row)

    def __str__(self):
        """
        Override default __str__ method
        :return: str
        """
        batteries = ""
        for key in self._batteries:
            if not batteries:
                batteries += "\n" + self.get_battery(key).__str__()
            else:
                batteries += "\n\n" + self.get_battery(key).__str__()

        houses = ""
        for key in self._houses:
            if not houses:
                houses += "\n" + self.get_house(key).__str__()
            else:
                houses += "\n\n" + self.get_house(key).__str__()

        cables = ""
        for key in self._cables:
            if not cables:
                cables += "\n" + self.get_cable(key).__str__()
            else:
                cables += "\n\n" + self.get_cable(key).__str__()

        grid = "Grid layout:\n["
        for row in self._grid:
            grid += f"\n{row}"
        grid += "\n]"

        return (f"District: {self._id}\nx max: {self._x_max}\ny max: {self._y_max}\n\nbatteries:{batteries}\n\n"
                f"houses:{houses} \n\ncables:{cables}\n{grid}")

    # Accessor methods (getters)
    def get_id(self):
        """
        Return id of the district
        :return: int
        """
        return self._id

    def get_max(self):
        """
        Returns max x, y values for district
        :return: int, int
        """
        return self._x_max, self._y_max

    def get_house(self, id):
        """
        Returns house object with given id.
        :return: object
        """
        return self._houses[id]

    def get_houses(self):
        """
        Returns all houses.
        :return: dictionary
        """
        return self._houses

    def get_battery(self, id):
        """
        Returns battery object with given id.
        :return: object
        """
        return self._batteries[id]

    def get_batteries(self):
        """
        Returns all batteries.
        :return: dictionary
        """
        return self._batteries

    def get_cable(self, cable_id):
        """
        Returns cable object with given id.
        :return: object
        """
        return self._cables[cable_id]

    def get_cables(self):
        """
        Returns all cables.
        :return: dictionary
        """
        return self._cables

    # Mutator methods (setters)
    def add_house(self, house):
        """
        Adds a house to the houses dict.
        :param house: object
        :return: none
        """
        if house.get_id() not in self._houses:
            self._houses[house.get_id()] = house
        else:
            print("Error: Key already in _houses")
        coord = house.get_coord()
        if self._grid[coord[1]][coord[0]] == '' or ('C' in self._grid[coord[1]][coord[0]]):
            self._grid[coord[1]][coord[0]] = house.get_id()

    def add_battery(self, battery):
        """
        Adds a battery to the batteries dict.
        :param battery: object
        :return: none
        """
        if battery.get_id() not in self._batteries:
            self._batteries[battery.get_id()] = battery
        else:
            print("Error: Key already in self._batteries")
        coord = battery.get_coord()
        if self._grid[coord[1]][coord[0]] == '' or self._grid[coord[1]][coord[0]] == 'C':
            self._grid[coord[1]][coord[0]] = battery.get_id()

    def add_cable(self, cable):
        """
        Adds cable to the cables dict.
        :param cable: object
        :return: none
        """
        cable_id = cable.get_id()
        self._cables[cable_id] = cable
        route = cable.get_route()
        for i in range(len(route)-1):
            x1 = route[i][0]
            y1 = route[i][1]
            x2 = route[i + 1][0]
            y2 = route[i + 1][1]

            if x1 - x2 == 0:
                if y1 > y2:
                    small = y2
                else:
                    small = y1
                for y in range(small, small + abs(y1 - y2)+1):
                    self._grid[y][x1] = self._grid[y][x1] + cable_id

            elif y1 - y2 == 0:
                if x1 > x2:
                    small = x2
                else:
                    small = x1
                for x in range(small, small + abs(x1 - x2)+1):
                    self._grid[y1][x] = self._grid[y1][x] + cable_id

            else:
                print("Error: invalid route")


# def main():
#     kanaleneiland = Grid(1, 10, 10)
#     coord_bat = [1, 3, 5, 7, 9]
#     nr = 0
#     for i in range(len(coord_bat)):
#         id0 = f"B{nr}"
#         kanaleneiland.add_battery(Battery(id0, coord_bat[i], coord_bat[i], 1500))
#         nr += 1
#
#     coord_house = [0, 2, 4, 6, 8, 10]
#     nr1 = 0
#     for i in range(len(coord_house)):
#         id1 = f"H{nr1}"
#         kanaleneiland.add_house(House(id1, coord_house[i], coord_house[i], 300))
#         nr1 += 1
#
#     C0 = Cable('C0')
#     C0.add_route(1, 1)
#     C0.add_route(1, 4)
#     C0.add_route(4, 4)
#     kanaleneiland.add_cable(C0)
#
#     print(kanaleneiland)
#
#
# if __name__ == "__main__":
#     main()