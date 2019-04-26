# District class for smart grid
# Gwydion Oostvogel, Jelle Westerbos, Sophie Schubert


class Cable(object):
    def __init__(self, id, price=9, batt_id=0):
        """
        Initialize object with parameters.
        :param id: string
        :param price: int
        :param batt_id: int
        """
        self._id = id
        self._price = price
        self._id_battery = batt_id
        self._route = []

    def __str__(self):
        """
        Override default __str__ method.
        :return: string
        """
        return (f"Cable: {self._id}\nPrice: {self._price}\n"
                f"From house: {self._id} to battery {self._id_battery}\nRoute: {self._route}")

    # Accessor methods (getters)
    def get_id(self):
        """
        Return id of cable which is also id of the house connected to the cable.
        :return: int
        """
        return self._id

    def get_batt(self):
        """
        Return battery id of cable
        :return: int
        """
        return self._id_battery

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

    # Mutator methods (setters)
    def add_batt(self, batt_id):
        """
        Adds battery to the cable.
        :param batt_id: int
        :return: none
        """
        self._id_battery = batt_id

    def add_route(self, x, y):
        """
        Adds route segment to routes
        :param x: int
        :param y: int
        :return: none
        """
        self._route.append((x, y))

    def change_route(self, old_x, old_y, new_x, new_y):
        """
        Change point of route.
        :param old_x: int
        :param old_y: int
        :param new_x: int
        :param new_y: int
        :return: none
        """
        for n, i in enumerate(self._route):
            if i == (old_x, old_y):
                self._route[n] = (new_x, new_y)
        return "Error: route not in routes"
