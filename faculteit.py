import numpy


def fac(n):
    """
    this is the documentation of fac(n)

    """
    if n < 2:
        return 1
    result = n
    for i in range(2, n):
        result *= result * i
    return result


def fac2(n: int):
    return numpy.prod(range(2, n + 1))


fac(4)
