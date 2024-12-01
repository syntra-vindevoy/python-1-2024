a = (27, 9, 3, 1)
b = (1, -1, -1, -1)

result = tuple([x * y for x, y in zip(a, b)])

print(result)

print(zip(a, b))