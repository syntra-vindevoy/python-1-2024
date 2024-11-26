c = ["cheddar", "parmesan", "brie", "feta"]

print(c)

d = c               #assign a variable to a mutable --> will always change when the source changes
e = c.copy()

c.append("mozzarella")
print(c)
print(len(c))

print(d)
print(e)
