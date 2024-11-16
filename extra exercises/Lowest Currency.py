def lowest_currency(amount: float | int):
    """

    Function to determine the lowest amount of physical currency for a given any given amount.

    parameters
    ----------

    amount: float | int
        Any given amount of money

    returns
    -------

    result: list
        a list with the amount needed of each available currency

    author
    ------
        Chiel

    date
    ----
        16-11-2024

    """

    currencies = [500 ,200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    result = []
    for currency in currencies:
        count = int(amount // currency)
        if count > 0:
            result.append((currency, count))
        amount = round(amount - (count * currency), 2)

    for currency, count in result:
        print(f"{count} x €{currency:.2f}")




def main():
    lowest_currency(777.76)

if __name__ == "__main__":
    main()