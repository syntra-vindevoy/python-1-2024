from coord import coord


class ship:
    "a ship is a range of coordinates, the length of the ship is the number of coordinates it occupies"

    def __init__(self, first: coord, last: coord):
        self.coords = []
        self.alive = True
        # vertical ship
        if first.x == last.x:
            for y in range(min(first.y, last.y), max(first.y, last.y) + 1):
                self.coords.append(coord(first.x, y))
        # horizontal ship
        elif first.y == last.y:
            for x in range(min(first.x, last.x), max(first.x, last.x) + 1):
                self.coords.append(coord(x, first.y))
        # if the coordinates are not in the same row or column, raise an error
        else:
            raise ValueError("Ships must be either horizontal or vertical")
