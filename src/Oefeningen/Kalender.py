#Global var
#Days = ["za", "Zo", "Ma", "Di", "Wo", "Do", "Vr"]
Days = [ "Ma", "Di", "Wo", "Do", "Vr","za", "Zo"]
Months: list[str] = [
    "Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober", "November",
    "December"
]

def draw (*,days_to_print:int, first_day_to_print:int, month_to_print:int, year_to_print:int)->None:
    """
    Draws a calendar for the specified month and year.

    Args:
        days_to_print: The number of days in the month to be printed.
        first_day_to_print: The index of the first day of the month.
        month_to_print: The month to be printed (1-based index).
        year_to_print: The year to be printed.
    """
    def make_banner_days (first_day: int):
        """
        Make a string with day starting from first day
        Args:
            first_day:

        Returns:
            output:
        """
        output_banner = ""
        for i in range (first_day, len (Days)):
            output_banner += f"{Days[i]} "
        for i in range (0, first_day):
            output_banner += f"{Days[i]} "
        return output_banner

    #Draw calendar month

    print (f"Month {Months[month_to_print - 1]} Year {year_to_print}")
    output = make_banner_days (first_day_to_print) + "\n"
    for day_count in range (1, days_to_print):
        output += f"{day_count:02d} "
        if day_count % 7 == 0:
            output += "\n"
    print (output)


def draw_intented (*, days_to_print: int, first_day_to_print: int, month_to_print: int, year_to_print: int) -> None:
    """
    Args:
        days_to_print: The total number of days in the month to print.
        first_day_to_print: The position of the first day in the week (1 for Monday, 7 for Sunday).
        month_to_print: The numeric representation of the month to print (1 for January, 12 for December).
        year_to_print: The year for which the calendar month is to be printed.
    """
    def make_banner_days (first_day: int):
        """
        Make a string with day starting from first day
        Args:
            first_day:

        Returns:
            output:
        """
        output_banner = ""
        for i in range (0, len (Days)):
            output_banner += f"{Days[i]} "
        return output_banner

    # Draw calendar month
    line_counter= first_day_to_print
    print (f"Month {Months[month_to_print - 1]} Year {year_to_print}")
    output = make_banner_days (first_day_to_print) + "\n"
    output += "   " * (first_day_to_print - 1)
    for day_count in range (1, days_to_print+1):
        output += f"{day_count:02d} "
        if line_counter % 7 == 0:
                output += "\n"
        line_counter += 1
    print (output)



def is_leap_year (year:int)->bool:
    """
    Args:
        year: An integer representing the year to be checked.

    Returns:
        A boolean value where True indicates that the year is a leap year, and False otherwise.

    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert is_leap_year(2024) == True
assert is_leap_year(2025) == False

def dow(year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    v = round((year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[v]

assert dow(2024,10,15) == "Tuesday"

def calculate_day_of_week (day, month, year):
    """
    Args:
        day: The day of the date.
        month: The month of the date.
        year: The year of the date.

    Returns:
        An integer representing the day of the week, where 0 represents Sunday, 1 represents Monday, and so on up to 6 which represents Saturday.
    """
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    v = (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7

    return v

print(calculate_day_of_week(1, 3, 2024))


def days_in_month (month_to_display:int, year:int) -> int:
    """
    Args:
        month_to_display: The month for which the number of days is to be calculated. Should be an integer between 1 and 12 inclusive.
        year: The year for which the days in the month are to be calculated. Used to determine if it is a leap year.

    Returns:
        The number of days in the specified month for the specified year. Accounts for leap years when February is selected.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year (year) and month_to_display == 2:
        return 29
    else:
        return month_days[month_to_display - 1]

assert days_in_month(2, 2024) == 29
assert days_in_month(2, 2023) == 28
assert days_in_month(1, 2023) == 31
assert days_in_month(4, 2023) == 30


def main ():
    """
    Main function to display a calendar for a given month and year.

    It calculates the number of days in the specified month, determines the day of the week on which the month starts, and then passes these values to a function that draws the calendar.

    Args:
      None

    Returns:
      None. Displays the calendar to the console output.
    """
    month_to_display = 6
    year_to_display = 1988
    draw_intented (days_to_print=days_in_month(month_to_display, year_to_display),
          month_to_print=month_to_display, year_to_print=year_to_display,
          first_day_to_print=calculate_day_of_week (1, month_to_display, year_to_display))


if __name__ == '__main__':
    main ()
