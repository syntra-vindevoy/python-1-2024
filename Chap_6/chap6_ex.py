def fac(n: int | float) -> int:
    if type(n) != int:
        if type(n) != float:
            raise TypeError("fac() argument must be an integer")

        if int(n) != n:
            raise TypeError("fac() argument must be an integer or whole number")

    if n < 0:
        raise ValueError("fac() argument can not be negative")

    return 1 if n < 2 else n * fac(n-1)

assert fac(0) == 1
assert fac(1) == 1
assert fac(2) == 2
assert fac(3) == 6
assert fac(4) == 24
assert fac(5) == 120
assert fac(6) == 720

failed = False
try:
    _ = fac(-1)
except ValueError:
    failed = True

assert failed, "TypeError not raised for negative argument"

failed = False
try:
    _ = fac("a")
except TypeError:
    failed = True

assert failed, "TypeError not raised for non-integer argument"

assert fac(2.0) == 2

assert failed, "only integer or float arguments are accepted"

try:
    _ = fac(2.5)
except TypeError:
    failed = True

assert failed, "TypeError not raised for non-integer argument"