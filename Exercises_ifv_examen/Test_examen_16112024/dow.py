

def day_of_the_week(year: int, month: int, day: int) -> int:
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7
    """
       Calculate the day of the week for a given date using an adjusted version of Zeller's Congruence.

       This function computes the day of the week for a given year, month, and day.
       The result is returned as an integer:
           - 1 = Monday
           - 2 = Tuesday
           - 3 = Wednesday
           - 4 = Thursday
           - 5 = Friday
           - 6 = Saturday
           - 7 = Sunday

       Leap years are correctly handled based on Gregorian calendar rules.

       Args:
           year (int): The year of the date (e.g., 2024).
           month (int): The month of the date (1 = January, ..., 12 = December).
           day (int): The day of the month (1-31).

       Returns:
           int: An integer representing the day of the week (1 = Monday, ..., 7 = Sunday).

       Author:
           Geoffrey Crapoen

       Date:
           November 16, 2024
       """
    #print(len(offset))
    if dow == 0:
        dow = 7

    return dow

print(day_of_the_week(2024, 11, 18))

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
