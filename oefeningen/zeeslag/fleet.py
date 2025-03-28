class fleet:
    """a fleet is a list of ships"""

    def __init__(self):
        self.ships = []

    def add_ship(self, ship):
        """add a ship to the fleet"""
        self.ships.append(ship)

    def __str__(self):
        """return the string representation of the fleet"""
        return str(self.ships)

    def __len__(self):
        """return the number of ships in the fleet"""
        return len(self.ships)
