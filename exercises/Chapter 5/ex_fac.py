import numpy

def fac(n: int) -> int:



    #if n == 0:
    #    return 1
    # in math, the definition for 0 and 1 always returns as 1
    if n < 2:
        return 1

    #if n == 1:
    #   return 1

    #starting with r = n to avoid an extra loop in the range which would otherwise be (2, n+1)
    r = n

    ###
    # sidchiv 2024-10-10
    # explanation ...
    # starting from 2 because multiplication with 1 makes no sense
    for i in range(2, n):
        r *= i #zelfde als r = r * i

    return r
    ###

def fac3(n: int) -> int:

    if n < 2:
        return 1

    return int(numpy.prod(range(2, n + 1)))


def main():

    print(fac3(6))

    assert fac(0) == 1
    assert fac(1) == 1
    assert fac(2) == 2
    assert fac(3) == 6
    assert fac(4) == 24
    assert fac(5) == 120

if __name__ == '__main__':
    main()




































