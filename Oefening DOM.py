def leapyear(year: int):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dom(y: int , m: int):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if leapyear(year):
            return 29
        else:
            return 28
    return 31

#assert leapyear(2024) == True
#assert leapyear(2025) == False
#assert leapyear(2000) == True
#assert leapyear(1900) == False