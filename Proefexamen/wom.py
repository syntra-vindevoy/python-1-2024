from Proefexamen.dom import days_of_month
from dow import day_of_the_week

def next_month_start_weeks (year, month):
    #calculates the number of weeks till next month, if month stops on a sunday, the next month starts in a new week
    if days_of_month == 29 and day_of_the_week (year, month, 1) == 7: #only exception for february
        return 6
    if month in (1,3,5,7,8,10,12) and day_of_the_week(year, month, 1) > 4:
        return 6
    if month in (4,6,9,11) and day_of_the_week(year, month, 1) > 5:
        return 6
    return 5

def month_start_week (year, month):
    if day_of_the_week (year, 1, 1) <= 4:
        #The first week of january has to be at least 4 days long, else it is the last week of the previous year
        total_weeks = 1
    else: total_weeks = 0

    for i in range(1, month):
        total_weeks += next_month_start_weeks(year, i) - 1#to not double count the first week of the month
    return total_weeks

if __name__ == '__main__':
    assert month_start_week(2018, 1) == 1
    assert month_start_week(2016, 5) == 17
    assert month_start_week(2020, 12) == 49
    assert next_month_start_weeks (2018, 4) == 6
    assert next_month_start_weeks (2024, 2) == 5
    assert next_month_start_weeks (2024, 12) == 6
    assert next_month_start_weeks (2024, 6) == 6
    assert next_month_start_weeks(2022,7) == 6
    assert next_month_start_weeks(2022, 2) == 5
    assert next_month_start_weeks(2020,2) == 5
