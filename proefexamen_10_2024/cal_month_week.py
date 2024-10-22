from week_number import *
from date_string import *
from dow import *
from dom import *


def print_month(year:int, month:int):
    empty = ""
    print(f"{name_of_month(month)} {year}")
    print("")

    for i in range(0,8):
        if i == 0:
            print(empty.center(4, " "), end=" ")
        else:
            if i < 7:
                print(name_of_day(i).center(4, " "), end=" ")
            else:
                print(name_of_day(i).center(4, " "))
                week = week_number(year, month, 1)
                print(f"[{week:>2}]", end=" ")

    start_skips = day_of_the_week(year, month, 1) - 1
    total_days = days_of_month(year, month) + start_skips

    for i in range(1, total_days + 1):
        if i <= start_skips:
            print(empty.center(4, " "), end=" ")
        else:
            if i == total_days:
                print(f"{i - start_skips:^5}")
            elif i % 7 == 0:
                print(f"{i - start_skips:^5}")
                week = week_number(year, month, (i - start_skips) + 1)
                print(f"[{week:>2}]", end=" ")
            else:
                print(f"{i - start_skips:^5}", end="")

if __name__ == "__main__":
    print_month(2022, 2)
