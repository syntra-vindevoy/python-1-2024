

def predict_next_number(numbers: str):

    """
    Function to predict the next number in a sequence of numbers

    parameters
    ----------
    numbers: str
        A string representing a sequence of numbers

    returns
    -------
    result: str
        the next number in the sequence of numbers

    author
    ------
        Chiel

    date
    ----
        16-11-2024
    """

    for i in range(10):
        result = ""
        length = len(numbers) #numeric bepalen van de lengte van string
        counter = 1

        for _ in range(1, length + 1):
            if _ < length and numbers[_] == numbers[_ - 1]:
                counter += 1
            else:
                result += str(counter) + numbers[_ - 1]
                counter = 1

        numbers = result
        print(numbers)

    return numbers

def main():
    predict_next_number("5")

if __name__ == "__main__":
    main()