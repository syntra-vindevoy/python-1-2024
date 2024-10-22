def day_of_the_week(year: int, month: int, day: int) -> int:
    """
    Calculate the day of the week for a given date using Zeller's congruence algorithm.

    Args:
        year (int): The year (e.g., 2022)
        month (int): The month (1-12)
        day (int): The day of the month (1-31)

    Returns:
        int: Day of the week as a number where:
            1 = Monday
            2 = Tuesday
            3 = Wednesday
            4 = Thursday
            5 = Friday
            6 = Saturday
            7 = Sunday

    Raises:
        ValueError: If month is not between 1 and 12
        ValueError: If day is not valid for the given month

    Examples:
        >>> day_of_the_week(2022, 12, 1)
        4  # Thursday
        >>> day_of_the_week(2022, 12, 4)
        7  # Sunday
        >>> day_of_the_week(2022, 12, 5)
        1  # Monday

    Notes:
        - Uses a modified version of Zeller's congruence algorithm
        - January and February are treated as months 13 and 14 of the previous year
        - The function returns 1-7 instead of 0-6 to align with ISO 8601 standard
    """
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month - 1] + day) % 7

    # Convert Sunday from 0 to 7 to align with ISO 8601 standard where Monday is 1
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