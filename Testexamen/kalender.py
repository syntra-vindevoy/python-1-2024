from dom import days_of_month
from date_string import name_of_month, name_of_day
from dow import day_of_the_week
from week_number import week_number


def print_month(year: int, month: int):
    # Print month and year
    print(f"     {name_of_month(month)} {year}")
    print()  # Blank line

    # Print the days of the week using name_of_day
    print("W  ", end="")  # Add a column header for week numbers
    for i in range(1, 8):  # Loop through days 1 to 7
        print(name_of_day(i), end=" ")
    print()  # Newline after days of the week

    # Get the first day of the month to determine the starting position
    start_day = day_of_the_week(year, month, 1)  # Get the day of the week for the 1st of the month

    # Initialize the day counter and week number
    day = 1
    days = days_of_month(year, month)

    # Print initial spaces for the first row based on start_day
    print(f"{week_number(year, month, day):2} ", end="")  # Print the week number for the first row
    for _ in range(start_day - 1):  # Adjust for starting day (1 = Monday)
        print("   ", end="")

    # Print all the days of the month
    for day in range(1, days + 1):
        print(f"{day:2}", end=" ")  # Print the day, formatted to be 2 characters wide

        # Check if the end of the week is reached
        if (day + start_day - 1) % 7 == 0:  # Newline at the end of the week
            print()  # Move to the next line

            # Print the next week's number if not the last day of the month
            if day != days:
                print(f"{week_number(year, month, day + 1):2} ", end="")

                # Ensure to print a final newline if the last row didn't end the week
    if (days + start_day - 1) % 7 != 0:
        print()  # Add a newline if the last line of days is not complete

    print()  # Add an extra blank line after each month

def print_year(year: int):
    for month in range(1, 13):  # Loop through each month of the year
        print_month(year, month)  # Print the calendar for the month

# Call the function to print the calendar for the entire year 2022
print_year(2022)
