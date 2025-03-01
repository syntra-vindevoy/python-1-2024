from datetime import datetime
from functools import reduce

import numpy
def fac(n: int) -> int:
    if n == 1:
        return 1

    if  n > 1:
        return n * fac1(n-1)

#herschreven functie zonder recursie
def fac2(n: int) -> int:
    #docstrings
    """
        This function calculates the faculty of a positive integer n. in math this is n!
    :param n:
        int: The number on which we calculate the faculty
    :return:
        int: The calculated faculty

    Notes:
        Author: Marta
        Date: 2024-10-10
        Version: 1.0.0
    """
    # in math, the definition for 0 and 1 states that the result is 1
    if n < 2:
        return 1
   #if n == 1: --> is overbodig
        #return 1

    # starting with r = n to avoid an extra loop in the range which would otherwise be (2, n+1)
    r = n

    ###
    #marta - 2024-10-10
    #i fixed this (met reden en op duidelijke manier)
    # starting from 2 because multiplication by 1 makes no sense
    for i in range(2, n):
        r *= i #verkorte notatie r = r * i
    ###

    return r

def fac3(n: int) -> int:
    if n < 2:
        return 1

    return int(numpy.prod(range(2,n + 1)))

def fac4(n: int) -> int:
    return 1 if n < 2 else reduce(lambda x, y: x * y, range(2, n + 1)) #

def main():
    fac = fac4
    assert fac(0) == 1
    assert fac(1) == 1
    assert fac(2) == 2
    assert fac(3) == 6
    assert fac(4) == 24
    assert fac(5) == 120

if __name__ == '__main__':
    start = datetime.now()

    for _ in range(50000):
        main()

    end = datetime.now()
    print(end - start)

#resultaat die je niet mag gebruiken (recursie en import)
#from dateime import datetime
#def fac(n:int) -> int:
#   if n == 0
#       return 1
#
#   if n == 1:
#       return 1
#
#   if n > 1:
#       return n * fac(n-1)

#def main ():
#    assert fac(0) == 1
#   assert fac(1) == 1
#   assert fac(2) == 2
#   assert fac(3) == 6
#   assert fac(4) == 24
#   assert fac(5) == 120

# if __name__