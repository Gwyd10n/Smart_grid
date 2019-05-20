class Battery(object):

    def __init__(self, id, x_pos, y_pos, capacity):
        """
        Initializes an Item
        """
        self.id = id
        self.x_battery = x_pos
        self.y_battery = y_pos
        self.capacity = capacity
        self.capacity_available = 0

    # Accessor methods (getters)
    def get_id(self):
        """
        Returns id of the battery
        """
        return self.id

    def get_coord(self):
        """
        Returns coordinates
        """
        return self.x_battery, self.y_battery

    def get_capacity(self):
        """
        Returns capacity
        """
        return self.capacity

    def __str__(self):
        return f"Battery {self.id} \nCoordinates (x,y): {self.x_battery},{self.y_battery}\nCapacity: {self.capacity}"
