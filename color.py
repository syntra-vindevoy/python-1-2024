class Color:
    """Represents a color in the chess game"""
    
    # Class-level predefined colors
    WHITE = None
    BLACK = None
    
    def __init__(self, *, name: str):
        self.name = name.upper()
    
    def __eq__(self, other):
        if not isinstance(other, Color):
            return False
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def initialize_colors(cls):
        """Create singleton colors"""
        if cls.WHITE is None:
            cls.WHITE = Color(name="WHITE")
        if cls.BLACK is None:
            cls.BLACK = Color(name="BLACK")
