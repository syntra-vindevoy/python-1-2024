def leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # if year % 4 == 0:
    #    if year % 100 == 0:
    #         if year % 400 == 0:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return True
    # else:
    #     return False

def days_in_month(year: int, month: int) -> int:

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28

    return 31

def days_in_month2(year: int, month: int) -> int: #shorter using months with 30, fewer months

    if month in [4, 6, 9, 11]:
        return 30

    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28

    return 31

def days_in_month3(year: int, month: int) -> int: #shorter with using a list

    count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_year(year) and month == 2:
        return 29

    return count[month - 1]

def days_in_month4(year: int, month: int) -> int: #shorter removing if and coming it with return (if else in list)

    return [31, 29 if leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def days_in_month5(year: int, month: int) -> int: #removing if else from list, using the value 1 of a boolean

    # int + bool = int + 1 (true) of + 0 (False)
    return [31, 28 + leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

def day_of_the_week(year: int, month: int, day: int) -> int:

    total_days = -1

    for y in range(1900, year):
        if leap_year(y):
            total_days += 366
        else:
            total_days += 365

    for m in range(1, month):
        total_days += days_in_month5(year, m)

    total_days += day

    return total_days % 7 + 1


def main():

    print(day_of_the_week(2024, 10, 15))

    assert leap_year(1900) == False
    assert leap_year(2024) == True
    assert leap_year(2000) == True
    assert leap_year(1999) == False

    assert days_in_month(2024, 4) == 30
    assert days_in_month(2024, 10) == 31
    assert days_in_month(2000, 2) == 29
    assert days_in_month(1900, 2) == 28

if __name__ == '__main__':
    main()