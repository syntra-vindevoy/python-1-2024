from color import Color
from piece import Pawn, Rook, Knight, Bishop, Queen, King
from position import Position


class Player:
    def __init__(self, *, name: str, color: Color):
        self.name: str = name
        self.color: Color = color
        self.pieces: list = []

        # Set up the pieces in the correct positions
        # In chess, rank 1 is white's back row, rank 8 is black's back row
        # Pawns are on rank 2 for white, rank 7 for black
        
        pawn_rank = 2 if self.color.name == "WHITE" else 7
        back_rank = 1 if self.color.name == "WHITE" else 8

        # Create pawns
        for file in range(1, 9):  # Files A-H (1-8)
            pawn = Pawn(
                color=self.color, 
                position=Position(horizontal=chr(file + 64), vertical=pawn_rank)
            )
            self.pieces.append(pawn)

        # Create rooks
        for file in [1, 8]:  # Files A and H
            rook = Rook(
                color=self.color, 
                position=Position(horizontal=chr(file + 64), vertical=back_rank)
            )
            self.pieces.append(rook)

        # Create knights
        for file in [2, 7]:  # Files B and G
            knight = Knight(
                color=self.color, 
                position=Position(horizontal=chr(file + 64), vertical=back_rank)
            )
            self.pieces.append(knight)

        # Create bishops
        for file in [3, 6]:  # Files C and F
            bishop = Bishop(
                color=self.color, 
                position=Position(horizontal=chr(file + 64), vertical=back_rank)
            )
            self.pieces.append(bishop)

        # Create queen (on D1/D8)
        queen = Queen(
            color=self.color, 
            position=Position(horizontal='D', vertical=back_rank)
        )
        self.pieces.append(queen)

        # Create king (on E1/E8)
        king = King(
            color=self.color, 
            position=Position(horizontal='E', vertical=back_rank)
        )
        self.pieces.append(king)
