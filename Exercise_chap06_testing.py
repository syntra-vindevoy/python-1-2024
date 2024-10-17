def factorial(n :int | float):
    if type(n) != int:
        if type(n) != float:
            raise TypeError('n must be an integer')
        if int(n) != n:
            raise TypeError('factorial only accepts whole numbers')
    if n<0:
        raise ValueError('n must be >= 0')

    return 1 if n < 2 else n*factorial(n-1)

assert factorial(2) == 2
assert factorial(4) == 24
assert factorial(5) == 120

failed = False
try:
    _ = factorial(-1)
except ValueError:
    failed = True

assert failed, "negative factorial should raise a ValueError"

failed = False
try:
    _ = factorial("a")
except TypeError:
    failed = True

assert failed, "only integers are valid factorial arguments"

failed = False
try:
    _ = factorial(2.5)
except TypeError:
    failed = True

assert failed, "only integers or whole floats are valid factorial arguments"