from dom import days_of_month
from dow import day_of_the_week
from leapyear import is_leap_year
def day_of_year (year):
    month = 1
    dom = days_of_month(year, month)
    if year == is_leap_year(year):
        day = dom(year)
def week_number(year: int, month: int, day: int):
    dom = days_of_month(year, month)
    dow = day_of_the_week(year, month, day)
    week_number = 1

    for i in range (1, day + 1):
        if i + dow % 7 == 0:
            week_number + 1





def main():
    assert week_number(2022, 1, 1) == 1


if __name__ == "__main__":
    main()
