


class Board:
    def __init__(self):
        self.setup()

    def setup(self):
        pass

    def draw(self):
        pass


class Position:
    def __init__(self, horizontal: str, vertical: int):
        assert horizontal.upper() in "ABCDEFGH"
        assert len(horizontal) == 1
        assert vertical >= 1 and vertical <= 8

        self.horizontal: int = ord(horizontal.upper()) - 64
        self.vertical: int = vertical


class Move:
    def __init__(self, from_pos: Position, to_pos: Position):
        self.from_pos = from_pos
        self.to_pos = to_pos