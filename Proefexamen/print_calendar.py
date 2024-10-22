### gestolen Chiel

from Proefexamen.dom import days_of_month
from day_number import day_number
from date_string import name_of_month

def month_calender(year: int, month: int):

    start_day = first_day(year, month)
    num_days = days_of_month(year, month)

    print(f"{name_of_month(month)}: {year}\n\nMa Di Wo Do Vr Za Zo")
    print("   " * start_day, end="")

    for day in range(1, num_days + 1):
        print(f"{day:2}", end=" ")
        if (start_day + day) % 7 == 0:
            print()

    print("\n")


def year_calender(year):
    for _ in range(1, 13):
        print(month_calender(year, _))


def first_day(year, month):
    f_day = day_number(year, month, 1) % 7

    return f_day