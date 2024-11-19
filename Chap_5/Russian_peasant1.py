def russian_peasant_multiplication(a, b):
    result = 0  # Initialize result

    while b > 0:
        # If the second number is odd, add the first number to the result
        if b % 2 != 0:
            result += a

        # Double the first number and halve the second number
        a = a * 2
        b = b // 2

    return result


# Example usage
num1 = 254
num2 = 369

print(
    f'The result of {num1} * {num2} using Russian Peasant Multiplication is: {russian_peasant_multiplication(num1, num2)}')


def russian_peasant_multiplication1(a, b):
    if b == 0:
        return 0
    elif b % 2 != 0:
        return a + russian_peasant_multiplication1(a * 2, b // 2)
    else:
        return russian_peasant_multiplication1(a * 2, b // 2)


# Example usage
num1 = 18
num2 = 24

print(
    f'The result of {num1} * {num2} using Russian Peasant Multiplication is: {russian_peasant_multiplication1(num1, num2)}')


def russian_peasant_multiplication3(a, b):
    results = [a * (2 ** i)
               for i in range(b.bit_length()) if (b >> i) & 1]
    return sum(results)


# Example usage
num1 = 236
num2 = 369

print(
    f'The result of {num1} * {num2} using Russian Peasant Multiplication is: {russian_peasant_multiplication3(num1, num2)}')


def fac(n: int, t: int = 1) -> int:
    if n < 2:
        return t

    return fac(n - 1, n * t)

assert fac(0) == 1
assert fac(1) == 1
assert fac(2) == 2
assert fac(4) == 24
assert fac(5) == 120
assert fac(6) == 720
