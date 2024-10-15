#Exercise Calendar

def leap_year(*, year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_of_month(*, year: int, month: int) -> int:
    #if month == 4 or month == 6 or month == 9 or month == 11:
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap_year(year = year):
            return 29
        else:
            return 28
    else:
        return 31


def dim(*, year: int, month: int) -> int:
    #if leap_year(year = year):
    #    number_of_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #else:
    #    number_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #return [month - 1]
    #return [31, 29 if leap_year(year=year) else 28, 31, 30, 31, 30, 31, 31, 30, 31][month - 1]
    return [31, 28 + leap_year(year=year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]


def day_of_week(*, year: int, month: int, day: int) -> int:
    #1st Jan 1900 = Monday

    total_days = -1
    for _ in range(1900, year):
        if leap_year(year=year):
            total_days += 366
        else:
            total_days += 365

    for i in range(1, month):
        total_days += dim(year=year, month=i)

    total_days += day

    return (total_days % 7) + 1






def dow(*, year: int, month: int):
    #Based on Zeller's Congruence

    #Day of the Month
    q = 1

    #Month
    if month == 1:
        m = 13
    elif month == 2:
        m = 14
    else:
        m = month

    #Year
    if month > 2:
        k = year % 100
    else:
        k = (year % 100) - 1

    #Century
    j = year // 100


print(day_of_week(year=2024, month=1, day=1))





def main():
    assert leap_year(year = 2100) == False, "Test failed on 2100"
    assert leap_year(year = 2024) == True, "Test failed on 2024"
    assert leap_year(year = 2023) == False, "Test failed on 2023"
    assert leap_year(year = 2020) == True, "Test failed on 2020"
    assert leap_year(year = 2000) == True, "Test failed on 2000"
    assert leap_year(year = 1900) == False, "Test failed on 1900"

    assert days_of_month(year = 2024, month = 1) == 31
    assert days_of_month(year = 2024, month = 2) == 29
    assert days_of_month(year = 2024, month = 3) == 31
    assert days_of_month(year = 2024, month = 4) == 30
    assert days_of_month(year = 2024, month = 5) == 31
    assert days_of_month(year = 2024, month = 6) == 30
    assert days_of_month(year = 2024, month = 7) == 31
    assert days_of_month(year = 2024, month = 8) == 31
    assert days_of_month(year = 2024, month = 9) == 30
    assert days_of_month(year = 2024, month = 10) == 31
    assert days_of_month(year = 2024, month = 11) == 30
    assert days_of_month(year = 2024, month = 12) == 31

    assert dim(year=2024, month=1) == 31
    assert dim(year=2024, month=2) == 29
    assert dim(year=2024, month=3) == 31
    assert dim(year=2024, month=4) == 30
    assert dim(year=2024, month=5) == 31
    assert dim(year=2024, month=6) == 30
    assert dim(year=2024, month=7) == 31
    assert dim(year=2024, month=8) == 31
    assert dim(year=2024, month=9) == 30
    assert dim(year=2024, month=10) == 31
    assert dim(year=2024, month=11) == 30
    assert dim(year=2024, month=12) == 31

    #assert day_of_week(year=2024, month=1, day=15) == 2

if __name__ == "__main__":
    main()
