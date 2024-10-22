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
    for i in range(9 - dow, 9-dow+7):
        line_2 += str(i) + "  "
    print (line_2)

    line_3 = ("")
    for i in range(9-dow + 7 , 9-dow + 14):
        line_3 += str(i) + "  "
    print (line_3)

    line_4 = ("")
    for i in range(9-dow + 14 , 9-dow + 21):
        line_4 += str(i) + "  "
    print (line_4)

    line_5 = ("")
    for i in range(9-dow + 21, days_of_month(year = year, month = month)+1):
        line_5 += str(i) + "  "
    print (line_5)






print_calendar(2024, 12)
