def day_of_the_week(year: int, month: int, day: int) -> int:
    """
    Determine the day of the week for a given date.

    This function calculates the day of the week based on the input
    year, month, and day. The result is represented as follows:
    1: Monday, 2: Tuesday, ..., 7: Sunday.

    This implementation was adapted to reflect that in Europe,
    Monday is considered the first day of the week (1)
    and Sunday is the seventh day (7).

    Args:
        year (int): The year of the date.
        month (int): The month of the date (1-12).
        day (int): The day of the month (1-31).

    Returns:
        int: An integer representing the day of the week (1=Monday, ..., 7=Sunday).

    Author: Onze Japanse vriend
    Date: In de jaren stillekes
    """

    # Offsets for the days of the week; adjusted for Monday as day 1.
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    # Adjust the year if the month is January or February,
    # because those months are considered part of the previous year.
    year -= month < 3

    # Calculate the day of the week using Zeller's Congruence formula,
    # resulting in dow = 0 for Sunday, ..., dow = 6 for Saturday.
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month - 1] + day) % 7

    # Adjust the output so that dow = 7 represents Sunday instead of dow = 0.
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
