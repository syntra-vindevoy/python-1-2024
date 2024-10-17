#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000.
#Otherwise, return their sum.

def calculation(a: int, b: int) -> int:
    if a * b <= 1000:
        return a * b
    else:
        return a + b

print(calculation(20, 30))
print(calculation(40, 30))
