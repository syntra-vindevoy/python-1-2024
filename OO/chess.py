from abc import ABC, abstractmethod


# Abstract Schaakstuk Klasse
class Piece(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def validate_move(self, from_pos: tuple, to_pos: tuple, board) -> bool:
        pass

    @abstractmethod
    def symbol(self) -> str:
        pass


# Concrete Schaakstukken (hier blijven andere stukken exact hetzelfde zoals Pawn, Rook, etc.)
class Pawn(Piece):
    def symbol(self):
        return "♟" if self.color == "black" else "♙"

    def validate_move(self, from_pos, to_pos, board):
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1
        if from_pos[1] == to_pos[1]:
            if from_pos[0] + direction == to_pos[0]:
                return board.board[to_pos[0]][to_pos[1]] is None
            if from_pos[0] == start_row and from_pos[0] + 2 * direction == to_pos[0]:
                intermediate_square = board.board[from_pos[0] + direction][from_pos[1]]
                return intermediate_square is None and board.board[to_pos[0]][to_pos[1]] is None
        return False


class Rook(Piece):
    def symbol(self):
        return "♜" if self.color == "black" else "♖"

    def validate_move(self, from_pos, to_pos, board):
        if from_pos[0] != to_pos[0] and from_pos[1] != to_pos[1]:
            return False
        return True


class Knight(Piece):
    def symbol(self):
        return "♞" if self.color == "black" else "♘"

    def validate_move(self, from_pos, to_pos, board):
        dx = abs(from_pos[0] - to_pos[0])
        dy = abs(from_pos[1] - to_pos[1])
        return (dx, dy) in [(2, 1), (1, 2)]


class Bishop(Piece):
    def symbol(self):
        return "♝" if self.color == "black" else "♗"

    def validate_move(self, from_pos, to_pos, board):
        dx = abs(from_pos[0] - to_pos[0])
        dy = abs(from_pos[1] - to_pos[1])
        return dx == dy


class Queen(Piece):
    def symbol(self):
        return "♛" if self.color == "black" else "♕"

    def validate_move(self, from_pos, to_pos, board):
        dx = abs(from_pos[0] - to_pos[0])
        dy = abs(from_pos[1] - to_pos[1])
        return dx == dy or from_pos[0] == to_pos[0] or from_pos[1] == to_pos[1]


class King(Piece):
    def symbol(self):
        return "♚" if self.color == "black" else "♔"

    def validate_move(self, from_pos, to_pos, board):
        dx = abs(from_pos[0] - to_pos[0])
        dy = abs(from_pos[1] - to_pos[1])
        return max(dx, dy) == 1


# Added: definition of Player class before it is used
class Player:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


# (Het resterende deel van Board en Game klassen blijft hetzelfde)

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            self.board[1][i] = Pawn("black")
            self.board[6][i] = Pawn("white")

        self.board[0][0] = self.board[0][7] = Rook("black")
        self.board[7][0] = self.board[7][7] = Rook("white")

        self.board[0][1] = self.board[0][6] = Knight("black")
        self.board[7][1] = self.board[7][6] = Knight("white")

        self.board[0][2] = self.board[0][5] = Bishop("black")
        self.board[7][2] = self.board[7][5] = Bishop("white")

        self.board[0][3] = Queen("black")
        self.board[7][3] = Queen("white")

        self.board[0][4] = King("black")
        self.board[7][4] = King("white")

    def print_board(self):
        print("    a   b   c   d   e   f   g   h")
        print("  +--------------------------------")
        for row_idx, row in enumerate(self.board):
            row_display = f"{8 - row_idx} |"
            for piece in row:
                cell_symbol = piece.symbol() if piece else '.'
                row_display += f" {cell_symbol.center(4)}"
            print(row_display)
        print("  +--------------------------------")

    def move_piece(self, from_pos, to_pos):
        piece = self.board[from_pos[0]][from_pos[1]]
        target_piece = self.board[to_pos[0]][to_pos[1]]

        if piece is None:
            print("Geen stuk om te verplaatsen op de gekozen positie.")
            return False

        if target_piece and piece.color == target_piece.color:
            print("Kan niet naar positie verplaatsen waar eigen stuk staat.")
            return False

        if not piece.validate_move(from_pos, to_pos, self):
            print(f"Ongeldige zet voor {piece.symbol()} van {from_pos} naar {to_pos}.")
            return False

        self.board[to_pos[0]][to_pos[1]] = piece
        self.board[from_pos[0]][from_pos[1]] = None
        return True


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "white"), Player("Player 2", "black")]
        self.current_turn = 0

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def play_turn(self):
        player = self.players[self.current_turn]
        print(f"\n{player.name}'s beurt ({player.color}).")
        self.board.print_board()
        from_input = input("Van positie (bv 6 0): ")
        to_input = input("Naar positie (bv 4 0): ")
        from_pos = tuple(map(int, from_input.split()))
        to_pos = tuple(map(int, to_input.split()))
        if self.board.move_piece(from_pos, to_pos):
            print("Verplaatst succesvol!")
            self.switch_turn()
        else:
            print("Ongeldige zet. Probeer opnieuw.")

    def run_game(self):
        for _ in range(10):
            self.play_turn()
        print("Spel gestopt, voorbeeld voltooid.")


# Start het spel
if __name__ == "__main__":
    game = Game()
    game.run_game()
