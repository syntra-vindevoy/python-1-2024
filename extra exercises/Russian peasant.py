from math import floor


def russian_peasant(a, b):
    """
    Russian Peasant Algorithm writen out in python

    parameters
    ----------
        a: int
            First number to multiply
        b: int
            Second number to multiply
    returns
    -------
        result: int
            the result of the multiplication after being run through the algorithm

    author
    ------
        Chiel

    date
    ----
        16-11-2024
    """

    result = 0

    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        while a != 0:
            if floor(a % 2) != 0:
                result += b
                a = (a / 2)
                b = (b * 2)

            else:
                a = floor(a / 2)
                b = floor(b * 2)

        return result

def main():
    print(russian_peasant(50, 237))

    assert russian_peasant(10, 10) == 100
    assert russian_peasant(10, 5) == 50
    assert russian_peasant(10, 3) == 30
    assert russian_peasant(10, 1) == 10
    assert russian_peasant(50, 237) == 11850

if __name__ == "__main__":
    main()
