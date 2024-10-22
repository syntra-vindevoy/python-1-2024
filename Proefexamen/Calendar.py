from Proefexamen.dom import days_of_month
from dow import day_of_the_week

def print_calendar(year=int, month=int):
    print (f"{month}  {year}\n\n")
    print (f"Ma Di Wo Do Vr Za Zo")
    dow = day_of_the_week(year = year, month = month, day = 1)

    line_1 = ("  " * dow)
    for i in range(1, 9 - dow):
        line_1 += str(i) + "  "
    print (line_1)

    line_2 = ("")
    for i in range(1+7, 9+7 - dow):
        line_2 += str(i) + "  "
    print (line_2)

print_calendar(2024, 10)




