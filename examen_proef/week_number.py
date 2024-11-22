from dow import day_of_the_week
from day_number import day_number


def week_number(year: int, month: int, day: int):
    dow = day_of_the_week(year, 1, 1)
    days = day_number(year, month, day)
    week = (dow - 2 + days) // 7
    week += 1
    return week


def main():
    assert week_number(2022, 1, 1) == 1


if __name__ == "__main__":
    main()
