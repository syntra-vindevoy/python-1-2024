import math
from itertools import repeat

from IPython.lib.pretty import Printable

print(8^9)
abs(-40)
print(abs(-40))
print(int(42.9))
print(float(42))
print(type(2))
print(type('126'))
print(int('126') / 3)

from math import *
print(math.floor(3.0))

print(2++2)
print(type('2 pi'))
print(pi)
from keyword import kwlist
print(kwlist)

n=12
print(n + 1)
print(n + 2)


def print_verse():
    print("test")
def print_n_verses(n):
    for i in range(n):
        print_verse()  # Calls the function to print a single verse
# Example usage
print_n_verses(3)  # Prints 3 verses



