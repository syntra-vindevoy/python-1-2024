from operator import truediv
from pickle import FALSE

first_name = "Thomas"
last_name = "Meersschaut"

def is_leap_year(year):
    ###
    #20240924 - TM
    #This function verifies if a year is a leap year
    ###

    if year % 4 == 0:
        return True
