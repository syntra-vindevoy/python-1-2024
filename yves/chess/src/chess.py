class Game:
    pass

class Board:
    def __init__(self):
        self.setup()

    def setup(self):
        pass

class Piece:
    pass

class Pawn(Piece):
    pass

class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

class Color:
    pass

class Position:
    def __init__(self, horizontal: str, vertical: int):
        self.horizontal: int = ord(horizontal.upper()) - 64
        self.vertical: int = vertical



class Player:
    def __init__(self, name: str):
        self.name = name

class Move:
    pass

def main():
    player_white = Player(input("Enter white player name: "))
    player_black = Player(input("Enter black player name: "))



if __name__ == "__main__":
    main()