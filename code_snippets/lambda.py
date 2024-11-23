add_ten = lambda x: x + 10
print(add_ten(5))  # 15

multiply = lambda x, y: x * y
print(multiply(2, 3))  # 6


def apply_function(func, arg):
    return func(arg)


print(apply_function(lambda x: x + 10, 5))  # 15

numbers = [1, 2, 3, 4, 5]
