import math

"""
Exercise 1  
"""
def my_sqrt(a: float):
    x=3
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y
print("a  mysqrt(a) math.sqrt(a)  diff")
for i in range(1,10):
    mx:float=my_sqrt(i)
    m:float=math.sqrt(i)
    print (f"{i} {mx:.8f}    {m:.8f}     {mx - m:.8f}")

"""
Exercise 3 
The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical
 approximation of 1 / π:
"""


def factorial (n):
    if n == 0:
        return 1
    else:
        result = n * factorial (n - 1)
        return result


def estimate_pi ():
    total = 0
    k = 0
    factor = 2 * math.sqrt (2) / 9801
    while True:
        num = factorial (4 * k) * (1103 + (26390 * k))
        divider = factorial (k) ** 4 * 396 ** (4 * k)
        total += num / divider
        term = factor * num / divider
        if abs (term) < 1e-15:
            break
        k += 1

    return 1 / (factor * total)


print (estimate_pi ())
