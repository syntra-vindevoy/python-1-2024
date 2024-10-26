from typing import Dict


def payment(amount: int) -> Dict[int, int]:
    money_list = [500, 100, 50, 20, 10, 5, 2, 1]
    money_dict = {
        500: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0,
    }
    for money in money_list:
        while amount >= money:
            amount -= money
            money_dict[money] += 1
    return money_dict


def print_payment(money_dict: Dict[int, int]) -> None:
    for money, count in money_dict.items():
        if count > 0:
            print(f"{money}: {count}")


def print_amount(amount: int) -> None:
    print(amount)
    print_payment(payment(amount))
    print()


def tests():
    assert payment(620) == {500: 1, 100: 1, 50: 0, 20: 1, 10: 0, 5: 0, 2: 0, 1: 0}
    assert payment(999) == {500: 1, 100: 4, 50: 1, 20: 2, 10: 0, 5: 1, 2: 2, 1: 0}


def main():
    tests()

    print_amount(500)
    print_amount(620)
    print_amount(999)


if __name__ == "__main__":
    main()
