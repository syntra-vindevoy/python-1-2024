from Proefexamen.dom import days_of_month
from dow import day_of_the_week
from wom import month_start_week
from date_string import name_of_month

def print_calendar(year=int, month=int):
    print (f"     {name_of_month(month)}  {year}\n")
    print (f"     Ma Di Wo Do Vr Za Zo")
    dow = day_of_the_week(year = year, month = month, day = 1)
    dom = days_of_month(year = year, month = month)

    week = month_start_week(year = year, month = month)
    if week == 0:
        line = f"[{52}]".ljust(5) + (dow - 1) * "   "
    else:
        line = f"[{week}]".ljust(5) + (dow - 1) * "   "

    for i in range (1, dom + 1):
        line += f"{i:2} "
        if ((i-1 + dow) % 7 == 0) and i != dom: #anders komt dit niet mooi uit bij jaarkalender
            week += 1
            if week == 53 and day_of_the_week(year,12,31) <= 3 : week = 1
            #the last week of the year has to contain december 28, else it is the first week of the next year
            line += "\n" + f"[{week}] ".ljust(5)

    print (line)


def print_year_calendar(year):
    for i in range (1,13):
        print_calendar(year,i)
        print ("")

print_year_calendar(2005)
