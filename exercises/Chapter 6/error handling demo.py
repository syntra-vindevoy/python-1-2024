def fac(n: int | float) -> int: #  |  als symbool om meer dan een type mee te geven

    if type(n) != int:
        if type(n) != float:
            raise TypeError('n must be an integer or float')

        if int(n) != n:
            raise TypeError('fac() only accepts float arguments that are whole numbers')

    if n < 0:
        raise ValueError('n must be >= 0')

    return 1 if n < 2 else n * fac(n - 1)

assert fac(0) == 1
assert fac(1) == 1
assert fac(2) == 2
assert fac(3) == 6
assert fac(4) == 24
assert fac(5) == 120

failed = False
try:
    _ = fac(-1)
except ValueError:
    failed = True

assert failed, "Negative factorial should raise a value error"

failed = False
try:
    _ = fac("a")
except TypeError:
    failed = True

assert failed, "Only integers are valid factorial arguments"

assert fac(2.0) == 2

failed = False
try:
    _ = fac(2.5)
except TypeError:
    failed = True

assert failed, "Only integers are valid factorial arguments"