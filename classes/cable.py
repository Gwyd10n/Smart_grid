#!/usr/bin/env python
# Gwydion Oostvogel, Sophie Schubert
"""
Cable class for smart grid.
"""


class Cable(object):
    def __init__(self, cable_id, price=9):
        """
        Initialize object with parameters.
        :param cable_id: string
        :param price: int
        """
        self._id = cable_id
        self._price = price
        self._battery_id = ""
        self._route = []

    def __str__(self):
        """
        Override default __str__ method.
        :return: string
        """
        return (f"Cable: {self._id}\nPrice: {self._price}\n"
                f"From house: {self._id} to battery {self._battery_id}\nRoute: {self._route}")

    # Accessor methods (getters)
    def get_id(self):
        """
        Return id of cable
        :return: int
        """
        return self._id

    def get_batt(self):
        """
        Return battery id of cable
        :return: string
        """
        return self._battery_id

    def get_price(self):
        """
        Return price of cable per segment.
        :return: int
        """
        return self._price

    def get_length(self):
        """
        Calculate total length of cable.
        :return: int
        """
        start = self._route[0]
        end = self._route[-1]
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def get_route(self):
        """
        Return route of cable.
        :return: list
        """
        return self._route

    # Mutator methods (setters)
    def add_batt(self, batt_id):
        """
        Adds battery to the cable.
        :param batt_id: int
        :return: none
        """
        self._battery_id = batt_id

    def add_house(self, house_id):
        """
        Adds house to the cable.
        :param house_id:
        :return:
        """
        self._house_id = house_id

    def add_route(self, house, battery):
        """
        Adds route to cable from house to battery
        :param x: int
        :param y: int
        :return: none
        """
        self._route.append((house[0], house[1]))
        self._route.append((battery[0], house[1]))
        self._route.append((battery[0], battery[1]))

    def change_route(self, start, end):
        """
        Change route
        :return: none
        """
        self._route = []
        self.add_route(start, end)
