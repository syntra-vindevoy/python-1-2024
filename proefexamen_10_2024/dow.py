def day_of_the_week(year: int, month: int, day: int) -> int:
    """
    Calculate the day of the week for a given date.

    Parameters
    ----------
    year : int
        The year of the date.
    month : int
        The month of the date.
    day : int
        The day of the month.

    Returns
     -------
    int
        An integer representing the day of the week, where Monday is 1 and Sunday is 7.

    Examples
    --------
    >>> day_of_the_week(2023, 10, 22)
    7
    >>> day_of_the_week(2000, 1, 1)
    6

    Notes
    -----
    Author: Your Name
    Version: 1.0
    """

    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7

    #Code adjusted so it's according European convention that a monday is day 1
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
