# leap year:
#           A year is a leap year if it is divisible by 4, but not divisible by 100,
#           unless it is also divisible by 400
def is_leap_year(year): # of hinted doe je zo (year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# DAYS IN MONTH
# Function to determine the number of days in a given month and year
def days_in_month(month, year):  # hinted: (month: int, year: int) -> int
    # Check if the month has 30 days (April, June, September, November)
    if month in [4, 6, 9, 11]:
        return 30  # These months have 30 days
    # Check if the month is February (month 2)
    elif month == 2:
        # If it's a leap year, February has 29 days
        if is_leap_year(year):
            return 29
        # If it's not a leap year, February has 28 days
        else:
            return 28
    # For all other months, return 31 days (January, March, May, July, etc.)
    return 31

# More concise function to determine days in a month using a list
def days_in_month2(month: int, year: int) -> int:
    # Create a list where each index corresponds to the number of days in each month.
    # February (index 1) gets 28 days, and we add 1 if it's a leap year.
    return [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
    # The list represents the number of days for each month from January (index 0) to December (index 11).
    # Access the correct number of days by subtracting 1 from the month number.


# bepalen welke dag van de week een maandag is
# Function to calculate the day of the week given a specific date
# year: The year as an integer (e.g., 2023)
# month: The month as an integer (1 = January, 2 = February, etc.)
# day: The day of the month as an integer (1, 2, 3, ..., 31)
def day_of_the_week(year: int, month: int, day: int) -> int:

    # Start counting total days from -1 because for Americans,
    # Sunday is day 0. We adjust this later for European (Belgian) days.
    total_days = -1

    # Loop through all the years from 1900 to the given year (not inclusive)
    # and count the total number of days.
    for y in range(1900, year):
        # If it's a leap year, add 366 days, otherwise add 365 days
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365

    # Loop through all months before the given month and add the number
    # of days in each month.
    for m in range(1, month):
        total_days += days_in_month(m, year)

    # Add the day of the month to the total days
    total_days += day

    # Return the remainder when total days are divided by 7 (this gives the weekday).
    # We add 1 because in Belgium, Monday is considered the first day of the week (1).
    return total_days % 7 + 1










# TESTEN
if __name__ == '__main__':
    #assert is_leap_year(2024) == True, "Test failed for year 2024"
    #assert is_leap_year(2000) == True, "Test failed for year 2000"
    #assert is_leap_year(2100) == True, "Test failed for year 2100"
    #assert is_leap_year(2025) == True, "Test failed for year 2025"

    print(day_of_the_week(1900, 1, 1))