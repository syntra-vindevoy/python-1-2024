# import math
import numpy
# from math import factorial
# n1 = 3
# print(math.factorial(n1))
#
# # for _ in range(1, !):
# #     print (n)
#
# def factorial(n1):
#     fact = 1
#     for num in range(2, n1 + 1):
#         fact *= num
#     return fact

def factorial1(n):
    if n < 2:
        return 1
    r = n
    for i in range (2, n):
        r *= i
    return r

def fac3(n):
    if n < 2:
        return 1

    return numpy.prod(range(2, n + 1))

# def voorbeeld_functie(param1, param2):
# voorbeeld docstring dummy in rst taal - created by AI
    """
    Voorbeeld functie

    Deze functie berekent de som van twee parameters.

    :param param1: De eerste parameter
    :type param1: int
    :param param2: De tweede parameter
    :type param2: int
    :returns: De som van param1 en param2
    :rtype: int
    :raises ValueError: Als een van de parameters geen integer is
    """
#     if not isinstance(param1, int) or not isinstance(param2, int):
#         raise ValueError("Beide parameters moeten integers zijn.")
#     return param1 + param2
# print(factorial(n))
print(factorial1(4))

lst = [1, 12, 7, 4, 10]
lst.sort
print(lst)