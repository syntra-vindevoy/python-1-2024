
import random

def guessing_game():
    number_to_guess = random.randint(1, 10000)
    low = 1
    high = 10000
    guess = 0
    guesses = 0

    while guess != number_to_guess:
        # Calculate the middle point for the next guess
        guess = (low + high) // 2
        guesses += 1
        print(f"Attempt {guesses}: Guessing {guess}")

        if guess < number_to_guess:
            print("Higher")
            low = guess + 1
        elif guess > number_to_guess:
            print("Lower")
            high = guess - 1
        else:
            print(f"Congratulations! The number was {number_to_guess}. Found in {guesses} attempts.")

def main():
    guessing_game()

if __name__ == "__main__":
    main()