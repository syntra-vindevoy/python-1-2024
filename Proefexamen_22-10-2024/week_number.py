from leapyear import is_leap_year
from dom import days_of_month

def week_number(year: int, month: int, day: int):
    total_days = -1

    for y in range(1900, year):
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365

    for m in range(1, month):
        total_days += days_of_month(m, year)

    total_days += day
    return total_days % 7 + 1

def main():
    assert week_number(2022, 1, 1) == 6


if __name__ == "__main__":
    main()


