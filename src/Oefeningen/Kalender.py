#Global var
Days = ["za", "Zo", "Ma", "Di", "Wo", "Do", "Vr"]
Months: list[str] = [
    "Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober", "November",
    "December"
]

def draw (*,days_to_print:int, first_day_to_print:int, month_to_print:int, year_to_print:int)->None:
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
        for i in range (1, first_day):
            output_banner += f"{Days[i]} "
        return output_banner

    #Draw calendar month

    print (f"Month {Months[month_to_print - 1]} Year {year_to_print}")
    output = make_banner_days (first_day_to_print) + "\n"
    for day_count in range (1, days_to_print):
        output += f"{day_count:02d} "
        if day_count % 6 == 0:
            output += "\n"
    print (output)

def is_leap_year (year:int)->bool:
    """
    Calculate if year is a leap year
    Args:
        year:

    Returns:
        bool
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert is_leap_year(2024) == True
assert is_leap_year(2025) == False

def calculate_day_of_week (day, month, year):
    """
        Calculate day of the week
    Args:
        day:
        month:
        year:

    Returns:
        day_of_week:
    """
    # January and February are treated as months 13 and 14 of the previous year
    if month < 3:
        month += 12
        year -= 1

    k = year % 100  # Year of the century
    j = year // 100  # Zero-based century

    f = day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    day_of_week = f % 7
    return day_of_week

assert calculate_day_of_week(9, 10, 2025) == 5


def days_in_month (month_to_display:int, year:int) -> int:
    """
     Get number of days in month
    Args:
        month_to_display:
        year:

    Returns:
        int
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
    month_to_display = 2
    year_to_display = 2018
    draw (days_to_print=days_in_month(month_to_display, year_to_display),
          month_to_print=month_to_display, year_to_print=year_to_display,
          first_day_to_print=calculate_day_of_week (year_to_display, month_to_display, 1))


if __name__ == '__main__':
    main ()
