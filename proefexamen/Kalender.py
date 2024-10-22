from date_string import *
from dow import *
from dom import *


def kalender(year: int, month: int, day: int) -> int:
    name_of_month(month)
    print(name_of_month(month), year)
    print()
    dow = day_of_the_week(year, month, day)
    print(name_of_day(dow))


print(kalender(2020, 1, 1))
