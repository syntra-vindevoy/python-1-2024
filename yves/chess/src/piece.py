from color import Color
from position import Position


class Piece:
    def __init__(self, *, color: Color, position: Position):
        self.color = color
        self.position = position

    def draw(self):
        raise NotImplementedError("draw not implemented")

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board):
        raise NotImplementedError("is_valid_move not implemented")

class Pawn(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        pass

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board):
        pass

class Rook(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        pass

class Knight(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        pass

class Bishop(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        pass

class Queen(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        pass

class King(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        pass