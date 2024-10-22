from dow import day_of_the_week
from day_number import day_number

def week_number(year: int, month: int, day: int):
    dow = day_of_the_week(year, 1, 1)
    days = day_number(year, month, day)
    week = (dow - 2 + days) // 7
    if week < 1:
        week = 52

    return week

def main():
    assert week_number(2022, 1, 1) == 52  # 1 januari 2022 valt in week 52 van 2021
    assert week_number(2022, 1, 3) == 1   # 3 januari 2022 is de eerste week van 2022
    assert week_number(2022, 1, 10) == 2  # 10 januari 2022 is de tweede week van 2022
    assert week_number(2022, 2, 1) == 5   # 1 februari 2022 valt in week 5
    assert week_number(2022, 2, 28) == 9  # 28 februari 2022 is week 9
    assert week_number(2022, 12, 31) == 52 # 31 december 2022 is week 52

if __name__ == "__main__":
    main()
