# # print_calendar.py
# from Proefexamen.dom import days_of_month
# from day_number import day_number
# from Proefexamen.date_string import name_of_month, name_of_day
#
#
# def month_calender(year: int, month: int) -> str:
#     """Returns the string representation of a given year and month."""
#     return f"{name_of_month(month)} {year}"
#
#
# def year_calender(year: int):
#     """Prints the calendar for each month in a given year."""
#     for month in range(1, 13):
#         print(month_calender(year, month))
#         starting_day = day_number(year, month, 1)
#         print("   " * starting_day, end="")
#
#         days_in_month = days_of_month(year, month)
#         month_string = ""
#
#         for day in range(1, days_in_month + 1):
#             day_num = day_number(year, month, day)  # Ensure the day number is between 1 and 7
#             month_string += f" {day:2}"
#
#             if (day_num + 1) % 7 == 0:  # Sunday -> Start a new line
#                 month_string += "\n"
#
#         print(month_string.strip())
#         print("\n" + "-" * 20 + "\n")  # Adding separation between months
#
#
# year_calender(2024)
#
# print_calendar.py
from Proefexamen.dow import day_of_the_week
from Proefexamen.dom import days_of_month
from Proefexamen.day_number import day_number
from Proefexamen.date_string import name_of_month, name_of_day


def month_calender(year: int, month: int) -> str:
    """Returns the string representation of a given year and month."""
    return f"{name_of_month(month)} {year}"


def year_calender(year: int):
    """Prints the calendar for each month in a given year."""
    for month in range(1, 13):
        starting_day = day_of_the_week(year, month, 1)

        days_in_month = days_of_month(year, month)
        print(month_calender(year, month))
        # Assuming day_number() is a function that returns the starting day of the month
        print(f"{' ':2 * starting_day, end='')

        month_string = ""

        for day in range(1, days_in_month + 1):
            day_num = day_number(year, month, day)  # Ensure the day number is between 1 and 7
            month_string += f"{day:2} "

            if (day_num + day) % 7 == 0:  # Sunday -> Start a new line
                month_string += "\n"

        print(month_string.strip())
        print("\n" + "-" * 20 + "\n")  # Adding separation between months


year_calender(2024)
