from board import Board, Move
from chess_game.src.board import Position
from player import Player

class Game:
    def __init__(self, player_white: Player, player_black: Player):
        self.player_to_move = player_to_move
        self.player_white = player_white
        self.player_black = player_black

        self.board = Board(player_white.pieces + player_black.pieces)

        self.is_finished = False
        self.payer_to_move = self.player_white

    def start(self):
        while not self.is_finished:
            pass

    def ask_move(self):
        print("Player to move: ",self.payer_to_move.name, "playing", 
              self.player_to_move.color.name)
        m = input("Enter move: (e.g. a2a4")
        from_pos = Position(m[0], int(m[1]))
        to_pos = Position(m[2], int(m[3]))
        move = Move(from_pos, to_pos)

        self.board.do_move(move, self.player_to_move)
        self.board.draw()

        #play the move
        self.board.draw()

        #check for mate, which puts the game.is_finished == true

        if self.payer_to_move == self.player_white:
            self.payer_to_move = self.player_black
        else:
            self.payer_to_move = self.player_white