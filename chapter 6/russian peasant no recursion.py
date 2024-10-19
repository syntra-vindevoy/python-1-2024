from math import log
def russian_peasant_alt(a,b):
    if a == 0:
        return 0
    negative = 1
    if (a < 0) and (b < 0):
        a *= -1
        b *= -1
    if (a < 0) ^ (b < 0):
        if a < 0:
            a *= -1
        else:
            b *= -1
        negative = -1
    n = int(log(a, 2)) #berekend het aantal keer dat a deelbaar is door 2
    result = 0
    for _ in range (n+1): # n gaf het hoogst aantal keren van a deelbaar door 2, a zelf moest er nog bij
        if a % 2 != 0:
            result += b
        a //= 2
        b *= 2
    return result * negative

assert russian_peasant_alt(1, 8) == 8
assert russian_peasant_alt( 8, 0) == 0
assert russian_peasant_alt( 7, 3) == 21
assert russian_peasant_alt(0, 45) == 0
assert russian_peasant_alt(-8, 5) == -40
assert russian_peasant_alt(9, -10) == -90
assert russian_peasant_alt(-5, -6) == 30
