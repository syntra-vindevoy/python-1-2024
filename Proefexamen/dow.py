def day_of_the_week(year: int, month: int, day: int) -> int:
    """
    Determines the day of the week from our Japanese friend based on a given date.

    This function has been adjusted to conform to the European convention,
    where Monday is considered the first day of the week (day 1) and Sunday is
    considered the seventh day of the week (day 7).

    Parameters:
    year (int): The year part of the date.
    month (int): The month part of the date (1-12).
    day (int): The day part of the date (1-31).

    Returns
    -------
    int: The European-conventional weekday number (1 for Monday through 7 for Sunday).

    Example
    -------
    day_of_the_week(2023, 10, 9)
    1  # Monday

    Notes
    -----
    Author: Tom Van de Vyver
    Date : 2024-10-10
    Version: 0.0.1
    """
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7

    if dow == 0:
        dow = 7

    return dow


def main():
    assert day_of_the_week(2022, 12, 1) == 4  # Thu
    assert day_of_the_week(2022, 12, 2) == 5  # Fri
    assert day_of_the_week(2022, 12, 3) == 6  # Sat
    assert day_of_the_week(2022, 12, 4) == 7  # Sun
    assert day_of_the_week(2022, 12, 5) == 1  # Mon
    assert day_of_the_week(2022, 12, 6) == 2  # Tue
    assert day_of_the_week(2022, 12, 7) == 3  # Wed


if __name__ == "__main__":
    main()
