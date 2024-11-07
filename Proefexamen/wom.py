from Proefexamen.dom import days_of_month
from dow import day_of_the_week

def next_month_start_weeks (year, month):
    #calculates the number of unfull weeks, if month stops on a sunday, the next month starts in a new week
    if days_of_month == 29 and day_of_the_week (year, month, 1) == 7:
        return 6
    if month in (1,3,5,7,8,10,12):
        if day_of_the_week(year, month, 1) > 4:
            return 6
    if month in (4,6,9,11):
        if day_of_the_week(year, month, 1) > 5:
            return 6
    return 5
def month_start_week (year, month):
    x = 1
    if month == 1: return 1
    for i in range(1, month):
        x += next_month_start_weeks(year, i) - 1#to not double count the first week of the month
    return x

assert month_start_week(2018, 1) == 1
assert month_start_week(2016, 5) == 18
assert month_start_week(2020, 12) == 49
assert next_month_start_weeks (2018, 4) == 6
assert next_month_start_weeks (2024, 2) == 5
assert next_month_start_weeks (2024, 12) == 6
assert next_month_start_weeks (2024, 6) == 6
assert next_month_start_weeks(2022,7) == 6
assert next_month_start_weeks(2022, 2) == 5
assert next_month_start_weeks(2020,2) == 5
