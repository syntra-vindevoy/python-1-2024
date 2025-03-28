from player import player


class game:
    # create players
    Player1 = player(input("Player 1, enter your name: "))
    Player2 = player(input("Player 2, enter your name: "))

    # ceate boards
    Player1.create_board()
    Player2.create_board()
