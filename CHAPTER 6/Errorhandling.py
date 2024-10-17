#raised erros opzoeken

def fac(n: int) -> int:   # def fac(n: int | float) -> pipeline symbool
    if type(n) != int:
        if type(n) != float:
        raise TypeError("fac() only accepts integer arguments")


    if n < 0:
        raise ValueError("fac() only accepts positive integers")


    return 1 if n < 2 else n * fac(n - 1)



assert fac(0) == 1
assert fac(1) == 1
assert fac(2) == 2
assert fac(3) == 6
assert fac(4) == 24
assert fac(5) == 120


#-----------------## RAISE ERRORS ##-----------------#

# Om negatieve integers te testen
failed = False
try:
    _ = fac(-1)
except ValueError:
    failed = True

assert failed, "Negative factorial should raise a ValueError"


# Om na te gaan of het een integer is en geen string
failed = False
try:
    _ = fac("a")
except TypeError:
    failed = True

assert fac(2.0) == 2
assert failed, "Only integers or whole floats are valid factorial arguments"




failed = False
try:
    _ = fac("2.0")
except TypeError:
    failed = True

assert failed, "Only integers are valid factorial arguments"

