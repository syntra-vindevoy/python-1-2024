me = "Yves"

print(type(me))

# Both will be True
print(type(me) == str)
print(isinstance(me, str))


# Class A is a bse class for B, see this as A being Animal, B a dog.  B is more specific than A.  Yet, any B is also an A.
# With isinstance, this is correct, with type it is not.  Therefore, depending on what you really want to do,
# use either type if you want to know it exact, or isinstance with inherited classes
class A:
    pass

class B(A):
    pass

b = B()

print(type(b))
print(type(b) == B)
print(isinstance(b, B))

print(type(b) == A)
print(isinstance(b, A))


# Don't use this if not needed
print(me.__class__)

