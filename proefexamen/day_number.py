from dom import *  # importing our days of month

from leapyear import *


def day_number(year, month, day):

    total_days = 0

    is_leap_year(year)

    for i in range (month - 1):

        total_days += days_of_month [i]

    total_days += day

    return total_days

print(day_number(2020, 3, 1))
# def main():
#     assert day_number(2020, 1, 1) == 1
#     assert day_number(2020, 2, 1) == 32
#     assert day_number(2020, 3, 1) == 61
#     assert day_number(2020, 12, 31) == 366
#
#     assert day_number(2022, 1, 1) == 1
#     assert day_number(2022, 2, 1) == 32
#     assert day_number(2022, 3, 1) == 60
#     assert day_number(2022, 12, 31) == 365
#
#
# if __name__ == "__main__":
#     main()
