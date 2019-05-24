#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
"""
Battery class for smart grid.
"""


class Battery(object):
    def __init__(self, id, x, y, cap, type='Standard', price=5000):
        """
        Initialize object with parameters.
        :param id: string
        :param x: int
        :param y: int
        :param cap: float
        :param type: string
        :param price: int
        """
        self._id = id
        self._x = x
        self._y = y
        self._max_cap = cap
        self._cap = cap
        self._type = type
        self._price = price

    def __str__(self):
        """
        Override default __str__ method.
        :return: string
        """
        return (f"Battery: {self._id}\nCoordinates x,y: {self._x},{self._y}\nType: {self._type}\n"
                f"Capacity: {self._cap}\nPrice: {self._price}")

    # Accessor methods (getters)
    def get_id(self):
        """
        Returns id
        :return: int
        """
        return self._id

    def get_coord(self):
        """
        Returns coordinates
        :return: int, int
        """
        return self._x, self._y

    def get_cap(self):
        """
        Returns capacity
        :return: float
        """
        return self._cap

    def get_type(self):
        """
        Returns type of battery
        :return: string
        """
        return self._type

    def get_price(self):
        """
        Returns price
        :return: int
        """
        return self._price

    # Mutator methods (setters)
    def set_coord(self, x, y):
        """
        Change location of battery
        :param x: int
        :param y: int
        :return: none
        """
        self._x = x
        self._y = y

    def red_cap(self, batt_in):
        """
        Reduce capacity of battery
        :param batt_in: float
        :return: none
        """
        self._cap -= batt_in

    def reset_cap(self):
        """
        Reset capacity
        :return: none
        """
        self._cap = self._max_cap
