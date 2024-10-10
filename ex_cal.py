#Exercise Calendar

def leap_year(*, year: int):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def days_month(*, month: int, year: int):
    if (month < 8):                                 #Months Jan - July
        if (month % 2 == 0) and (month != 2):       #Even months, excl febr
            return 30
        elif (month % 2 == 0) and (month == 2):     #Febr
            if leap_year(year = year) == True:             #Febr = 29
                return 29
            else:                                   #Febr = 28
                return 28
        else:                                       #Uneven
            return 31
    elif (month > 7) and (month < 13):              #Months Aug - Dec
        if (month % 2 == 0) :                       #Even
            return 31
        else:                                       #Uneven
            return 30
    else:                                           #Invalid month
        return 0

