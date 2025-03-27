from __future__ import annotations
from typing import TYPE_CHECKING

from color import Color
from move import Move
from piece import Pawn, Rook, Knight, Bishop, Queen, King
from position import Position

if TYPE_CHECKING:
    from board import Board  # Avoids importing at runtime


class Player:
    def __init__(self, *, name: str, color: Color):
        self.name: str = name
        self.color: Color = color
        self.pieces: list = []

        pawn_row = "B" if self.color.name == "WHITE" else "G"
        king_row = "A" if self.color.name == "WHITE" else "H"

        for p in range(1, 9):
            pawn = Pawn(
                color=self.color, position=Position(horizontal=pawn_row, vertical=p)
            )
            self.pieces.append(pawn)

        for r in [1, 8]:
            rook = Rook(
                color=self.color, position=Position(horizontal=king_row, vertical=r)
            )
            self.pieces.append(rook)

        for k in [2, 7]:
            knight = Knight(
                color=self.color, position=Position(horizontal=king_row, vertical=k)
            )
            self.pieces.append(knight)

        for b in [3, 6]:
            bishop = Bishop(
                color=self.color, position=Position(horizontal=king_row, vertical=b)
            )
            self.pieces.append(bishop)

        queen = Queen(
            color=self.color, position=Position(horizontal=king_row, vertical=4)
        )
        self.pieces.append(queen)

        king = King(
            color=self.color, position=Position(horizontal=king_row, vertical=5)
        )
        self.pieces.append(king)

    def do_move(self, *, move: Move, board: Board):
        piece = board.positions[move.from_pos.get_key()]

        if piece is None:
            raise ValueError(f"There is no piece on {move.from_pos}")

        if piece.color != self.color:
            raise ValueError("On the from position is a piece of the other player")

        if not piece.is_valid_move(from_pos=move.from_pos, to_pos=move.to_pos, board=board):
            raise ValueError(f"You cannot move from {move.from_pos} to {move.to_pos}")

        board.positions[move.to_pos.get_key()] = piece
        board.positions[move.from_pos.get_key()] = None