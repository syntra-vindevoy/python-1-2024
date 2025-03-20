from board import Position
from color import Color


class Piece:
    def __init__(self, color: Color, position: Position):
        self.color = color
        self.position = position

    def draw(self):
        raise NotImplementedError("Draw not implemented")


class Pawn(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)

    def draw(self):
        print("  o")
        print(" /|\\")
        print(" / \\")


class Rook(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)

    def draw(self):
        pass


class Knight(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)

    def draw(self):
        pass


class Bishop(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)

    def draw(self):
        pass


class Queen(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)

    def draw(self):
        pass


class King(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)

    def draw(self):
        pass