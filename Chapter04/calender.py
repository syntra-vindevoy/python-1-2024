def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 31
    elif month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    #month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12
    return 30

# dit is de meest performante manier om de dagen in de maand te krijgen.
def days_in_month2(year, month):
    return [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]


def day_of_week(year, month, day):
    total_days = -1

    for y in range(1900, year):
        if is_leap(year):
            total_days += 366
        else:
            total_days += 365

    for m in range(1, month):
        total_days += days_in_month(m, year)

    total_days += day

    return total_days % 7 + 1

def dow (year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    v = (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7

    return v

assert is_leap(2024) == True
assert is_leap(2023) == False
assert is_leap(2000) == True
assert is_leap(2300) == False

print(day_of_week(2024,10,15))
print(dow(2024, 10, 15))