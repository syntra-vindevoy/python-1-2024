# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Function to get the number of days in a month
def get_days_in_month(year, month):
    # Days in each month: January to December
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap_year(year):
        return 29
    return days_in_month[month - 1]


# Function to calculate the day of the week for the first day of the month
# Using Zeller's Congruence algorithm
def get_start_day(year, month):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    day = 1  # We are calculating for the 1st of the month
    start_day = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * j) % 7
    return (start_day + 5) % 7  # Adjust to make Sunday = 0


# Function to display the calendar of a specific month and year
def display_calendar(year, month):
    days_in_month = get_days_in_month(year, month)
    start_day = get_start_day(year, month)

    # Display month and year
    print(f"   {month:02d} - {year}")
    print("Su Mo Tu We Th Fr Sa")

    # Print leading spaces for the first day
    print("   " * start_day, end="")

    # Print each day of the month
    for day in range(1, days_in_month + 1):
        print(f"{day:2d} ", end="")
        if (start_day + day) % 7 == 0:
            print()  # Newline after Saturday

    print()  # Final newline for the next month


# Example usage
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
display_calendar(year, month)
