"""
Opdracht 2.1
author : Benoit Goethals
"""


def faculteit_range(n) -> int:
    """
    Faculitieit using range
    :param n: An integer for which the factorial-like calculation is to be performed.
    :return: The result of multiplying the input number by all integers from 2 up to one less than the input number.
    """
    if n < 2:
        return 1
    r = n
    for i in range(2, n):
        r *= i
    return r


assert faculteit_range(0) == 1
assert faculteit_range(1) == 1
assert faculteit_range(2) == 2
assert faculteit_range(3) == 6
assert faculteit_range(4) == 24
assert faculteit_range(5) == 120


def faculteit_while(n: int) -> int:
    """
    Faculitieit using while loop
    :param n: The non-negative integer whose factorial is to be computed.
    :return: The factorial of the given integer.
    """
    if n < 2:
        return 1
    r = n
    i = 2
    while i < n:
        r *= i
        i += 1
    return r


assert faculteit_while(0) == 1
assert faculteit_while(1) == 1
assert faculteit_while(2) == 2
assert faculteit_while(3) == 6
assert faculteit_while(4) == 24
assert faculteit_while(5) == 120


def faculteit_recursive(n: int) -> int:
    """
    faculitieit using recursion
    :param n: The integer number for which the factorial is to be calculated.
    :return: The factorial of the given integer n. Returns 1 if n is 0 or 1, otherwise calculates recursively.
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return n * faculteit_recursive(n - 1)


assert faculteit_recursive(0) == 1
assert faculteit_recursive(1) == 1
assert faculteit_recursive(2) == 2
assert faculteit_recursive(3) == 6
assert faculteit_recursive(4) == 24
assert faculteit_recursive(5) == 120
