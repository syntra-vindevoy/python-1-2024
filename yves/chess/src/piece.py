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

    def empty_or_foe(self, *, position: Position, board: Board):
        piece = board.get_piece(position=position)

        if piece is None:
            return True

        if piece.color != self.color:
            return True

        return False

    def get_movement(self, *, from_pos: Position, to_pos: Position):
        delta_horizontal = abs(to_pos.horizontal - from_pos.horizontal)
        delta_vertical = abs(to_pos.vertical - from_pos.vertical)

        return delta_horizontal, delta_vertical


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

        # for _ in range(max(horizontal_move, vertical_move)):
        #     current_pos = Position(current_pos.horizontal + step_horizontal, current_pos.vertical + step_vertical)
        #     if current_pos == to_pos:
        #         break
        #     if board.get_piece(current_pos) is not None:
        #         return True
        # return False


class Pawn(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self, position: Position):
        symbol = "♟" if self.color == "black" else "♙"
        return f"{self.color.ansi_code}{symbol}\033[0m"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        eof = self.empty_or_foe(position=to_pos, board=board)

        if not eof:
            return False

        ism = self.has_invalid_submoves(from_pos=from_pos, to_pos=to_pos, board=board)

        if ism:
            return False

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
        vertical_diff = abs(to_pos.vertical - from_pos.vertical)
        horizontal_diff = abs(to_pos.horizontal - from_pos.horizontal)
        return (vertical_diff == 2 and horizontal_diff == 1) or (vertical_diff == 1 and horizontal_diff == 2)


class Bishop(Piece):
    def __init__(self, *, color: Color, position: Position):
        super().__init__(color=color, position=position)

    def draw(self, position: Position):
        return "♝" if self.color == "black" else "♗"

    def is_valid_move(self, *, from_pos: Position, to_pos: Position, board: Board):
        # Bishops move diagonally, meaning horizontal and vertical changes must be equal
        horizontal, vertical = self.get_movement(from_pos=from_pos, to_pos=to_pos)
        return horizontal == vertical

        # horizontal_step = 1 if to_pos.horizontal > from_pos.horizontal else -1
        # vertical_step = 1 if to_pos.vertical > from_pos.vertical else -1
        # current_horizontal = from_pos.horizontal + horizontal_step
        # current_vertical = from_pos.vertical + vertical_step
        # # Check that no pieces are in the way
        # while current_horizontal != to_pos.horizontal and current_vertical != to_pos.vertical:        current_key = Position(current_horizontal, current_vertical).get_key()        if board.positions[current_key] is not None:            return False  # something is blocking the path        current_horizontal += horizontal_step        current_vertical += vertical_step    # Check if the target position is occupied by a piece of the same color    target_piece = board.positions[to_pos.get_key()]    if target_piece is not None and target_piece.color == self.color:        return False    # If all checks pass, the move is valid    return True


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
        vertical_diff = abs(to_pos.vertical - from_pos.vertical)
        horizontal_diff = abs(to_pos.horizontal - from_pos.horizontal)

        return vertical_diff <= 1 and horizontal_diff <= 1