from itertools import groupby
from pprint import pprint


names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
names.sort()
grouped = groupby(names, lambda x: x[0])


for key, group in grouped:
    print(key, list(group))
    

# Create a new groupby object
grouped = groupby(names, lambda x: x[0])


result_with_dict = {}
for key, group in grouped:
    result_with_dict[key] = list(group)  # Convert group to list
pprint(result_with_dict)


result_with_comprehension_1 = {key: list(group) for key, group in grouped}

pprint(result_with_dict)

