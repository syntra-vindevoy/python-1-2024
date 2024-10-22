from date_string import name_of_month
from dom import days_of_month
from dow import day_of_the_week
from week_number import week_number


def print_calendar_month(year: int, month: int):
    print(f"{name_of_month(month)} {year}")
    print()
    print("     Ma   Di  Wo  Do  Vr Za  Zo")

    first_day = day_of_the_week(year, month, 1)
    total_days = days_of_month(year, month)
    day = 1
    week_num = week_number(year, month, day)

    print(f"[{week_num:2}] ", end="")
    for _ in range(1, first_day):
        print("    ", end="")

    while day <= total_days:
        print(f"{day:2}", end="  ")
        if day_of_the_week(year, month, day) == 7:
            day += 1
            if day <= total_days:
                week_num = week_number(year, month, day)
                print()
                print(f"[{week_num:2}] ", end="")
            else:
                print()
        else:
            day += 1
    print()


def print_calendar_year(year: int):
    for month in range(1, 13):
        print_calendar_month(year, month)
        print()


def main():
    print_calendar_year(2022)


if __name__ == "__main__":
    main()