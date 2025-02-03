x = (1, 2)

y = 1, 2

print(type(x))
print(type(y))


a = 1
b = 2

a, b = b, a

c = (a, b)

y = ("yves",)
print(y)

print(y[0])
print(len(y))

print(sorted(tuple("yves")))


# t = (1, 2, "y", [1, 2, 3])
# print(sorted(t))

a, b = 1, 2
print(a)


d, e, _, f = 1, 2, 3, 4

print(_)