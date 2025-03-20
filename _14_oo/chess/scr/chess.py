class Color:
    def __init__(self, name: str):
        assert name in ["white", "black"]

class Game:
    pass

class Board:
    def __init__(self):
        self.setup()

    def setup(self):
        pass

class Piece:
    def __init__(self, color: Color, position: Position):
        self.color = color
        self.position = position


class Pawn(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)
class Rook(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)


class Knight(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)


class Bishop(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)


class Queen(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)


class King(Piece):
    def __init__(self, color: Color, position: Position):
        super().__init__(color, position)



class Position:
    def __init__(self, horizontal: str, vertical: int):
        assert vertical >= 1 and vertical <= 8

        self.horizontal: int = ord(horizontal.upper()) - 64
        self.vertical: int = vertical


class Player:
    def __init__(self, name: str, color: Color):
        self.name = name
        self.color = color
        self.pieces = []

        pawn_row = "B" if self.color == "white" else "G"

        for p in range(1, 9):
            pawn = Pawn(color = self.color, position = Position(pawn_row, p))
            self.pieces.append(pawn)



class Move:
    pass

def main():
    white = Color("white")
    black = Color("black")

    player_white = Player(input("Enter white player name: "))
    player_black = Player(input("Enter black player name: "))



if __name__ == "__main__":
    main()