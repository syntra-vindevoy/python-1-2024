#square root exercise
# import math
# def mysqrt(a):
#     x = a / 2  # Initial guess
#     epsilon = 0.0000001  # Desired level of precision
#
#     while True:
#         y = (x + a / x) / 2
#         if abs(y - x) < epsilon:
#             return y
#         x = y
#
#
# def test_square_root():
#
#     print('a   mysqrt(a)        math.sqrt(a)    diff')
#     print('-   ---------        ------------    ----')
#
#     for a in range(1, 10):
#         a = float(a)
#         my_sqrt = mysqrt(a)
#         math_sqrt = math.sqrt(a)
#         diff = abs(my_sqrt - math_sqrt)
#         print(f'{a:.1f} {my_sqrt:<16.11f} {math_sqrt:<16.11f} {diff}')
#
#
# if __name__ == '__main__':
#     test_square_root()

##################################################################
#Eval loop exercise
#import math


# def mysqrt(a):
#     """
#     Calculate the square root of a number using Newton's method
#     """
#     x = a / 2  # Initial guess
#     epsilon = 0.0000001  # Desired level of precision
#
#     while True:
#         y = (x + a / x) / 2
#         if abs(y - x) < epsilon:
#             return y
#         x = y
#
#
# def test_square_root():
#
#
#     print('a   mysqrt(a)        math.sqrt(a)    diff')
#     print('-   ---------        ------------    ----')
#
#     for a in range(1, 10):
#         a = float(a)
#         my_sqrt = mysqrt(a)
#         math_sqrt = math.sqrt(a)
#         diff = abs(my_sqrt - math_sqrt)
#         print(f'{a:.1f} {my_sqrt:<16.11f} {math_sqrt:<16.11f} {diff}')
#
#
# if __name__ == '__main__':
#     test_square_root()
#
#
# ########################
# #Estimate pi
import math


def factorial(n):

    if n == 0:
        return 1
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


def estimate_pi():

    k = 0
    total = 0
    constant = 2 * math.sqrt(2) / 9801

    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        term = constant * num / den

        if abs(term) < 1e-15:
            break

        total += term
        k += 1

    return 1 / total


if __name__ == '__main__':
    estimated_pi = estimate_pi()
    print('Estimated π:', estimated_pi)
    print('Math.pi:', math.pi)
    print('Difference:', abs(estimated_pi - math.pi))