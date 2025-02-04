from random import randint

from ex_10_7 import has_duplicates


def get_birthdays(nbr: int):
    return [randint(1, 365) for _ in range(nbr)]


def test(nbr):
    same_birthdays = 0

    for i in range(nbr):
        birthdays = get_birthdays(23)
        # print(birthdays)
        if has_duplicates(birthdays):
            print(birthdays)
            same_birthdays += 1

    return same_birthdays, nbr


if __name__ == '__main__':
    s, n = test(10)

    print(s / n)
