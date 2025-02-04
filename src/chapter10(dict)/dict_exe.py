dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1['a'])
print(dict1.get('a'))
print(dict1.get('d'))
print(dict1.get('d', 4))
dict1['a'] = 10
print(dict1)
dict1['d'] = 4
print(dict1)
dict1.update({'e': 5, 'f': 6})

print(dict1['a'])

del dict1['a']

print(dict1)

dict1.popitem()
print(dict1)

if 'b' in dict1:
    print('b in dict1')


for k,v in dict1.items():
    print(k,v)

new_dict = dict(dict1)
print(new_dict)


dicct3 = {'a': 10, 'b': 9, 'c': 6}
dicct3.update(dict1)
print(dicct3)

direr = {}
direr[0] = "test"
direr[1] = "test"
print(direr)
direr[0] = "kaka"
print(direr)