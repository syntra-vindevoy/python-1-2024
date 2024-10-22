from sys import exec_prefix


def fac(n: int) ->int:
    if type(n) != int:
        raise TypeError('n must be an integer')

    if n < 0:
        raise ValueError('n must be a positive integer')

    return 1 if n < 2 else n * fac(n-1)


def fac2(n: int | float) -> int:
    if type(n) != int:
        if type(n) != float:
            raise TypeError('n must be an integer or float')

        if int(n) != n:
            raise TypeError('only float numbers that are whole numbers')

    if n < 0:
        raise ValueError('n must be a positive integer')

    return 1 if n < 2 else n * fac(n - 1)

assert fac(0) == 1
assert fac(1) == 1
assert fac(2) == 2
assert fac(3) == 6
assert fac(4) == 24
assert fac(5) == 120

assert fac2(0) == 1
assert fac2(1) == 1
assert fac2(2) == 2
assert fac2(3) == 6
assert fac2(4) == 24
assert fac2(5) == 120
assert fac2(2.0) == 2

failed = False
try:
    _ = fac(-1)
except ValueError:
    failed = True

assert failed, "negative factorial should raise a valueError"

failed = False
try:
    _ = fac("n")
except TypeError:
    failed = True

assert failed, "must be an integer"

failed = False
try:
    _ = fac(2.5)
except TypeError:
    failed = True

assert failed, "must be an integer"



