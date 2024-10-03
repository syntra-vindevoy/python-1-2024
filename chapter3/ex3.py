import string

def main_start():
    print(f"2020 {leap_year(2020)}")
    print(f"1900 {leap_year(1900)}")
    print(f"400 {leap_year(400)}")


# To determine whether a year is a leap year, you can follow these rules:
#
# A year is a leap year if it is divisible by 4.
# However, if the year is divisible by 100, it is NOT a leap year, unless...
# The year is also divisible by 400, in which case it IS a leap year.
# Steps for Calculation:
# If the year is divisible by 4 and not divisible by 100, it's a leap year.
# If the year is divisible by 100, check if it’s divisible by 400. If so, it’s a leap year.
def leap_year(year:int)->bool:
    """

    Args:
        year (object):

    Returns: bool
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def is_valid_iban(iban):
    """
    Validate a IBAN string

    Args:
        iban (str): IBAN string

        Returns:
            bool: True if valid, False otherwise
    """

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


def fac1(n:int)->int:
    """

    Args:
        n (object):
    """
    total = 1
    for i in range(2, n+1):
        total = total * i
    return total

def fact(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    return n * fact(n-1)


def draw_grid(row_count, col_count,inner_width):
    horizontal_line = (("+" + ("-" * inner_width)) * col_count) + "+"
    vertical_line = (("|" + (" " * inner_width))* col_count) + "|"
    for _ in range(row_count):
        print(horizontal_line)
        for _ in range(col_count):
            print(vertical_line)
    print(horizontal_line)



if __name__ == '__main__':
    main_start()
    assert is_valid_iban("NL91ABNA0417164300") == True
    assert fac1(3) == 6
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(3) == 6
    assert fact(2) == 2
    assert fact(4) == 24
    assert fact(5) == 120
    draw_grid(2, 5,4)

