


def day_of_the_week(year: int, month: int, day: int) -> int:
    """
        Calculate the day of the week for a given date.

        This function implements Zeller's Congruence algorithm to determine the
        day of the week for any given date (year, month, day). The days of the
        week are encoded as integers from 1 to 7, starting with Monday as 1 and
        ending with Sunday as 7.

        Args:
            year (int): The year of the date. Must be a positive integer.
            month (int): The month of the date (1-12).
            day (int): The day of the month (1-31).

        Returns:
            int: The day of the week, where 1 = Monday, 2 = Tuesday, ..., 7 = Sunday.

        Example:
            #>>> day_of_the_week(2022, 12, 1)
            4  # Thursday
            #>>> day_of_the_week(2022, 12, 5)
            1  # Monday

        Note:
            The method adjusts the year and month in case the month is January or February
            to align with Zeller's Congruence requirements.

        Author:
            Chiel Vansompel
        """

    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7

    #sidchiv
    #added code to set day 1 as monday and the day 7 as sunday.
    #this now uses the european order of the week instead of the American way.

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
