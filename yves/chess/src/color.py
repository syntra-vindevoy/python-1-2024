class Color:
    def __init__(self, name: str):
        assert name.upper() in ["WHITE", "BLACK"]

        self.name = name.upper()
