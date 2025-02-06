example = {}

print(type(example))

numbers = {'zero' : 0, 'one' : 1, 'two' : 2}

print(numbers)

#print(numbers.values())
#print(numbers.items())
#print(numbers.keys())

def value_counts(string):
    counts = {}
    for i in string:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] = counts[i] + 1
    return counts

counter = value_counts('bert is python')

for key in counter:
    print(key)

for value in counter.values():
    print(value)

for key in counter:
    value = counter[key]
    print(key, value)

#print(value_counts('bert is python aan het studeren.'))