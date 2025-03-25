from position import Position


class Board:
    def __init__(self, *, pieces: list):
        self.pieces = pieces
        self.positions = {}
        self.setup()

    def setup(self):
        for piece in self.pieces:
            self.positions[piece.position] = piece



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
