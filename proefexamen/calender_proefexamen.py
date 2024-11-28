
from proefexamen.date_string import name_of_month
from proefexamen.dom import days_of_month
from proefexamen.dow import day_of_the_week


def prt_calender(year, month, day):
    d = 0
    start_position = day_of_the_week(year, month, day-1)
    print(name_of_month(month), year)
    print("")
    print(f"Ma Di Wo Do Vr Za Zo")
    print("   " * start_position, end="")
    for i in range(1, days_of_month(year, month) + 1):
        #print(i, end=" ")
        print(f"{i:2}", end=" ")  # Deze code werd gebruikt om de dagen lengte 2 mee te geven: {i:2}
        #print(f" {i}" if len(i) < 2 else f"{i}")
        if (day_of_the_week(year, month, day + d) % 7 == 0):
            print()
        d += 1
    print()

def print_year(year:int):
    for i in range(1, 13):
        prt_calender(year, i, days_of_month(year, i))
        print("")

prt_calender(2022, 12, 31)

#print_year(2022)