
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

counter = value_counts("brontosausus")
print(counter)

print(counter.get("u", 0))