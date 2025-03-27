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

    def draw(self, position: Position):
        raise NotImplementedError("draw not implemented")

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        raise NotImplementedError("is_valid_move not implemented")


class Pawn(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self, position: Position):
        return "♟" if self.color == "black" else "♙"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        # TODO: "slaan en passant"
        # TODO: "promoveren" van pion die aan de andere kant geraakt

        if self.color == "WHITE":
            if from_pos.vertical != to_pos.vertical:
                if abs(from_pos.vertical - to_pos.vertical) != 1:
                    return False

                piece = board.positions[to_pos.get_key()]

                if piece is None:
                    return False

                if piece.color == self.color:
                    return False

            if from_pos.horizontal == 2:
                if to_pos.horizontal not in [3, 4]:
                    return False

            else:
                return to_pos.vertical == from_pos.vertical + 1

        else:
            pass

        return True


def has_invalid_submoves(
    self,
    *,
    from_pos: Position,
    to_pos: Position,
    board: Board,
):
    delta_horizontal = to_pos.horizontal - from_pos.horizontal
    delta_vertical = to_pos.vertical - from_pos.vertical

    step_horizontal = 1 if delta_horizontal > 0 else -1 if delta_horizontal < 0 else 0
    step_vertical = 1 if delta_vertical > 0 else -1 if delta_vertical < 0 else 0

    current_pos = from_pos

    horizontal_move = abs(delta_horizontal)
    vertical_move = abs(delta_vertical)

    for _ in range(max(horizontal_move, vertical_move)):
        current_pos = Position(
            current_pos.horizontal + step_horizontal,
            current_pos.vertical + step_vertical,
        )
        if current_pos == to_pos:
            break
        if board.get_piece(current_pos) is not None:
            return True
    return False


class Rook(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self, position: Position):
        return "♜" if self.color == "black" else "♖"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        return True


class Knight(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self, position: Position):
        return "♞" if self.color == "black" else "♘"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        return True


class Bishop(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self, position: Position):
        return "♝" if self.color == "black" else "♗"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        return True


class Queen(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self, position: Position):
        return "♛" if self.color == "black" else "♕"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        return True


class King(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self, position: Position):
        return "♚" if self.color == "black" else "♔"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        return True
