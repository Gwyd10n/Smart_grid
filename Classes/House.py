# Battery class for smart grid
# Gwydion Oostvogel, ..., ...


class House(object):
    def __init__(self, id, x, y, max_out):
        """
        Initialize object with parameters.
        :param id: int
        :param x: int
        :param y: int
        :param max_out: float
        """
        self._id = id
        self._x = x
        self._y = y
        self._max_out = max_out

    def __str__(self):
        """
        Override default __str__ method.
        :return: string
        """
        return f"House: {self._id}\nCoordinates (x,y): {self._x},{self._y}\nMaximum Output: {self._max_out}"

    # Accessor methods (getters)
    def get_id(self):
        """
        Returns id of house.
        :return: int
        """
        return self._id

    def get_coord(self):
        """
        Returns coordinates of house.
        :return: int, int
        """
        return self._x, self._y

    def get_max(self):
        """
        Returns maximum output of house.
        :return:
        """
        return self._max_out

    # Mutator methods (setters)
    ########### Nodig? #############

