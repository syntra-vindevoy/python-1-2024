#Exercise 9 - Write a func to calc the faculty of a number without recursive
#Also optimizing is investigated, each iteration of the fac'x' is more memory efficient

def fac1(*, x: int):
    if x == 0:
        return 1

    if x == 1:
        return 1

    result = 1
    if x > 0:
        for i in range(x, 1, -1):
            result = result * i

        return result
    else:
        return 0

def fac2(*, x: int):
    if x == 0:
        return 1

    if x == 1:
        return 1

    result = 1
    if x > 0:
        for i in range(2, x + 1):
            result = result * i

        return result
    else:
        return 0

def fac3(*, x: int):
    if x == 0:
        return 1

    if x == 1:
        return 1

    result = x          #one FOR iteration less, because the last iteration is multiply with itself, but here we start with our self
    if x > 0:
        for i in range(2, x):
            result = result * i

        return result
    else:
        return 0

def fac4(*, x: int):
    if x == 0 or x == 1:
        return 1

    result = x          #one FOR iteration less, because the last iteration is multiply with itself, but here we start with our self
    if x > 0:
        for i in range(2, x):
            result = result * i

        return result
    else:
        return 0

def fac5(*, x: int):
    if x < 2:
        return 1

    result = x          #one FOR iteration less, because the last iteration is multiply with itself, but here we start with our self
    if x > 0:
        for i in range(2, x):
            result *= i

        return result
    else:
        return 0








print(fac2(x = 5))
