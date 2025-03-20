class Color:
    def __init__(self, *, name: str):
        assert name in ["white", "black"]
        self.name = name