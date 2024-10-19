from math import log

def russian_peasant_alt(a,b):
    if a == 0:
        return 0

    check_string (a,b) # deals with false input
    a, b, negative = check_negative(a,b) #checks and deals with negative numbers
    a, b, factor = use_floats_recursion(a,b)
    n = int(log(a, 2)) #calculates the number of times a is dividable by 2
    result = 0

    for _ in range (n+1): # repeats n times + 1 time for a itself
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

def use_floats_recursion (a,b,factor=1):
    if (a.is_integer()) and (b.is_integer()): #checks if a float is actually an integer
        return a, b, factor
    if a % 1 != 0:
        a *= 10
        factor *= 10
    if b % 1 != 0:
        b *= 10
        factor *= 10
    return use_floats_recursion(int(a),int(b),factor)

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
#assert russian_peasant_alt(8.45, -2.58) == -21.801
try:
    russian_peasant_alt("a", 5)
except SyntaxError:
    failed = True
assert failed, "Values can not be strings"
failed = False

