from board import Board
from player import Player


class Game:
    def __init__(self, player_white: Player, player_black: Player):
        self.player_white = player_white
        self.player_black = player_black

        self.board = Board()

        self.is_finished = False
        self.player_to_move = self.player_white

    def start(self):
        while not self.is_finished:
            self.board.draw()
            self.ask_move()

    def ask_move(self):
        print("Player to move: ", self.player_to_move.name, "playing", self.player_to_move.color.name)
        _ = input("Enter move: ")

        # play the move

        if self.is_finished:
            print("Game is finished", self.player_to_move.name, "won!")
            return

        if self.player_to_move == self.player_white:
            self.player_to_move = self.player_black
        else:
            self.player_to_move = self.player_white