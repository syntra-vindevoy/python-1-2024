def is_palindroom(a: list, b: list) -> bool:
    return a == list(reversed(b))


print(is_palindroom([1, 2, 3], [3, 2, 1]))
print(is_palindroom([4, 2, 3], [3, 2, 1]))
print(is_palindroom([1, 3, 2], [3, 2, 1]))