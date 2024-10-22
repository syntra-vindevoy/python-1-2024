from leapyear import *
from dom import *
from dow import *
from date_string import *
from day_number import *
from week_number import *

def number_of_lines(year:int, month:int) -> int:
    pass


def print_month(year:int, month:int):
    print(f"{name_of_month(month)} {year}")
    print("")
    for i in range(1,8):
        print(name_of_day(i), end=" ")
    print("")

    start_skips = day_of_the_week(year, month, 1) - 1
    total_days = days_of_month(year, month) + start_skips

    for i in range(1, total_days + 1):
        if i <= start_skips:
            print("   ", end="")
        else:
            if i % 7 == 0:
                print(f"{i - start_skips:^3}")
            else:

                print(f"{i - start_skips:^3}", end="")

print_month(2024, 10)
