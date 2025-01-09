#Write function called find_repeats that takes
#a dictionary that maps from each key to a counter,
# like the result from value_counts. It should loop through the dictionary
# and return a list of keys that have counts greater than 1.
# You can use the following outline to get started.

def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    repeats = []
    for key in counter:
        if counter[key] > 1:
            repeats.append(key)

    return repeats

counter = {'a': 2, 'b': 1, 'c': 3, 'd': 1}
result = find_repeats(counter)

print(result)