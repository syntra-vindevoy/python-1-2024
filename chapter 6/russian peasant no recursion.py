from math import log

def russian_peasant_alt(a,b):
    if a == 0 or b == 0: return 0 #b == 0 is not necessary for the result but avoids unnecessary calculations
    if a == 1: return b
    if b == 1: return a

    check_string (a,b) # deals with input of strings

    if (a < 0) ^ (b < 0): #checks and deals with negative numbers
        negative = -1
    else: negative = 1

    a, b = abs(a), abs(b)
    a, b, factor = if_floats(a,b) #turns floats into integers and calculates the factor to convert the result
    n = int(log(a, 2)) #calculates the number of times a is dividable by 2
    result = 0

    for _ in range (n + 1): # repeats n times + 1 time for a itself
        if a % 2 != 0:
            result += b
        a //= 2
        b *= 2
    return result * negative / factor

def check_string (a,b):
    if isinstance(a, str) or isinstance(b, str):
        raise SyntaxError ("Values can not be strings")

def if_floats (a,b):
    """this function turns floats into integers and calculates the factor
        to convert the multiplication into a float again.
        Used in the russian peasant method """
    decimals = 0
    decimals_a = len(str(a)) - len(str(int(a))) #calculates the number of decimals
    decimals_b = len(str(b)) - len(str(int(b)))
    if decimals_a != 0:
        decimals += decimals_a -1
        a *= 10 ** (decimals_a -1)
    if decimals_b != 0:
        decimals += decimals_b -1
        b *= 10 ** (decimals_b -1)
    factor = 10 ** decimals
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
assert russian_peasant_alt(-8.4, 1) == -8.4
try:
    russian_peasant_alt("a", 5)
except SyntaxError:
    failed = True
assert failed, "Values can not be strings"
failed = False

def ask_input():
    a = input("\nLet's try the Russian Peasant multiplication method. \n\n" "Enter is the first number: ")
    b = input("Enter is the second number: ")
    try:
        a = float (a)
        b = float (b)
    except ValueError:
        print ("\nPlease enter only whole or decimal numbers!")
        return ask_input()
    print (f"The result of the multiplication is: {russian_peasant_alt(float(a),float(b))}")
ask_input()

