from date_string import *
from dow import *
from dom import *


def print_month(year: int, month: int, day: int) -> int:
    name_of_month(month)
    print(name_of_month(month), year)
    print()
    dow = day_of_the_week(year, month, day)
    print(name_of_day(dow), day)


print(print_month(2020, 1, 1))
