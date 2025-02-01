list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
t

t[1].append(6)  # AttributeError: 'tuple' object has no attribute 'append'
print(t)
