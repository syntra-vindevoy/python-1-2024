a = 1
b = a

assert b == 1

a = 2

assert b == 1


a = [1, 2, 3]
b = a
c = a.copy()

assert b == [1, 2, 3]

a.append(4)

assert b == [1, 2, 3]  # Error here
assert c == [1, 2, 3]
