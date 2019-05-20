#!/usr/bin/python
# District class for smart grid
# Gwydion Oostvogel, Sophie Schubert


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

        return (f"District: {self._id}\nx max: {self._x_max}\ny max: {self._y_max}\n\nbatteries:{batteries}\n\n"
                f"houses:{houses} \n\ncables:{cables}")

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

    def tot_len(self):
        """
        Calculate total length of all cables.
        :return:
        """
        len = 0
        for key in self._cables:
            len += self._cables[key].get_length()
        return len

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

    def add_cable(self, cable):
        """
        Adds cable to the cables dict.
        :param cable: object
        :return: none
        """
        cable_id = cable.get_id()
        self._cables[cable_id] = cable

    def rem_cable(self, key):
        """
        Removes cable from cables dict.
        :param key: string
        :return:
        """
        del self._cables[key]

    def clear_cables(self):
        """
        Clears connections, reset battery capacity
        :return:
        """
        self._cables = {}
        for key in self._batteries:
            self._batteries[key].reset_cap()
