from dom import *  # importing our days of month


def day_number(year: int, month: int, day: int) -> int:

    number_of_day = 0               #Instead of init, add here number of days of current month

    for i in range(1, month, 1):
        number_of_day += days_of_month(year, i)

    number_of_day += day            #If you didn't init in the beginning, you can omit this line

    return number_of_day


def main():
    assert day_number(2020, 1, 1) == 1
    assert day_number(2020, 2, 1) == 32
    assert day_number(2020, 3, 1) == 61
    assert day_number(2020, 12, 31) == 366

    assert day_number(2022, 1, 1) == 1
    assert day_number(2022, 2, 1) == 32
    assert day_number(2022, 3, 1) == 60
    assert day_number(2022, 12, 31) == 365


if __name__ == "__main__":
    main()
