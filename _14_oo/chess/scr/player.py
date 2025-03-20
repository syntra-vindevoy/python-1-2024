from board import Position
from color import Color
from piece import Pawn, Rook, Knight, Bishop, Queen, King


class Player:
    def __init__(self, *, name: str, color: Color):
        self.name = name
        self.color = color
        self.pieces = []

        pawn_row = "B" if self.color == "white" else "G"
        king_row = "A" if self.color == "white" else "H"

        for p in range(1, 9):
            pawn = Pawn(color = self.color, position = Position(pawn_row, p))
            self.pieces.append(pawn)

        for t in [1, 8]:
            rook = Rook(color = self.color, position = Position(king_row, t))
            self.pieces.append(rook)

        for k in [2, 7]:
            knight = Knight(color = self.color, position = Position(king_row, k))
            self.pieces.append(knight)

        for b in [3, 6]:
            bishop = Bishop(color = self.color, position = Position(king_row, b))
            self.pieces.append(bishop)

        queen = Queen(color = self.color, position = Position(king_row, 4))
        self.pieces.append(queen)

        king = King(color = self.color, position = Position(king_row, 5))
        self.pieces.append(king)