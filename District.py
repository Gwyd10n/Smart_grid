"""
District class for smart grid
"""

class District(object):

    def __init__(self, id, x_max, y_max):
        self._id = id
        self._x_max = x_max
        self._y_max = y_max
        self._houses = {}
        self._batteries = {}

    def __str__(self):
        return f" District: {self.id}\n x max: {self.x_max}\n y max: {self.y_max}"

    # Accessor methods (getters)
    def get_id(self):
        """
        Return id of the district
        :return: int
        """
        # TODO

    def get_max(self):
        """
        Returns max x, y values for district
        :return: tuple
        """
        return self._x_max, self._y_max

    def get_house(self):
        """
        Returns dictionary of house objects in the district.
        :return: dict
        """
        # TODO

    def get_batteries(self):
        """
        Returns dictionary of battery objects in the district.
        :return: dict
        """
        # TODO

    # Mutator methods (setters)
    # TODO


if __name__ == "__main__":
    Krooswijk = District(1, 50, 50)
    print(Krooswijk)