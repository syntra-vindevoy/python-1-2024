from game import Game
from player import Player
from color import Color


def main():
    white = Color('WHITE')
    black = Color('BLACK')
    player_white = Player(input("give white player name: "))
    player_black = Player(input("give black player name: "))

    game = Game(player_white, player_black)
    game.start()


if __name__ == "__main__":
    main()
