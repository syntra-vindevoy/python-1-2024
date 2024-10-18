def is_leapyear(year: int):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dom(year: int , month: int):
    if month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if is_leapyear(year):
            return 29
        else:
            return 28
    return 31

print(dom(2024, 2))

#assert leapyear(2024) == True
#assert leapyear(2025) == False
#assert leapyear(2000) == True
#assert leapyear(1900) == False