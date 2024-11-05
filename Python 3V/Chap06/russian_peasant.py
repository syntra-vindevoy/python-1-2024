# recursie code YVES
def russian_peasant(a: int, b: int) -> int:
    if b == 0:
        return 0
    elif b % 2 != 0:
        return a + russian_peasant(a * 2, b // 2)
    else:
        return a + russian_peasant(a * 2, b // 2)



"""

def russian_peasant_multiplication(a, b):
    result = 0

    while a > 0:
        if a % 2 == 1:
            result += b

        a //= 2
        b *= 2

    return result


# Voorbeeld gebruik:
num1 = 18
num2 = 24
product = russian_peasant_multiplication(num1, num2)
print(f"The product of {num1} and {num2} is: {product}")

"""