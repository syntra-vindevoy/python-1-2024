from color import Color
from game import Game
from player import Player


def main():
    white = Color("white")
    black = Color("black")

    player_white = Player(input("Enter white player name: "), white)
    player_black = Player(input("Enter black player name: "), black)

    game = Game(player_white, player_black)
    game.start()


if __name__ == "__main__":
    main()