def day_of_the_week(year: int, month: int, day: int) -> int:
    """
            calculate witch day of the week we are.

            it uses the Tomohiko Sakamoto’s Algorithm to find the number of the day of the week.

            Returns:
                int: the number of the day of the week.

            Examples:
                day_of_the_week(2022, 12, 1) -> 4

            Version: 1.0.0
 #          Author: bgeeroms
 #          Date: 2024-10-22
    """
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7

    # In europe monday is the first day of the week,
    # the original function above is from japan, here sunday is the first day of the week
    # in the function above, when the modulo is 0, its sunday, in Europe day 7, so wo rematch 0 to 7 for sunday
    # the other modulo is correct. 1 for monday, 2 for tuesday
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
