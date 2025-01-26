some_tuple = tuple()
some_tuple = "a", "c", "d", 4, 5
some_string = "this is fun"

string_tuple = tuple(some_string)

concat_tuple = tuple("lup") + ("i", "nll")


concat_tuple = concat_tuple * 2

reversed_tuple = tuple(reversed(some_tuple))

a = 1
b = 2
a, b = b, a


d = {"one": 1, "two": 2}
for item in d.items():
    key, value = item
    print(key, "->", value)

for key, value in d.items():
    print(key, "->", value)


quotient, remainder = divmod(7, 3)


def mean(*args):
    return sum(args) / len(args)


scores1 = [1, 2, 4, 5, 1, 5, 2]
scores2 = [5, 5, 2, 2, 5, 2, 3]

for pair in zip(scores1, scores2):
    print(pair)

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))


for index, element in enumerate("abc"):
    print(index, element)


def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


counter = value_counts("banana")
items = counter.items()
items


def invert_dict(d):
    new = {}
    for key, value in d.items():
        if value not in new:
            new[value] = [key]
        else:
            new[value].append(key)
    return new


pass
