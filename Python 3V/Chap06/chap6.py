from unittest.result import failfast


def fac(n: int) -> int:
    if type(n) != int:
        if type(n) != float:
           raise TypeError("fac() only must be an integer")

    if n < 0:
              raise ValueError('fac() does not accept negative arguments')

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
    except ValueError:(
        failed) = True

assert failed, "Negative Factorial should raise a ValueError"


failed = False
try:
    _ = fac("a")
    except TypeError:
        failed = True

assert failed, "Only integers are valid factorial arguments"


failed = False
try:
    _ = fac(2.0)
    except TypeError:
        failed = True

assert failed, "Only integers are valid factorial arguments"