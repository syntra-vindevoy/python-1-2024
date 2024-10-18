def is_leapyear(year: int):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dom(year: int , month: int):
    #hier wordt een lijst gebruikt. Nummer input gaat in positie resultaat uit de lijst halen
    return [31, 28 + is_leapyear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month -1]

def day_of_the_week(year: int, month: int, day= int) -> int:
    #1900/01/01 was a monday
    total_days = -1

    for y in range(1900, year):
        if is_leap_year(y):
            total_days += 366
        else:
            total_days += 365
    for m in range(1, month):
        total_days += day_in_month(m, year)

    total_days += day

    return total_days % 7

#assert leapyear(2024) == True
#assert leapyear(2025) == False
#assert leapyear(2000) == True
#assert leapyear(1900) == False

if __name__=='__main__':
    print(day_of_the_week(1900, 1, 1))