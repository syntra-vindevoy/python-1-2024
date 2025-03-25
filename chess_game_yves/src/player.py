from board import Position
from color import Color

class Player:
    def __init__(self, name: str, color: Color):
        self.name = name
        self.color = color
        self.pieces = []

        pawn_row = "B" if self.color.name == "WHITE" else "G"
        king_row = "A" if self.color.name == "WHITE" else "H"

        for p in range(1,9):
            pawn = Pawn(color=self.color, position=Position(pawn_row, 1))
            self.pieces.append(pawn)

        for t in [1,8]:
            rook = Rook(color=self.color, position=Position(king_row, t))
            self.pieces.append(rook)

        for k in [2,7]:
            knight = Knight(color=self.color, position=Position(king_row, k))
            self.pieces.append(knight)


        for b in [3,6]:
            bishop = Bishop(color=self.color, position=Position(king_row, b))
            self.pieces.append(bishop)

        queen = Queen(color=self.color, position=Position(king_row, 4))
        self.pieces.append(queen)

        king = King(color=self.color, position=Position(king_row, 5))
        self.pieces.append(king)

    def do_move(self, move: Move, board: Board):
        piece = board.positions[move.from_pos]

        if piece is None:
            raise ValueError(f"there is no piece on {move.from_pos}")

        if piece.color != self.color:
            raise ValueError(f"On the from position is a piece of the other player")

        if not piece.valid_move(move.from_pos, move.to_pos, self):
            raise ValueError(f"you cannot move from {move.from_pos} to {move.to_pos}")
