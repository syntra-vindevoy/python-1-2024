import string


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


def is_valid_iban(iban):
    # Verwijder spaties en zet alles om naar hoofdletters
    iban = iban.replace(' ', '').upper()

    # Controleer lengte van Nederlandse IBAN (18 tekens)
    if len(iban) != 18:
        return False

    # Controleer of de IBAN begint met "NL" en de eerste vier tekens correct zijn
    if not iban[:2].isalpha() or not iban[2:4].isdigit():
        return False

    # Verplaats de eerste vier tekens naar het einde
    rearranged_iban = iban[4:] + iban[:4]

    # Vervang letters door cijfers (A = 10, B = 11, ..., Z = 35)
    iban_numeric = ''.join(str(int(char, 36)) if char in string.ascii_uppercase else char for char in rearranged_iban)

    # Controleer of het IBAN mod 97 gelijk is aan 1
    return int(iban_numeric) % 97 == 1


def factorial(n):
    total = 0
    for i in range(1,n+1):
        total = total*i
    return total

if __name__ == '__main__':
    main()