def is_leap_year_short(year: int) -> bool:
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0


def is_leap_year(year: int) -> bool:
    # A year is a leap year
    # if it is divisible by 4,
    # except for years that are divisible by 100 but not by 400
    if year % 400 == 0: return True
    if year % 100 == 0: return False
    if year % 4 == 0: return True
    return False


def dom_with_dict(year: int, month: int) -> int:
    # Return the number of days in a month
    day_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31,
    }
    if is_leap_year(year) and month == 2: return 29
    return day_in_month[month]


def dom_with_list(year: int, month: int) -> int:
    # Return the number of days in a month
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year) and month == 2: return 29
    return day_in_month[month - 1]


def dom_with_list_and_ternary(year: int, month: int) -> int:
    # Return the number of days in a month
    # day_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # OF
    day_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day_in_month[month - 1]


def dom_ternary(year: int, month: int) -> int:
    # Return the number of days in a month
    # .... ternary is meant to be written on one line, not a good solution
    return \
        31 if month in {1, 3, 5, 7, 8, 10, 12} else \
            30 if month in {4, 6, 9, 11} else \
                29 if month == 2 and is_leap_year(year) else \
                    28


def day_of_week(year: int, month: int, day: int) -> str:
    total_days = -1  # 1 Jan 1900 is a Monday (-1 or 0 depending on monday or sunday)
    for y in range(1900, year):
        total_days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        total_days += dom_with_list(year, m)
    total_days += day
    return total_days % 7 + 1


def some_function(*, name: str, age: int):
    print(name, age, sep=" - ", end="...")


some_function(
    name="John",
    age=25
)


def main():
    assert is_leap_year_short(2000) == True
    assert is_leap_year_short(1900) == False
    assert is_leap_year_short(2024) == True
    assert is_leap_year_short(2020) == True

    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2024) == True
    assert is_leap_year(2020) == True

    assert dom_with_dict(2020, 1) == 31
    assert dom_with_dict(2020, 2) == 29
    assert dom_with_dict(2021, 2) == 28

    assert dom_with_list(2020, 1) == 31
    assert dom_with_list(2020, 2) == 29
    assert dom_with_list(2021, 2) == 28

    assert dom_with_list_and_ternary(2020, 1) == 31
    assert dom_with_list_and_ternary(2020, 2) == 29
    assert dom_with_list_and_ternary(2021, 2) == 28

    assert dom_ternary(2020, 1) == 31
    assert dom_ternary(2020, 2) == 29
    assert dom_ternary(2021, 2) == 28

    assert day_of_week(2024, 10, 15) == 2
    assert day_of_week(2025, 10, 15) == 3
    assert day_of_week(2024, 10, 16) == 3
