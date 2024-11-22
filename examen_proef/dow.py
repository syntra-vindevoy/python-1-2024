def day_of_the_week(year: int, month: int, day: int) -> int:
    '''
    param year: int: the year on which we calculate the day of the week
    param month: int: the month on which we calculate the day of the week
    param day: int: the day on which we calculate the day of the week

    return
        int: the number of the day of the week (starting with monday as 1)
        example: 1 for Monday, 2 for Tuesday, ..., 7 for Sunday.
    raises
        value-error...: (none)
    examples
        day_of_the_week(2022, 12, 1)
    Notes
        Date: 2024-10-22
        Author: Marijn Vandenholen
        Version: 1.0.0
        Bugfix: adjusted the offset to start with monday as 1

    '''
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month - 1] + day) % 7

    if dow == 0:
        dow = 7
    # modified 2024-10-22
    # The function should return 1 for Monday, 2 for Tuesday, ..., 7 for Sunday.
    # Marijn Vandenholen
    return dow


def main():
    assert day_of_the_week(2022, 12, 1) == 4  # Thu
    assert day_of_the_week(2022, 12, 2) == 5  # Fri
    assert day_of_the_week(2022, 12, 3) == 6  # Sat
    assert day_of_the_week(2022, 12, 4) == 7  # Sun
    assert day_of_the_week(2022, 12, 5) == 1  # Mon
    assert day_of_the_week(2022, 12, 6) == 2  # Tue
    assert day_of_the_week(2022, 12, 7) == 3  # Wed

    print('dow.py ok')


if __name__ == "__main__":
    main()
