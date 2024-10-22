from dow import *
from day_number import *

def week_number(year: int, month: int, day: int):
    dow = day_of_the_week(year, 1, 1)
    days = day_number(year, month, day)
    week = (dow - 2 + days) // 7
    return week + 1


def main():
    assert week_number(2022, 1, 1) == 1
    assert week_number(2022, 2, 28) == 10
    assert week_number(2022, 10, 22) == 43


if __name__ == "__main__":
    main()
