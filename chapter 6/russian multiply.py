def russian_peasant_calc (a:int, b:int, negative, result = 0):
    if a % 2 != 0:
        result += b
    if a < 2:
        result *= negative #turns the value into a negative number if one the starting values was negative
        return result
    a //= 2
    b *= 2
    return russian_peasant_calc(a, b, negative, result)

def russian_peasant (a:int, b:int):
    negative = 1
    if isinstance(a, str) or isinstance(b, str):
        raise SyntaxError ("Values can not be strings")

    if isinstance (a, float) or isinstance(b, float):
        raise ValueError("Values can not be floats")

    if a < 0 and b < 0:
        a *= -1 #makes a a positive number
        b *= -1 #makes b a positive number
    if (a < 0) ^ (b < 0): #only if one of the value is negative
        if a < 0:
            a *= -1
        else:
            b *= -1
        negative = -1
    return russian_peasant_calc(a, b, negative = negative)

assert russian_peasant(5, 2) == 10
assert russian_peasant(7,3) == 21
assert russian_peasant(45, 89) == 4005
assert russian_peasant(-3, 5) == -15
assert russian_peasant(11, -8) == -88
assert russian_peasant(-7, -10) == 70
try:
    russian_peasant("a", 5)
except SyntaxError:
    failed = True
assert failed, "Values can not be strings"
failed = False
try:
    russian_peasant(a= 8.5, b= -7.3)
except ValueError:
    failed = True
assert failed, "Values can not be floats"
failed = False
