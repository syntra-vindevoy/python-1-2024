from position import Position


class Move:
    def __init__(self, *, from_pos: Position, to_pos: Position):
        self.from_pos = from_pos
        self.to_pos = to_pos