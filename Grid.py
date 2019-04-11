# District class for smart grid
# Gwydion Oostvogel, ..., ...

class District(object):

    def __init__(self, id, x_max, y_max):
        self._id = id
        self._x_max = x_max
        self._y_max = y_max
        self._houses = {}
        self._batteries = {}

    def __str__(self):
        """
        Overrides default __str__ method
        :return: str
        """
        return f" District: {self._id}\n x max: {self._x_max}\n y max: {self._y_max}"

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
        :return: tuple of ints
        """
        return self._x_max, self._y_max

    def get_house(self, id):
        """
        Returns house object with given id.
        :return: dict
        """
        return self._houses[id]

    def get_batteries(self, id):
        """
        Returns battery object with given id.
        :return: dict
        """
        return self._batteries[id]

    # Mutator methods (setters)
    # TODO

# test
if __name__ == "__main__":
    Krooswijk = District(1, 50, 50)
    print(Krooswijk)