class Color:
    def __init__(self, name: str):
        assert name in ["WHITE","BLACK"]

        self.name = name