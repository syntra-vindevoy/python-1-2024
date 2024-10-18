# This function will ask which year you want to see the calendar of. This function needs to calculate if it's a leap year. To calculate leap year, check if divisible by 4, 100 and by 400a. If not, then is not leap year.
def leap_year(leap_year: int) -> int:
    year = input("Enter year:")
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return leap_year
    else


# A calendar shows the months, expressed as int

# A calendar shows the days in each month, expressed as int. A month has 30 or 31 days, except February which has 28 days or 29 days if it's a leap year.

# This function will need to print out a calendar in the form of a matrix showing you the month, year, days of the week including names of the days.