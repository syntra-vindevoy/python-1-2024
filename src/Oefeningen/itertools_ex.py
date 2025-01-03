import itertools

combinations = itertools.combinations([1, 2, 3, 4, 5],2)
print(list(combinations))

combinations_with_replacement = itertools.combinations_with_replacement([1, 2, 3, 4, 5],2)
print(list(combinations_with_replacement))

permutations = itertools.permutations([1, 2, 3, 4, 5],2)
print(list(permutations))

product = itertools.product([1, 2, 3, 4, 5],repeat=2)
print(list(product))

accumulate = itertools.accumulate([1, 2, 3, 4, 5])
print(list(accumulate))

grouper = itertools.groupby([1, 2, 3, 4, 5, 6, 7, 8, 9], lambda x: x % 2 == 0)
for key, group in grouper:
    print(key, list(group))

persons = [
    {"name": "John", "age": 36},
    {"name": "Anne", "age": 29},
    {"name": "Lisa", "age": 33},
    {"name": "camil", "age": 33},
    {"name": "liv", "age": 33},
    {"name": "muse", "age": 36},
]

sorted_persons = sorted(persons, key=lambda x: x["age"])
print(sorted_persons)

grouped_persons = itertools.groupby(sorted_persons, key=lambda x: x["age"])
for key, group in grouped_persons:
    print(key, list(group))


for i in itertools.count(10):
    print(i)
    if i >= 20:
        break

for i in itertools.cycle([1, 2, 3]):
    print(i)
    if i >= 3:
        break

for i in itertools.repeat(1, 5):
    print(i)



