# District class for smart grid
# Gwydion Oostvogel, Jelle Westerbos, Sophie Schubert


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
        self._cables = {}

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


    def add_cable(self, cable, id):
        """
        Adds cable to the cables dict.
        :param cable: object
        :param id: int
        :return: none
        """
        self._cables[id] = cable

    def get_cable(self, id):
        """
        Returns cable object with given id.
        :return: object
        """
        return self._cables[id]
