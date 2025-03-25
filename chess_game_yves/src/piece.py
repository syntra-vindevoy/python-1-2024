from board import Position
from player import Color

class Piece:
    def __init__(self, position: Position, color: Color):
        self.position = position
        self.color = color

    def draw(self):
        raise NotImplementedError("draw not implemented")

    def is_valid_move(self, from_pos: Position, to_pos: Position)
        raise NotImplementedError("is_valid_move not implemented"):

class Pawn(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(position, color)

    def draw(self):
        pass

    def is_valid_move(self, from_pos: Position, to_pos: Position):
        pass

class Rook(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(position, color)

class Bishop(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(position, color)

class Knight(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(position, color)

class Queen(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(position, color)


class King(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(position, color)
