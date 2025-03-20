from color import Color


class Position:
    def __init__(self, *, horizontal: str, vertical: int):
        assert horizontal.upper() in "ABCDEFGH"
        assert len(horizontal) == 1
        assert 1 <= vertical <= 8

        self.horizontal: int = ord(horizontal.upper()) - 64
        self.vertical: int = vertical

    def color(self):
        return Color(name="BLACK") if (self.horizontal + self.vertical) % 2 == 0 else Color(name="WHITE")
