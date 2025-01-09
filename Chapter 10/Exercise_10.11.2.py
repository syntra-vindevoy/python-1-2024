# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example, here’s a dictionary that maps
# from the letters in a string to the number of times they appear.

def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

#If we look up a letter that appears in the word, get returns the number of times it appears.
counter = value_counts('brontosaurus')
print(counter.get('b', 0))

#If we look up a letter that doesn’t appear, we get the default value, 0.
print(counter.get('c', 0))

#Use get to write a more concise version of value_counts. You should be able to eliminate the if statement.
def value_counts_2(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

print(value_counts_2("banaan"))
