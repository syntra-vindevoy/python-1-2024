def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#print(is_leap_year(2000))

def dom(year: int, month: int)-> int:
    """Return the number of days in a given month and year."""
    return [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
    # ANDERE MANIEREN
    # if month == 4 or month == 6 or month == 9 or month ==
    # if month in [4, 6, 9, 11]:
    #     return 30
    # elif month == 2:
    #     if is_leap_year(year):
    #         return 29
    #     else:
    #         return 28
    # return 31

def day_of_the_week(year: int, month: int, day: int) -> int:

    total_days = -1
    for y in range(1900, year):
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365
    for m in range(1, month):
        total_days += dom(year, m)

    total_days += day

    return total_days % 7 + 1

## poetie

# def dow(year: int, month: int, day: int) -> int:
#     t=[0,3,2,5,0,3,5,1,4,6,2,4][month-1]
#



def main():

    assert is_leap_year(2024)==True
    assert is_leap_year(2000)==True
    assert is_leap_year(2402)==False
    assert is_leap_year(2211)==False
    assert is_leap_year(36001)==False


if __name__ == "__main__":
    main()
print(day_of_the_week(2024, 10, 15))

x=6
y=3

print(x == 6 and y != 3)
