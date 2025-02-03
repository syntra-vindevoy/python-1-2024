from datetime import datetime
from functools import reduce

import numpy


def fac1(n: int) -> int:
    if n == 0:
        return 1

    if n == 1:
        return 1

    if n > 1:
        return n * fac1(n - 1)


def fac2(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer `n` using an iterative approach.

    The factorial of a non-negative integer n, denoted as n!, is the product of all
    positive integers less than or equal to n. By definition, the factorial of 0 and 1 is 1.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input integer `n`.

    Raises:
        ValueError: If `n` is a negative integer.

    Examples:
        fac2(5) -> 120
    """

    # in math, the definition for 0 and 1 states that the result is 1
    if n < 2:
        return 1

    # Starting with r = n to avoid an extra loop in the range which would otherwise be (2, n+1)
    r = n

    ###
    # sidviny - 2024-10-10
    # Starting from 2 because multiplication by 1 makes no sense
    for i in range(2, n):
        r *= i  # this is the short version of r = r * i
    ###

    return r


# Version: 1.1.0
#        Author: sidviny
#        Date: 2024-10-10
#        New feature: dkjsfmkldsj
#        Bugfix: jkdqsmlj
#
#        Version: 1.0.0
#        Author: <NAME>
#        Date: 2024-10-09

def fac3(n: int) -> int:
    if n < 2:
        return 1

    return int(numpy.prod(range(2, n + 1)))


def fac4(n: int) -> int:
    return 1 if n < 2 else reduce(lambda x, y: x * y, range(2, n + 1))


def main():
    fac = fac3

    assert fac(0) == 1
    assert fac(1) == 1
    assert fac(2) == 2
    assert fac(3) == 6
    assert fac(4) == 24
    assert fac(5) == 120


if __name__ == "__main__":
    start = datetime.now()

    for _ in range(50000):
        main()

    end = datetime.now()
    print(end - start)
