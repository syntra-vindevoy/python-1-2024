def value_counts(word):
    d = {}
    for letter in word:
        d [letter] = d.get(letter, 0) + 1
        print (d)
value_counts("hallo")
