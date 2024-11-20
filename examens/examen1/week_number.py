from examens.examen1.dom import days_of_month
from examens.examen1.dow import day_of_the_week


def week_number (year: int, month: int, day: int):
    def day_of_year (year, month, day):
        """Calculate the day of the year."""

        doy = 0
        for m in range (month - 1):
            doy += days_of_month (year, m + 1)
        doy += day
        return doy

    doy = day_of_year (year, month, day)

    # Calculate the week number (DOW should be 0 = Monday, 6 = Sunday)
    week_number = (doy - (day_of_the_week (year, month, day) - 1) + 10) // 7

    return week_number + 1


def main ():
    assert week_number (2022, 1, 1) == 1
    assert week_number (2022, 1, 3) == 2
    assert week_number (2022, 2, 21) == 9


if __name__ == "__main__":
    main ()
