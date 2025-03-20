class Color:
    def __init__(self, name: str):
        assert name in ["white", "black"]


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
        assert horizontal.upper() in "ABCDEFGH"

        assert vertical >= 1 and vertical <= 8

        self.horizontal: int = ord(horizontal.upper()) - 64
        self.vertical: int = vertical


class Player:
    def __init__(self, name: str, color: Color):
        self.name = name
        self.color = color
        self.pieces = []

        pawn_row = "B" if self.color == "white" else "G"
        king_row = "A" if self.color == "white" else "H"

        for p in range(1, 9):
            pawn = Pawn(color = self.color, position = Position(pawn_row, p))
            self.pieces.append(pawn)

        for t in [1, 8]:
            rook = Rook(color = self.color, position = Position(king_row, t))
            self.pieces.append(rook)

        for k in [2, 7]:
            knight = Knight(color = self.color, position = Position(king_row, k))
            self.pieces.append(knight)

        for b in [3, 6]:
            bishop = Bishop(color = self.color, position = Position(king_row, b))
            self.pieces.append(bishop)

        queen = Queen(color = self.color, position = Position(king_row, 4))
        self.pieces.append(queen)

        king = King(color = self.color, position = Position(king_row, 5))
        self.pieces.append(king)



class Game:
    def __init__(self, player_white: Player, player_black: Player):
        self.player_white = player_white
        self.player_black = player_black

        self.is_finished = False
        self.player_to_move = self.player_white

    def start(self):
        while not self.is_finished:
            pass

    def ask_move(self):
        print("Player to move: ", self.player_to_move.name, "playing", self.player_to_move.color.name)
        n = input("Enter move: ")

        #play the move

        if self.is_finished:
            print("Game is finished", self.player_to_move.name, "won!")
            return

        if self.player_to_move == self.player_white:
            self.player_to_move = self.player_black
        else:
            self.player_to_move = self.player_white


class Move:
    pass

def main():
    white = Color("white")
    black = Color("black")

    player_white = Player(input("Enter white player name: "), white)
    player_black = Player(input("Enter black player name: "), black)

    game = Game(player_white, player_black)
    game.start()



if __name__ == "__main__":
    main()