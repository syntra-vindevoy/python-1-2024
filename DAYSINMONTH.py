# leap year
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# DAYS IN MONTH
def days_in_month(month: int, year:int) -> int:
    if month in [4, 6, 9,11]:    #== 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2: #February
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 31

def days_in_month2(month: int, year:int) -> int:
    return [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

# bepalen welke dag van de week een maandag is
def day_of_the_week(year: int, month: int, day: int) -> int:

    total_days = -1 #voor de amerikanen (zondag is voor hun 0)

    for y in range(1900, year):
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365

    for m in range(1, month):
        total_days += days_in_month(m, year)

    total_days += day

    return total_days % 7 + 1 # +1 voor de belgische dagen




# TESTEN
if __name__ == '__main__':
    #assert is_leap_year(2024) == True, "Test failed for year 2024"
    #assert is_leap_year(2000) == True, "Test failed for year 2000"
    #assert is_leap_year(2100) == True, "Test failed for year 2100"
    #assert is_leap_year(2025) == True, "Test failed for year 2025"

    print(day_of_the_week(1900, 1, 1))