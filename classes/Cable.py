# District class for smart grid
# Gwydion Oostvogel, Sophie Schubert


class Cable(object):
    def __init__(self, cable_id, price=9):
        """
        Initialize object with parameters.
        :param cable_id: string
        :param price: int
        """
        self._id = cable_id
        self._price = price
        self._battery_id = ''
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


    def get_house(self):
        """
        Return house id of cable
        :return: string
        """
        return self._house_id


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
        total_length = 0
        for i in range(len(self._route)-1):
            total_length += abs(self._route[i] - self._route[i+1])
        return total_length

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


    def add_route(self, start, end):
        """
        Adds route segment to routes
        :param x: int
        :param y: int
        :return: none
        """
        self._route.append([start[0], start[1]])
        self._route.append([end[0], start[1]])
        self._route.append([end[0], end[1]])

    def change_route(self, old_x, old_y, new_x, new_y):
        """
        Change point of route.
        :param old_x: int
        :param old_y: int
        :param new_x: int
        :param new_y: int
        :return: none
        """
        for n, coord in enumerate(self._route):
            if coord == (old_x, old_y):
                self._route[n] = [new_x, new_y]
        return "Error: route not in routes"
