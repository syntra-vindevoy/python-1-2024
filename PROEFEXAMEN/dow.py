def day_of_the_week(year: int, month: int, day: int) -> int:
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7

    if dow == 0:
        dow = 7
    """

        This function calculates the day of the week for any given date specified by year, month, and day. 
        
        Made a change to the old version because in Europe monday is day 1 & sunday is day 7
            ORIGINAL version: Sunday was day 0 & Saturday was day 6
            NEW version: Monday is now day 1 & Sunday is day 7
                -> dow == 0 case is adjusted to 7 to match a common convention where Sunday is represented as 7

        Notes:
            Versie: 1.0.0
            Autor: BESA03
            Date: 2024-10-22
           

        """
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
