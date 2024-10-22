import numpy

def fac(n: int):
    if n < 2:
        return 1
    else:
        return n * fac(n - 1)

def fact2(n: int):
    r = 1
    for i in range(n, 1, -1):
        r = r * i
        return r


def fact3(n: int):
    """
    this function calculates the faculty of a positive integer n

    :param n:
        int: the number on wich we calcualte the faculty
    :return:
        int: the calculated faculty
    """
    if n < 2:
        return 1
    else:
        r = n

        for i in range(2, n):
            r = r * i

    return r


# deze maakt geen winst, duurt langer.omdat hij hiervoor elke keer een call moet maken. en die is veel te duur in tijd.
def fac4(n: int) -> int:
    if n < 2:
        return 1

    return int(numpy.prod(range(2, n + 1)))


print(fac4(3))
