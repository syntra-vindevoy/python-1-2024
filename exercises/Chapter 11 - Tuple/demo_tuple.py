x = (1, 2)
y = 1, 2

print(type(x))
print(type(y))

a = 1
b = 2

a, b = b, a
print(a, b)

c = (a, b)

y = tuple('yves')
y2 = ('yves', )
print(y)
print(y2)

print(sorted(tuple('yves')))

t = (1, 2, 'y', [1, 2, 3])
print(t)

d, e, _ = 1, 2, 3
#voor wanneer men de 3de niet wilt gebruiken.