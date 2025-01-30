x=(1, 2)

y=1, 2

print(type(x))
print(type(y))

a = 1
b = 2

a, b = b, a

c = (a, b)

print(a, b, c)

y = tuple('Yves')
print(y)

y=("Yves",)
print(y)
print(y[0])
print(len(y))

print(tuple("yves"))

print(sorted(tuple("yves")))

#t=(1,2,"y",[1,2,3])
#print(sorted(t))

a, b = 1, 2
print(a)
print(b)

d, e, _ = 5, 6, 7

# d, e, _,f = 1, 2, 3, 4

print(d)
print(e)
print(_)
