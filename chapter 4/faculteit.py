import numpy


def fac (n):
    result = 1
    for i in range (1, n+1):
        result = i * result
    print (result)

fac (6)


def fac (n):
    """
            Calculate the factorial of a given number using an iterative approach.

            This function calculates the factorial of `n` by starting with the value `n`
            as the initial result and then iteratively multiplying it by integers from 2
            to `n-1`. The function prints the final factorial value instead of returning it.

            Parameters
            ----------
            n : int
                A non-negative integer for which the factorial is to be calculated.

            Notes
            -----
            - This function assumes `n` is a positive integer greater than or equal to 2.
            - The calculation starts by initializing the result to `n` and multiplies by
              all integers from 2 up to `n-1`, which saves one multiplication step
              compared to the traditional factorial algorithm starting with 1.

            Examples
            --------
            >>> fac(5)
            120

            Notes:
                Author: Kenneth Teck
                Date: 10-10-2024
                version: 1.2.0
            Notes:
                Author: Kenneth Teck
                Date: 10-10-2024
                version: 1.2.1
                Bugfix: add ...
            """
    result = 1
    for i in range (2, n+1):
        result = i * result
    print (result)

fac (6)

def fac (n): #heeft 1 stap minder nodig (*startwaarde ipv *1)
    def fac(n):
        """
    2024-10-10
    This function calculates the factorial of a integer, in math it is called the facility.
    :param n: integer from which the facility is to be calculated
    :return: integer, factorial of n
    """
    if n < 0:
        return "Error"

    if n < 2:
        return 1

    result = n
    for i in range (2, n):
        result = i * result
    return result

print (fac(6))

def fac (n):
    if n < 0:
        return "Error"

    if n < 2:
        return 1

    return numpy.prod(range(2, n + 1))  #speciale import maar veel trager

print (fac(5))

