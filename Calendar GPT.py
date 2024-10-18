def is_leap_year(year):
    """Check if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    """Return the number of days in a given month and year."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0  # Invalid month


def print_calendar(month, year):
    """Print the calendar for a given month and year."""
    # Days of the week
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Print header
    print(f"\nCalendar for {month}/{year}")
    print(" ".join(days))

    # Start day of the month (assuming the 1st is a Sunday for simplicity)
    start_day = 0  # 0 = Sunday, 1 = Monday, ..., 6 = Saturday

    # Number of days in the month
    days_count = days_in_month(month, year)

    # Print leading spaces for the first week
    for _ in range(start_day):
        print("     ", end="")  # 5 spaces for each day

    # Print days of the month
    for day in range(1, days_count + 1):
        print(f"{day:5}", end="")  # Format to right-align numbers
        start_day += 1

        # Move to next line after Saturday
        if start_day % 7 == 0:
            print()  # New line

    print()  # Final newline


# Example usage
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
print_calendar(month, year)