def day_of_the_week(year: int, month: int, day: int) -> int:
    """
    Calculate the day of the week for a given date.

    This function computes the day of the week for a given date using Zeller's Congruence,
    with Monday as the first day of the week (1) and Sunday as the last day of the week (7).
    It adjusts for leap years by treating January and February as months of the previous year.

    Parameters
    ----------
    year : int
        The year of the date (e.g., 2024).
    month : int
        The month of the date (1 for January, 12 for December).
    day : int
        The day of the month.

    Returns
    -------
    int
        The day of the week as an integer where 1 = Monday, ..., 7 = Sunday.

    Notes
    -----
    This function applies a slight adjustment to Zeller's Congruence to map the result from
    a Sunday-first system (where Sunday = 0) to a Monday-first system (where Monday = 1).

    Author: Kenneth
    Date: 22/10/2024
    Version: 1.0.0

    """
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7

    if dow == 0: #adjustment because we count monday as day 1 instead of sunday
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
    
