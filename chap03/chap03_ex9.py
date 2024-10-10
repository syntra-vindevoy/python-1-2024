#Exercise 9 - Write a func to calc the faculty of a number without recursive
#Also optimizing is investigated, each iteration of the fac'x' is more memory efficient
import numpy
from functools import reduce

def fac1(*, x: int) -> int:
    """
    This function calculates the factorial of a given number.
    :param x:
        int: The number to factorise.
    :return:
        int: The factorial.
    """
    if x == 0:
        return 1

    if x == 1:
        return 1

    result = 1
    if x > 0:
        for i in range(x, 1, -1):
            result = result * i

        return result
    else:
        return 0

def fac2(*, x: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    The factorial of a non-negative integer n, denoted as n!,
    is the product of all positive integers less than or equal to n.
    If x is 0 or 1, the function returns 1. If x is a positive integer,
    it computes the factorial iteratively. If x is negative, the function
    returns 0.

    Parameters
    ----------
    x : int
        A non-negative integer for which the factorial is to be computed.

    Returns
    -------
    int
        The factorial of x if x is non-negative; otherwise, returns 0.

    Examples
    --------
    >>> fac2(x=5)
    120
    >>> fac2(x=0)
    1
    >>> fac2(x=-3)
    0

    Notes
    ------
        Version 1.0.0
        Author: TM
        Date: 20241010
        New Features: ddffd
        Bugfix:
    """

    if x == 0:
        return 1

    if x == 1:
        return 1

    result = 1
    if x > 0:
        for i in range(2, x + 1):
            result = result * i

        return result
    else:
        return 0

def fac3(*, x: int) -> int:
    if x == 0:
        return 1

    if x == 1:
        return 1

    result = x          #one FOR iteration less, because the last iteration is multiply with itself, but here we start with our self
    if x > 0:
        for i in range(2, x):
            result = result * i

        return result
    else:
        return 0

def fac4(*, x: int) -> int:
    #the faculty of 0 & 1 is 1
    if x == 0 or x == 1:
        return 1

    # one FOR iteration less, because the last iteration is multiply with itself, but here we start with our self
    result = x
    if x > 0:
        #Starting from 2, because multiplying by 1 is pointless
        for i in range(2, x):
            result = result * i

        return result
    else:
        return 0

def fac5(*, x: int) -> int:
    if x < 2:
        return 1

    result = x          #one FOR iteration less, because the last iteration is multiply with itself, but here we start with our self
    if x > 0:
        for i in range(2, x):
            result *= i

        return result
    else:
        return 0

def fac6(*, x: int) -> int:             #Way less efficient by using numpy if you execute this code like a million times
    if x < 2:
        return 1

    return int(numpy.prod(range(2, x + 1)))

def fac7(*, n: int) -> int:             #Way less efficient by using numpy if you execute this code like a million times
    return 1 if n < 2 else reduce(lambda x, y: x * y, range(2, n + 1))


print(fac7(n = 5))
