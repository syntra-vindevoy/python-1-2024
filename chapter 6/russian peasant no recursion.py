from math import log

def russian_peasant_alt(a,b):
    if a == 0:
        return 0

    check_string (a,b) # deals with false input
    a, b, negative = check_negative(a,b) #checks and deals with negative numbers
    a, b, factor = if_floats(a,b) #turns floats into integers and calculates the factor to convert the result
    n = int(log(a, 2)) #calculates the number of times a is dividable by 2
    result = 0

    for _ in range (n + 1): # repeats n times + 1 time for a itself
        if a % 2 != 0:
            result += b
        a //= 2
        b *= 2
    return result * negative / factor

def check_negative (a,b):
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
    return a,b,negative

def check_string (a,b):
    if isinstance(a, str) or isinstance(b, str):
        raise SyntaxError ("Values can not be strings")

def if_floats (a,b):
    dec = 0
    dec_a = len(str(a)) - len(str(int(a)))
    dec_b = len(str(b)) - len(str(int(b)))
    if dec_a != 0:
        dec += dec_a -1
        a *= 10 ** (dec_a -1)
    if dec_b != 0:
        dec += dec_b -1
        b *= 10 ** (dec_b -1)
    factor = 10 ** dec
    return a, b, factor


assert russian_peasant_alt(1, 8) == 8
assert russian_peasant_alt( 8, 0) == 0
assert russian_peasant_alt( 7, 3) == 21
assert russian_peasant_alt(0, 45) == 0
assert russian_peasant_alt(-8, 5) == -40
assert russian_peasant_alt(9, -10) == -90
assert russian_peasant_alt(-5, -6) == 30
assert russian_peasant_alt(0, -7) == 0
assert russian_peasant_alt(5.5, 10) == 55
assert russian_peasant_alt(-5.5, 10) == -55
assert russian_peasant_alt(1.1, 2) == 2.2
assert russian_peasant_alt(0.001, 900) == 0.9
assert russian_peasant_alt(-8.487, 4.87) == -41.33169
try:
    russian_peasant_alt("a", 5)
except SyntaxError:
    failed = True
assert failed, "Values can not be strings"
failed = False

