from dom import *  # importing our days of month


def day_number (year: int, month: int, day: int) -> int:
    """
    Args:
        year: The year as an integer, used to account for leap years.
        month: The month as an integer (1-12).
        day: The day of the month as an integer (1-31, depending on the month).

    Returns:
        The day of the year as an integer.
    """
    days = day
    for i in range (1, month):
        days += days_of_month (year, i)
    return days


def main ():
    assert day_number (2020, 1, 1) == 1
    assert day_number (2020, 2, 1) == 32
    assert day_number (2020, 3, 1) == 61
    assert day_number (2020, 12, 31) == 366

    assert day_number (2022, 1, 1) == 1
    assert day_number (2022, 2, 1) == 32
    assert day_number (2022, 3, 1) == 60
    assert day_number (2022, 12, 31) == 365


if __name__ == "__main__":
    main ()
