from Proefexamen.dom import days_of_month
from dow import day_of_the_week
from date_string import name_of_month

def print_calendar(year=int, month=int):
    print (f"{name_of_month(month)}  {year}\n\n")
    print (f"Ma Di Wo Do Vr Za Zo")
    dow = day_of_the_week(year = year, month = month, day = 1)
    dom = days_of_month(year = year, month = month)

    line = (dow - 1) * "   "
    for i in range (1, dom + 1):
        line += str(f"{i:2} ")  #aan chat gpt gevraagd hoe ik de dagen kon uitlijnen
        if (i-1 + dow) % 7 == 0:
            line += "\n"
    print (line)

print_calendar(2024, 7)
