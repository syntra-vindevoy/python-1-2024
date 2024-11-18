# DOCSTRING
"""
        This function calculates the days of the week. We based ourselves on the Tomohiko
        Sakamotho's Algorithm.

    :param year
        int: The year we would like to know
    :parameter month
        int: The month we would like to know
    : parameter day
        int: The day we would like to know
    return:
        int: The day of the week

    Notes:
        Author: Marta
        Date: 2024-11-02
        Version: 1.0.0

"""


def day_of_the_week(year: int, month: int, day: int) -> int:
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month - 1] + day) % 7
    if dow != 0:  # In Europe we use monday as the first day in the week and not sunday
        else dow = 7  # In  Europe we use sunday as the last day of the week and not saturday
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