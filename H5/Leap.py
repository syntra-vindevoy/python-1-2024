def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Leap year cases
assert is_leap_year(2020) == True, "Test Case 1 Failed: 2020 is a leap year"
assert is_leap_year(2000) == True, "Test Case 2 Failed: 2000 is a leap year (divisible by 400)"
assert is_leap_year(1600) == True, "Test Case 3 Failed: 1600 is a leap year (divisible by 400)"

# Non-leap year cases
assert is_leap_year(1900) == False, "Test Case 4 Failed: 1900 is not a leap year (divisible by 100 but not 400)"
assert is_leap_year(2021) == False, "Test Case 5 Failed: 2021 is not a leap year"
assert is_leap_year(2100) == False, "Test Case 6 Failed: 2100 is not a leap year (divisible by 100 but not 400)"

def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 31

# More compact version using a list (days_in_month2)
def days_in_month2(month: int, year: int) -> int:
    return [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
    # if it's a leap year, `is_leap_year(year)` returns `True` (which is `1` in boolean logic), so 28 + 1 becomes 29

# Testing the functions
print(days_in_month(12, 1996))  # Should print 31 (December has 31 days)
print(days_in_month2(2, 2020))  # Should print 29 (February in a leap year)
print(days_in_month2(2, 2021))  # Should print 28 (February in a non-leap year)

def day_of_the_week(year: int, month: int, day: int) -> int:
    """
    This function calculates the day of the week for a given date using a simple
    algorithm. It returns an integer corresponding to the day (e.g., 1 for Monday, 7 for Sunday).
    """

    # Initialize total_days with -1 because we assume 1st Jan 1900 is a Monday (total_days starts from 0).
    total_days = -1

    # Loop through each year from 1900 to the input year (exclusive).
    # Add 366 days for leap years, and 365 days for non-leap years.
    for y in range(1900, year):
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365

    # Loop through each month of the input year, up to the given month.
    # Add the number of days in each month to total_days.
    for m in range(1, month):
        total_days += days_in_month(m, year)

    # Finally, add the days in the current month to total_days.
    total_days += day

    # Return the day of the week as an integer between 1 (Monday) and 7 (Sunday).
    return total_days % 7 + 1

if __name__ == "__main__":
    # Test the function with some dates.
    print(day_of_the_week(1900, 1, 1))  # Expected output: 1 (Monday)
    print(day_of_the_week(2024, 10, 15))  # Test another date.

def down(year, month, day):
    """
    This function uses a mathematical algorithm (Zeller's Congruence) to compute
    the day of the week for a given date. The result is returned as an integer (0 = Sunday, 6 = Saturday).
    """
    # Precomputed month adjustment values for the algorithm.
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    # Adjust year if the month is January or February (because the year starts from March).
    year -= month < 3

    # Apply Zeller's formula to calculate the day of the week.
    v = (year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7

if __name__ == "__main__":
    # Test the function with some dates.
    print(day_of_the_week(1900, 1, 1))  # Expected output: 1 (Monday)
    print(day_of_the_week(2024, 10, 15))  # Test another date.