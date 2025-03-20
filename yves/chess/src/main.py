from color import Color
from game import Game
from player import Player


def main():
    white = Color(name="white")
    black = Color(name="black")

    player_white = Player(name=input("Enter white player name: "), color=white)
    player_black = Player(name=input("Enter black player name: "), color=black)

    game = Game(player_white=player_white, player_black=player_black)
    game.start()


if __name__ == "__main__":
    main()
