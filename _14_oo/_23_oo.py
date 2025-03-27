def guess_number(number:int) -> None:
    if type(number) != int:
        raise TypeError("number must be an integer")

    if number < 0 or number > 10:
        raise ValueError("number must be between 0 and 10")

    print("You guessed it!", number)

def main():
    guess_number(5)
    guess_number(11)

if __name__ == "__main__":
    main()