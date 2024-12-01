def divide(a: int, b: int, text: str = ""):
    return a / b


print(divide(a=6, b=2))
print(divide(
    b=2,
    a=6
))
print(divide(2, b=2))


def test_divide():
    assert divide(6, 2) == 3
    assert divide(6, 3) == 2

# test_divide()
