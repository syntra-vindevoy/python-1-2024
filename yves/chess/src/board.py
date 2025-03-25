from move import Move
from player import Player
from position import Position


class Board:
    def __init__(self, *, pieces: list):
        self.pieces = pieces
        self.positions = {}
        self.setup()

    def setup(self):
        for piece in self.pieces:
            self.positions[piece.position.get_key()] = piece

        for horizontal in "CDEF":
            for vertical in range(1, 9):
                pos = Position(horizontal=horizontal, vertical=vertical)
                self.positions[pos.get_key()] = None

    def get_piece(self, *, position: Position):
        key = position.get_key()
        if key in self.positions:
            return self.positions[key]
        else:
            return None


    def draw(self):
        for horizontal in "ABCDEFGH"[::-1]:
            for vertical in range(1, 9):
                pos = Position(horizontal=horizontal, vertical=vertical)
                piece = self.get_piece(position=pos)

                if piece:
                    print(piece.draw(pos), end="")
                else:
                    print(" ", end="")

            print("")
