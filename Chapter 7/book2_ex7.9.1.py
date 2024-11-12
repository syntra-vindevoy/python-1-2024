# Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that takes a as a parameter
# chooses a reasonable value of x, and returns an estimate of the square root of a.
import math


#>>> a = 4
#>>> x = 3
#>>> y = (x + a/x) / 2
#>>> y
#2.16666666667
#>>> x = y

def mysqrt(a: int) -> float:
    x = 3
    y = (x + (a/x) / 2)
    x = y
    return y

def line_1():
    print(f"a   mysqrt(a)     math.sqrt(a)  diff")

def line_2():
    print(f"-   ---------     ------------  ----")

def rest_of_lines(a: int) -> float:
    for a in range(1, a):
        while a < 10:
            print(int(a:.2f))

line_1()
line_2()
rest_of_lines(9)