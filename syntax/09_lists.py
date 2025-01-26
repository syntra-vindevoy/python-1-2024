words = list()
numbers = list()
phrase = ""
phrase_with_delimiter = ""
chars = list()


def reset():
    global words
    words = ["abc", "def", "ghi", "jkl"]
    global numbers
    numbers = [1, 2, 3, 4]
    global phrase
    phrase = "this is fun"
    global phrase_with_delimiter
    phrase_with_delimiter = "this_phrase_has_a_delimiter"
    global chars
    chars = ["z", "y", "a"]


reset()

words_contains = "abc" in words
words_len = len(words)

words_sliced = words[2:3]

words1 = ["abc", "def"]
words2 = ["ghi", "jkl"]
words = words1 + words2

words_time_4 = words * 4

sum = sum(numbers)
min = min(numbers)
max = max(numbers)

# min_words = min(words)
# max_words = max(words)

words.append("extra woord")
words.extend(["extra", "lijst"])

reset()

# remove item by index
popped_item = words.pop(1)

# remove item by item
# list_with_removed_item = words.remove("jkl")
# words.remove returns no value !!!...
words.remove("jkl")

reset()

words = phrase.split()
words = phrase_with_delimiter.split("_")

reset()

delimiter = "|"
joined_words = delimiter.join(words)

some_string = "de kat krabt de krollen van de trap"
looping_list = list()
for word in some_string.split():
    looping_list.append(word)

# gesorteerde lijst, origineel blijft behouden
# result is a list!!!

chars_sorted = sorted(chars)

chars_with_method = chars
chars_with_method.sort()


a = [1, 2, 3]
b = [1, 2, 3]

is_symbol = a == b
is_word = a is b

# OPENEN VAN DOCUMENT NOG TOEVOEGEN

reset()

reversed_words = list(reversed(words))
reversed_chars = " ".join(reversed(chars))
# keert oorspronkelijke set niet om

pass
