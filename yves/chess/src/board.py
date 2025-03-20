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
            self.positions[piece.position] = piece

    def do_move(self, *,  move: Move, player: Player):
        piece = self.positions[move.from_pos]

        if piece is None:
            raise ValueError(f"There is no piece on {move.from_pos}")

        if piece.color != player.color:
            raise ValueError(f"On the from position is a piece of the other player")

        if not piece.valid_move(move.from_pos, move.to_pos, self):
            raise ValueError(f"You cannot move from {move.from_pos} to {move.to_pos}")

    def get_piece(self, *, position: Position):
        if position in self.positions:
            return self.positions[position]
        else:
            return None

    def empty(self, *, position: Position):
        pass

    def draw(self):
        for horizontal in "ABCDEFGH":
            for vertical in range(1, 9):
                pos = Position(horizontal=horizontal, vertical=vertical)
                piece = self.get_piece(position=pos)

                if piece:
                    piece.draw(pos)
                else:
                    self.empty(position=pos)


