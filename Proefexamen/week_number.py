from dow import day_of_the_week
from day_number import day_number

def week_number(year: int, month: int, day: int):
    return (day_of_the_week(year, month, day) - 2 + day_number(year, month, day)) // 7




def main():
    assert week_number(2022, 1, 1) == 1
    assert week_number(2022, 2, 22) == 8
    assert week_number(2022, 3, 10) == 10
    assert week_number(2022, 4, 5) == 14
    assert week_number(2022, 5, 20) == 20
    assert week_number(2022, 6, 1) == 23
    assert week_number(2022, 7, 25) == 30
    assert week_number(2022, 8, 12) == 32
    assert week_number(2022, 9, 18) == 37
    assert week_number(2022, 10, 3) == 40
    assert week_number(2022, 11, 28) == 48
    assert week_number(2022, 12, 9) == 49



if __name__ == "__main__":
    main()
