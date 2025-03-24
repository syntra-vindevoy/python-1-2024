from __future__ import annotations
from typing import TYPE_CHECKING

from color import Color
from position import Position

if TYPE_CHECKING:
    from board import Board  # Avoids importing at runtime


class Piece:
    def __init__(self, *, color: Color, position: Position):
        self.color = color
        self.position = position

    def draw(self):
        raise NotImplementedError("draw not implemented")

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        raise NotImplementedError("is_valid_move not implemented")


class Pawn(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        return "♟" if self.color == "black" else "♙"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        pass


class Rook(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        return "♜" if self.color == "black" else "♖"


class Knight(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        return "♞" if self.color == "black" else "♘"


class Bishop(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        return "♝" if self.color == "black" else "♗"


class Queen(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        return "♛" if self.color == "black" else "♕"


class King(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self):
        return "♚" if self.color == "black" else "♔"
