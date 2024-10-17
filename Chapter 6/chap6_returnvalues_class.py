def fac(n: int) -> int:
    if type(n) != int:
        raise TypeError('n must be an integer')

    if n <= 0:
        raise ValueError('n must be positive')

    return 1 if n < 2 else n * fac(n - 1)

assert fac(0) == 1
assert fac(1) == 1
assert fac(2) == 2
assert fac(3) == 6
assert fac(4) == 24
assert fac(5) == 120

#errors testen (negatieve getallen)
failed = False
try:
    _ = fac(-1)
except ValueError:
    failed = True

assert failed, "Negative factorials should raise a ValueError"

#errors testen (string)
failed = False
try:
    _ = fac("a")
except TypeError:
    failed = True

assert failed, "Only integers are valid factorial arguments"
