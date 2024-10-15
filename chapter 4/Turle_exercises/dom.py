def leap (year):
    if (year % 4 == 0 and  year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def dom (year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        if leap(year):
            return 29
        return 28

#print (dom(2200, 2))

def leap_alt (year):
        return (year % 4 == 0 and  year % 100 != 0) or (year % 400 == 0)

def dom_alt (year, month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        if leap(year):
            return 29
        return 28
    return 31
#print (dom_alt(2200, 3))

def dom_alt2 (year, month):
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        if leap(year):
            return 29
        else:
            return 28
    else:
        return 31

#print (dom_alt2 (1983,3))

def dom_alt3 (year, month):
    count = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if leap (year) and month == 2:
        return 29
    return count[month - 1]
#print (dom_alt3 (2000,10))

def dom_alt4 (year, month):
    return [31, 29 if leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31][month - 1] #begint steeds met 0 te tellen
print (dom_alt4(2024,3))


def day_of_week (year: int, month:int, day:int) ->int:
    total_days = -2
    for y in range (1900, year):
        if leap(year):
            total_days += 366
        else:
            total_days += 365

    for d in range (1, month):
        total_days += dom_alt4(d, month)
    total_days += day
    return total_days %7 + 1

print (day_of_week(2024, 10, 15))


if __name__ == "__main__":
    assert leap(2000) == True
    assert leap(2400) == True
    assert leap(2004) == True
    assert leap(1995) == False