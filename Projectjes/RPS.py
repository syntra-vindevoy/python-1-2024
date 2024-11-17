import sys
import random
from enum import Enum


def play_rps():

    class rps(Enum):
        rock = 1
        paper = 2
        scissors = 3

    playerchoice = input(
        "\nEnter... \n1 for rock, \n2 for paper, \n3 for scissors:\n\n") #\n is new line

    if playerchoice not in ["1", "2", "3"]:
        print("you must enter 1, 2 or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(rps(player)).replace('rps.', '').title() + ",")
    print("python chose " + str(rps(computer)).replace('rps.', '').title() + ",")

    if player == 1 and computer == 3:
        print("You Win!")
    elif player == 2 and computer == 1:
        print("You Win!")
    elif player == 3 and computer == 2:
        print("You Win!")
    elif player == computer:
        print("Tie game, go again")
        return play_rps()
    else:
        print("You Lose!")

    print("Play again?")
    while True:
        playagain = input ("Y for Yes or Q to quit")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Thank you for playing")
        sys.exit("Bye!")

play_rps()
