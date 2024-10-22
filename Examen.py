def name_of_day(day: int) -> str:
    # Validate the input day
    if 1 <= day <= 7:
        return ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"][day - 1]  # Adjusting the order to match Monday as day 1
    else:
        raise ValueError("Day must be between 1 (Monday) and 7 (Sunday).")


def name_of_month(month: int) -> str:
    # Validate the input month
    if 1 <= month <= 12:
        return ["Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober",
                "November", "December"][month - 1]
    else:
        raise ValueError("Month must be between 1 (January) and 12 (December).")


# Update days_of_week to Dutch names
days_of_week = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]

# Use name_of_month to create a dictionary for months
months = {i: name_of_month(i) for i in range(1, 13)}

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 31

# Updated print_month to take arguments
def print_month(month, year, start_day):
    days = days_in_month(month, year)  # Get the correct number of days for the month

    # Print the header with the days of the week
    for i in range(len(days_of_week)):
        if i == len(days_of_week) - 1:
            print(days_of_week[i], end="")
        else:
            print(days_of_week[i], end=" ")

    print()  # Newline after printing the days of the week

    current_day = 0

    # Print initial spaces for the first row based on start_day
    for _ in range(start_day):
        print("  ", end=" ")
        current_day += 1

    # Print all the days of the month
    for day in range(1, days + 1):
        print(f"{day:2}", end=" ")
        current_day += 1
        if current_day % 7 == 0:  # Newline at the end of the week
            print()

    # Ensure to print a final newline if the last row didn't end the week
    if current_day % 7 != 0:
        print()

    print("\n")  # Newline after each month

# Set the year
year = 2022  # You can change this to the desired year
start_day = 5  # Initial start_day is 5 (Friday)

# Loop through each month and print its calendar
for month in range(1, 13):  # Loop through months 1 to 12
    print(f"    {months[month]} {year}")  # Print the month title
    print_month(month, year, start_day)

    # Calculate the start day for the next month
    start_day = (start_day + days_in_month(month, year)) % 7
