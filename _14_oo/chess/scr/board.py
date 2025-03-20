from color import Color
from player import Player


class Position:
    def __init__(self, *, horizontal: str, vertical: int):
        assert horizontal.upper() in "ABCDEFGH"
        assert len(horizontal) == 1
        assert 1 <= vertical <= 8

        self.horizontal: int = ord(horizontal.upper()) - 64
        self.vertical: int = vertical

    def color(self):
        return Color("Black") if (self.horizontal + self.vertical) % 2 == 0 else Color("White")


class Move:
    def __init__(self, *, rom_pos: Position, to_pos: Position):
        self.from_pos = from_pos
        self.to_pos = to_pos


class Board:
    def __init__(self, *, pieces: list):
        self.pieces = pieces
        self.positions = {}
        self.setup()

    def setup(self):
        for piece in self.pieces:
            self.positions[piece.position] = piece

    def do_move(self, *, move: Move, player: Player):
        piece = self.positions[move.from_pos]

        if piece is None:
            raise ValueError(f"No piece at {move.from_pos}")

        if piece.color != player.color:
            raise ValueError(f"Player {player.name} cannot move piece of color {piece.color.name}")

        if not piece.is_valid_move(move.from_pos, move.to_pos, self):
            raise ValueError(f"Invalid move {move.from_pos} -> {move.to_pos}")

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
                pos = Position(horizontal, vertical)
                piece = self.get_piece(pos)

                if piece:
                    piece.draw(pos)
                else:
                    self.empty(pos)


