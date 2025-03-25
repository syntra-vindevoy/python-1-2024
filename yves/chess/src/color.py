class Color:
    def __init__(self, *, name: str):
        assert name.upper() in ["WHITE", "BLACK"]

        self.name = name.upper()

        if self.name == "WHITE":
            self.ansi_code = "\033[97m"  # Bright white
            # self.piece_color = "white"
        else:
            self.ansi_code = "\033[31m"  # Red (of kies een andere kleur voor zwart)
            # self.piece_color = "Red"