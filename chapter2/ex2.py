def main ():
   print(f"2020 {leap_year(2020)}")
   print (f"1900 {leap_year (1900)}")
   print (f"400 {leap_year (400)}")
# To determine whether a year is a leap year, you can follow these rules:
#
# A year is a leap year if it is divisible by 4.
# However, if the year is divisible by 100, it is NOT a leap year, unless...
# The year is also divisible by 400, in which case it IS a leap year.
# Steps for Calculation:
# If the year is divisible by 4 and not divisible by 100, it's a leap year.
# If the year is divisible by 100, check if it’s divisible by 400. If so, it’s a leap year.
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    main()