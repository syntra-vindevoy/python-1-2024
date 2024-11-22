import date_string as ds
from dow import day_of_the_week
from week_number import week_number
import dom


# from proefexamen import days_of_month


def print_calendar(year: int, mont: int) -> None:
    first_day_of_week = day_of_the_week(year, mont, 1)
    # print(f"eerste dag van de maand: dag {first_day_of_week} {ds.name_of_day(first_day_of_week)}")
    print(f"\n{ds.name_of_month(mont)} {year}")
    print()
    print("      ", end=" ")
    for i in range(1, 8):
        print(ds.name_of_day(i), end=" ")
    print()

    def print_one_line(
            start: int, end: int, wn
    ):  # needs extra parameter to find weeknumber
        print(f"[{wn}]  ", end=" ")
        for i in range(start, end):
            if i < 1:
                print("  ", end=" ")
            elif i > dom.days_of_month(year, mont):
                print(f"  ", end=" ")
            else:
                print(f"{i:2}", end=" ")
        print()

    weeks_in_month = 6  # different for each month, needs revision
    start = 1 - first_day_of_week + 1
    weeknum = week_number(year, mont, 1)
    for i in range(weeks_in_month):
        print_one_line(
            start, start + 7, weeknum
        )  # needs extra parameter for weeknumber
        start += 7
        weeknum += 1


def main():
    for i in range(1, 13):
        print_calendar(2022, i)


if __name__ == "__main__":
    main()
