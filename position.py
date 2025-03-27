from color import Color


class Position:
    def __init__(self, *, horizontal: str, vertical: int):
        assert horizontal.upper() in "ABCDEFGH"
        assert len(horizontal) == 1
        assert 1 <= vertical <= 8

        self.horizontal: int = ord(horizontal.upper()) - 64  # A=1, B=2, etc.
        self.vertical: int = vertical
    
    def color(self):
        """Get the color of the square at this position"""
        return (
            Color.BLACK
            if (self.horizontal + self.vertical) % 2 == 0
            else Color.WHITE
        )
    
    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.horizontal == other.horizontal and self.vertical == other.vertical
    
    def __hash__(self):
        return hash((self.horizontal, self.vertical))
    
    def __str__(self):
        return f"{chr(self.horizontal + 64)}{self.vertical}"
    
    def __repr__(self):
        return f"Position(horizontal='{chr(self.horizontal + 64)}', vertical={self.vertical})"
    
    def offset(self, dx, dy):
        """Create a new position with the given offset"""
        new_h = chr(self.horizontal + dx + 64)
        new_v = self.vertical + dy
        
        # Check if the new position is valid
        if new_h not in "ABCDEFGH" or not (1 <= new_v <= 8):
            return None
        
        return Position(horizontal=new_h, vertical=new_v)
    
    @staticmethod
    def from_algebraic(algebraic):
        """Create a position from algebraic notation (e.g. 'e4')"""
        assert len(algebraic) == 2
        horizontal = algebraic[0]
        vertical = int(algebraic[1])
        return Position(horizontal=horizontal, vertical=vertical)
