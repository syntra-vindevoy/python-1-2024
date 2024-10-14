# n = 6
#
import numpy

def fac1(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(fac1(6))

def fac(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return n * fac(n-1)
print(fac(6))

"""
Calculate the factorial of a non-negative integer `n`.

The factorial of a non-negative integer `n` is the product of all 
positive integers less than or equal to `n`. By definition, the 
factorial of 0 and 1 is 1.

Parameters
----------
n : int
    A non-negative integer to calculate the factorial for.

Returns
-------
int
    The factorial of the given integer `n`.

Examples
--------
>>> fac2(0)
1
>>> fac2(1)
1
>>> fac2(5)
120
>>> fac2(6)
720

Notes
-----
Author: Tom Van de Vyver
Date : 2024-10-10
Version: 1.0.1
new feature: test
Bugfix: test2
    
Version: 1.0.0
Author: Name
Version: 1.0.0
"""


def fac2(n: int) -> int:

# in math, the definition for 0 an 1 states that the result is 1
    if n < 2:
        return 1
# starting with r = n to avoid an extra loop in the range which would otherwise be (2, n + 1)
    r = n
# starting from 2 because multiplication by 1 makes no sense
    for i in range(2, n):
        r *=i
        # this is the short version of r = r * i

    return r
print(fac2(6))

def fac3(n: int) -> int:
    if n < 2:
        return 1
    return int(numpy.prod(range(2, n + 1)))
print(fac3(6))


#     assert fac(0) == 1
#     assert fac(1) == 1
#     assert fac(2) == 2
#     assert fac(3) == 6
#     assert fac(4) == 24
#     assert fac(5) == 120
#     assert fac(6) == 720
#

