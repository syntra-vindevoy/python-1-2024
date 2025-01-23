def value_counts(word):
    d = {}
    for letter in word:
        d [letter] = d.get(letter, 0) + 1
    return d
#print(value_counts("hallo"))

def find_repeats(word):
    value_count = value_counts(word)
    d = []
    for key, value in value_count.items():
        if value > 1:
            d.append(key)
    return d

print(find_repeats("ouzdhciukjzhdkchlk"))

"""Write function called find_repeats that takes a dictionary that maps from each key to a counter, 
like the result from value_counts. 
It should loop through the dictionary and return a list of keys that have counts greater than 1. 
You can use the following outline to get started."""

