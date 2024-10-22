def leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_of_month(year: int, month: int) -> int:
    odd_months = {1, 3, 5, 7, 8, 10, 12}

    if month in odd_months:
        return 31
    elif month == 2 and leap_year(year):
        return 29
    elif month == 2:
        return 28
    else:
        return 30


def days_since_1900(year: int, month: int) -> int:
    total_days = 0

    for y in range(1900, year):
        if leap_year(y):
            total_days += 366
        else:
            total_days += 365

    for m in range(1, month):
        total_days += days_of_month(year, m)

    return total_days


def day_of_week(year: int, month: int) -> int:
    total_days = days_since_1900(year, month)

    return (total_days + 0) % 7


def month_name(month: int) -> str:
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_names.get(month, "Invalid month")


def print_calendar(month: int, year: int):
    days_in_month = days_of_month(year, month)
    start_day = day_of_week(year, month)
    month_str = month_name(month)

    print(f"{month_str} {year:^20}")
    print("-" * 28)

    print("Mo Tu We Th Fr Sa Su")

    for _ in range(start_day):
        print("   ", end="")

    for day in range(1, days_in_month + 1):
        print(f"{day:2}", end=" ")
        if (start_day + day) % 7 == 0:
            print()

    print("\n" + "-" * 28)


def main():
    year = 1989
    month = 5
    print_calendar(month, year)


if __name__ == "__main__":
    main()