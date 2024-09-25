name = "Thomas"

print(type(name))

print(type(name) == str)
print(isinstance(name, str))

class A:
    pass

class B(A):
    pass

a = A()

print(type(a))

b = B()

print(type(b))
print(type(b) == B)
print(isinstance(b, B))

print(type(b) == A)         #type doesn't take into account inheritance
print(isinstance(b, A))     #isinstance takes into account inheritance --> usage of isinstance is better!!!!

print(type((4,2)))
