def is_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return the number of days in a given month and year."""
    return [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]


def calculate_day_of_week(year, month, day):
    """Determine the day of the week for a given date. Returns 0 (Monday) to 6 (Sunday)."""
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    h = (day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    return (h + 5) % 7


def calculate_week_number(year, month, day):
    """Return the ISO 8601 week number for a given date."""
    # Calculate the day of the year
    days_before_month = sum(days_in_month(year, m) for m in range(1, month))
    day_of_year = days_before_month + day

    # Calculate the weekday of January 4 (ISO week 1 always contains January 4)
    jan4 = calculate_day_of_week(year, 1, 4)

    # Calculate week number
    corrector = 3 - (jan4 - 1)
    week_number = (day_of_year + corrector) // 7 + 1

    # Handle cases where the week number is 0 or 53
    if week_number == 0:
        week_number = calculate_week_number(year - 1, 12, 31)
    elif week_number == 53 and calculate_week_number(year + 1, 1, 1) == 1:
        week_number = 1

    return week_number


def generate_calendar(year):
    """Generate a calendar for the given year with week numbers."""
    months = [
        ("January", 31),
        ("February", 29 if is_leap_year(year) else 28),
        ("March", 31),
        ("April", 30),
        ("May", 31),
        ("June", 30),
        ("July", 31),
        ("August", 31),
        ("September", 30),
        ("October", 31),
        ("November", 30),
        ("December", 31),
    ]

    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    def first_day_of_year(year):
        """Determine the first day of the year."""
        return calculate_day_of_week(year, 1, 1)

    start_day = first_day_of_year(year)

    print(f"Calendar Year: {year}\n")
    for month_index, (month, days_count) in enumerate(months):
        print(f"{month} {year}".center(27, ' '))
        print(f"{'Wk':>2} {' '.join(days)}")

        week_number = calculate_week_number(year, month_index + 1, 1)

        # Align first line
        print(f"{week_number:2} {'   ' * start_day}", end=" ")

        for day in range(1, days_count + 1):
            print(f"{day:2}", end=" ")
            start_day = (start_day + 1) % 7
            if start_day == 0:  # New week
                print()
                if day != days_count:  # Prevent incrementing week number for the start of next month
                    week_number = calculate_week_number(year, month_index + 1, day + 1)
                print(f"{week_number:2} ", end="")
        print("\n")


generate_calendar(2024)
