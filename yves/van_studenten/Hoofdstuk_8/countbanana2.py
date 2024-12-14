def count_the_a(word):
    return sum(char == 'a' for char in word.lower())

print(count_the_a('BANANA'))

