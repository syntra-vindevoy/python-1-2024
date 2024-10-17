from operator import truediv


def fac(n/ int) -> int:
    if type(n) != int:
        raise TypeError("fac() only accepts integer arguments")

    if n<0:
        raise ValueError("fac() only accepts positive integers")

    return 1 if n < 2 else n * fac(n-1)


assert fac(0) == 1
assert fac(1) == 1

failed = false
    try:
        _= fac(-1)
except ValueError:
    failed = true

assert failed, "Negative factorial should raise a ValueError"
