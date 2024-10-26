from Proefexamen.dow import day_of_the_week
from Proefexamen.dom import days_of_month
from Proefexamen.day_number import day_number
from Proefexamen.date_string import name_of_month, name_of_day


def print_month_calendar(year, month):
    # Get the number of days in the month
    num_days = days_of_month(year, month)

    # Get the name of the month
    month_name = name_of_month(month)

    # Print the month and year
    print(f"{month_name} {year}".center(20, ' '))

    # Print the days of the week header
    for i in range(1, 8):
        print(name_of_day(i).center(3, ' '), end=' ')
    print()

    # Find out the start day of the week for the 1st of the month
    start_day = day_of_the_week(year, month, 1)

    # Print initial spacing for the first day
    for _ in range(start_day - 1):
        print("   ", end=' ')

    # Print all days of the month
    for day in range(1, num_days + 1):
        # Adjust spacing for single-digit days
        print(str(day).rjust(3, ' '), end=' ')

        # Go to the next line at the end of the week
        if (start_day + day - 1) % 7 == 0:
            print()

    # Print a new line for the last week
    print()


def print_year_calendar(year):
    for month in range(1, 13):
        print_month_calendar(year, month)
        print('\n' + '-' * 20 + '\n')  # Separation line between months


# Example usage
print_year_calendar(2024)
