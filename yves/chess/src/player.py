from color import Color
from piece import Pawn, Rook, Knight, Bishop, Queen, King
from position import Position


class Player:
    def __init__(self, *, name: str, color: Color):
        self.name: str = name
        self.color: Color = color
        self.pieces: list = []

        pawn_row = "B" if self.color.name == "WHITE" else "G"
        king_row = "A" if self.color.name == "WHITE" else "H"

        for p in range(1, 9):
            pawn = Pawn(color=self.color, position=Position(horizontal=pawn_row, vertical=p))
            self.pieces.append(pawn)

        for r in [1, 8]:
            rook = Rook(color=self.color, position=Position(horizontal=king_row, vertical=r))
            self.pieces.append(rook)

        for k in [2, 7]:
            knight = Knight(color=self.color, position=Position(horizontal=king_row, vertical=k))
            self.pieces.append(knight)

        for b in [3, 6]:
            bishop = Bishop(color=self.color, position=Position(horizontal=king_row, vertical=b))
            self.pieces.append(bishop)

        queen = Queen(color=self.color, position=Position(horizontal=king_row, vertical=4))
        self.pieces.append(queen)

        king = King(color=self.color, position=Position(horizontal=king_row, vertical=5))
        self.pieces.append(king)
