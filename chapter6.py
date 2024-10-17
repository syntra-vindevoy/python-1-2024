def fac(n: int | n: float) -> int:
    if type(n) != int:
        if type(n) != float:
                raise TypeError("fac() only accepts integer or float arguments")
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

failed = false
try:
    _= fac("a")
except TypeError:
    failed = True

assert fac(2.0) ==2

assert failed, "Only integers are valid"

failed = false
try:
    _ = fac(2.5)
except TypeError:
    failed = True

assert failed, "Only floats are valid"

