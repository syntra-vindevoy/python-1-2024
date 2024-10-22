from day_number import day_number
from dow import day_of_the_week


def week_number(year: int, month: int, day: int) -> int:
    dow_jan1 = day_of_the_week(year, 1, 1)
    days = day_number(year, month, day)
    week = ((dow_jan1 - 2 + days) // 7) + 1
    return week


def main():
    assert week_number(2022, 1, 1) == 1
    assert week_number(2022, 1, 3) == 1
    assert week_number(2022, 12, 31) == 53


if __name__ == "__main__":
    main()