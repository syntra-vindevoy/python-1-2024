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


def fact_tail_recursion(n: int, result: int = 1):
    if n == 0:
        return result
    return fact_tail_recursion(n - 1, result * n)


fac(4)


def fact_tail_string_recursion(n: int, result: str = "1"):
    if n < 2:
        return result
    return fact_tail_string_recursion(n - 1, f"{result}*{n}")


fact_tail_recursion(4)
print(fact_tail_string_recursion(5))
