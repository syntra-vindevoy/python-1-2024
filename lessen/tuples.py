"""
from pprint import pprint

x = (1, 2)
y = 1, 2

print(x)
print(y)

type(x)
type(y)


x = ()
y = tuple()

a, b = 1, 2
pprint(a)
pprint(b)

a, b = b, a
a, b = (b, a)

c = (b, a)
a = c[0]
b = c[1]

t1 = (1,)
print(type(t1))

y = tuple("yves")
print(y)

a = 1, 2
b = list(a), 3
print(b)

d, e, _ = 1, 2, 3

d, e, _, _ = 1, 2, 3, 4
print(_)

d, *e = 1, 2, 3, 4
print(e)

d, *e, f = 1, 2, 3, 4
print(e)

email = 'marijnvandenholen@gmail.com'
username, domain = email.split('@')

d = {"one": 1, "two": 2, "three": 3}
for item in d.items():
    print(item)

def main(*args):
    return sum(args) / len(args)

print(main(1, 2, 3, 4, 5))

t = [1, 2, 3, 4]
print(*t)

def toto(**kwargs):
    print(kwargs)

def version_is_newer(old_version,new_version):
 

point = (1, 2)
x, y = point
print(x)
print(y)

"""

tuple_dict = {(1, 2): "tuple_1", (2, 3): "tuple_2", (3, 4): "tuple_3"}

print(tuple_dict[1, 2])  # Output: New York
print(tuple_dict[2, 3])

some_list = [3, 4]
print(tuple_dict[tuple(some_list)])
