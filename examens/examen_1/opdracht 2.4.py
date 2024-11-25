"""
algorithm for russian peasant multiplication
Author : Benoit Goethals
"""


def russian_peasant(a: int, b: int) -> int:
    """
    algorithm for russian peasant multiplication

    :param a: The first integer to be multiplied
    :param b: The second integer to be multiplied
    :return: The product of the two integers calculated using the Russian Peasant multiplication algorithm
    """
    if b == 0:
        return 0
    elif b % 2 != 0:
        return a + russian_peasant(a * 2, b // 2)
    else:
        return russian_peasant(a * 2, b // 2)


assert russian_peasant(24, 16) == 384, "Test case 24x16 failed"
assert russian_peasant(12, 12) == 144, "Test case 12 x 12 failed"
assert russian_peasant(1, 1) == 1, "Test case 1x1 failed"
assert russian_peasant(2, 2) == 4, "Test case 2x2 failed"
assert russian_peasant(3, 3) == 9, "Test case 3x3 failed"
