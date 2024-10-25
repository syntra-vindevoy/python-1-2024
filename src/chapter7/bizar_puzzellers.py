# Constants for bills and coins
BILLS = [500, 200, 100, 50, 20, 10, 5]
COINS = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]


def main():
    price = 2689

    # Handling bills
    used_bills, remaining_price = calculate_denominations(price, BILLS)

    # Handling coins
    used_coins, _ = calculate_denominations(remaining_price, COINS)

    # Printing reports
    print_report("Bills", used_bills)
    print_report("Coins", used_coins)


def print_report(denomination_type: str, denominations: dict):
    for denomination, count in denominations.items():
        print(f"{denomination_type} {denomination} * {count}")
    print()


def calculate_denominations(amount: float, denominations: list, index: int = 0, used_denominations=None) -> tuple:
    if used_denominations is None:
        used_denominations = {}

    if index >= len(denominations):
        return used_denominations, amount

    denomination = denominations[index]
    count = amount // denomination
    if count > 0:
        used_denominations[denomination] = int(count)
        amount %= denomination

    return calculate_denominations(amount, denominations, index + 1, used_denominations)


if __name__ == '__main__':
    main()
