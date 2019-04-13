# District class for smart grid
# Gwydion Oostvogel, ..., ...


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
        self._houses = {}
        self._batteries = {}

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
                batteries += ",\n\n" + self.get_battery(key).__str__()

        houses = ""
        for key in self._houses:
            if not houses:
                houses += "\n" + self.get_house(key).__str__()
            else:
                houses += ",\n\n" + self.get_house(key).__str__()

        return f"District: {self._id}\nx max: {self._x_max}\ny max: {self._y_max}\nbatteries: {batteries}\n\nhouses: {houses}"

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

    def get_battery(self, id):
        """
        Returns battery object with given id.
        :return: object
        """
        return self._batteries[id]

    # Mutator methods (setters)
    def add_battery(self, battery, id):
        """
        Adds a battery to the batteries dict.
        :param battery: object
        :param id: int
        :return: none
        """

        if id not in self._batteries:
            self._batteries[id] = battery
        else:
            print("Error: Key already in _batteries")

    def add_house(self, house, id):
        """
        Adds a house to the houses dict.
        :param house: object
        :param id: int
        :return: none
        """
        if id not in self._houses:
            self._houses[id] = house
        else:
            print("Error: Key already in _houses")


# test
if __name__ == "__main__":
    Krooswijk = Grid(1, 50, 50)
    print(Krooswijk)
