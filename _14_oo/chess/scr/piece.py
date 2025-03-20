from board import Position
from color import Color


class Piece:
    def __init__(self, color: Color, position: Position):
        self.color = color
        self.position = position


class Pawn(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)
class Rook(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)


class Knight(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)


class Bishop(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)


class Queen(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)


class King(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)