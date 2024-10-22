from dom import *  # importing our days of month

from leapyear import is_leap_year


def day_number(year: int, month: int, day: int) -> int:
    start_year = 2020
    start_month = 1
    start_day = 1
    start_day_of_week = 3

    day_count = 0

    # for y in range(start_year, year):
    #    day_count += 366 if is_leap_year(y) else 365
    # this code is not needed... always calculating in the same year

    for m in range(start_month, month):
        day_count += days_of_month(year, m)
    day_count += day - start_day + 1

    return day_count
    # return day_count


def main():
    assert day_number(2020, 1, 1) == 1
    assert day_number(2020, 2, 1) == 32

    assert day_number(2020, 3, 1) == 61
    assert day_number(2020, 12, 31) == 366

    assert day_number(2022, 1, 1) == 1
    assert day_number(2022, 2, 1) == 32
    assert day_number(2022, 3, 1) == 60
    assert day_number(2022, 12, 31) == 365
    print('day_number.py ok')


if __name__ == "__main__":
    main()
