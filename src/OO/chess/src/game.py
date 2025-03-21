from move import Move

from board import Board
from player import Player
from position import Position


class Game:
    def __init__(self, *, player_white: Player, player_black: Player):
        self.player_white = player_white
        self.player_black = player_black

        self.board = Board(pieces=player_white.pieces + player_black.pieces)

        self.is_finished = False
        self.player_to_move = self.player_white

    def start(self):
        self.board.draw()

        while not self.is_finished:
            self.ask_move()

    def ask_move(self):
        print(
            "Player to move:",
            self.player_to_move.name,
            "playing",
            self.player_to_move.color.name,
        )
        m = input("Enter move: (e.g. a2a4) ")
        from_pos = Position(horizontal=m[0], vertical=int(m[1]))
        to_pos = Position(horizontal=m[2], vertical=int(m[3]))
        move = Move(from_pos=from_pos, to_pos=to_pos)

        self.board.do_move(move=move, player=self.player_to_move)
        self.board.draw()
        # check for mate, which puts the game.is_finished == True

        if self.is_finished:
            print("Game is finished,", self.player_to_move.name, "won!")
            return

        if self.player_to_move == self.player_white:
            self.player_to_move = self.player_black
        else:
            self.player_to_move = self.player_white
