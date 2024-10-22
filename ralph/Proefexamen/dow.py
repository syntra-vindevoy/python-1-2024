"""
    Calculates the day of the week for a given date using Zeller's congruence-like algorithm.

    Args:
        year (int): The year of the date.
        month (int): The month of the date (1 = January, 2 = February, etc.).
        day (int): The day of the month.

    Returns:
        int: The day of the week as an integer where:
             1 = Monday, 2 = Tuesday, ..., 7 = Sunday.

    Notes:
        - The algorithm adjusts the year if the month is January or February by treating them as
          months of the previous year (since in Zeller's congruence March is treated as the start
          of the year).
        - This function returns a result in the range [1, 7], where 1 is Monday and 7 is Sunday.

    Example:
        day_of_the_week(2023, 10, 22)
        7  # (Sunday)

    Author: Ralph Allaert
    Date: 2024-10-22
    Version: 1.0.0
    """

def day_of_the_week(year: int, month: int, day: int) -> int:

    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7

    if dow == 0: #In Europe Monday is day 1 and Sunday is day 7
        dow = 7  #In the US Sunday is day 1 -> becomes day because counting starts at 0

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
