def is_leap_year (year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_mon (month: int, year: int) -> int:
    if month in [4, 6, 9, 11]:  # == 4 or month == 6 or month == 9 or month == 11:  # January
        return 30
    elif month == 2:  # February
        if is_leap_year (year):
            return 29
        else:
            return 28

    # elif :  # April
    return 31


def days_in_month2 (month: int, year: int) -> int:
    return [31, 28 + is_leap_year (year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]


def day_of_the_week (year: int, month: int, day: int) -> int:
    # 1900/01/01 was a Monday

    total_days = -1

    for y in range (1900, year):
        if is_leap_year (y):
            total_days += 366
        else:
            total_days += 365

    for m in range (1, month):
        total_days += days_in_mon (m, year)

    total_days += day

    return total_days % 7 + 1


def dow (year: int, month: int, day: int) -> int:
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    v = (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7

    return v


if __name__ == "__main__":
    # assert is_leap_year(2024) == True, "Test failed for year 2024"
    # assert is_leap_year(2000) == True, "Test failed for year 2000"
    # assert is_leap_year(2100) == False, "Test failed for year 2100"
    # assert is_leap_year(2025) == False, "Test failed for year 2025"

    # print(days_in_month(2, 2024))

    print (day_of_the_week (1900, 1, 1))
    print (day_of_the_week (1900, 1, 7))
    print (dow (2024, 10, 15))