# Battery class for smart grid
# Gwydion Oostvogel, ..., ...

class Battery(object):
    def __init__(self, id, x, y, cap, type='Standard', price=5000):
        self._id = id
        self._x = x
        self._y = y
        self._cap = cap
        self._type = type
        self._price = price

    def __str__(self):
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
        :return: tuple of ints
        """
        return (self._x, self._y)

    def get_capacity(self):
        """
        Returns capacity
        :return: float
        """
        return self._cap

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


if __name__ == "__main__":
    Duracel = Battery(1, 25, 25, 100.0, 'AA', 2500)
    print(Duracel)
    Duracel.set_coord(30, 30)
    print(Duracel.get_id())
    print(Duracel.get_coord())
    print(Duracel.get_capacity())
    print(Duracel.get_price())
