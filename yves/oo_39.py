my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)

my_list = [i for i in range(10)]
print(my_list)

my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)

my_dict = {}

for i in range(10):
    my_dict[i] = i
print(my_dict)

my_dict = {i: i for i in range(10)}
print(my_dict)

my_dict = {chr(i + 97): i + 1 for i in range(26)}
print(my_dict)