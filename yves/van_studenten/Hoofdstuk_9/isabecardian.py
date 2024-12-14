def is_abecedarian(word):
    previous_letter = word[0]
    for c in word:
        if c < previous_letter:
            return False
        previous = c
    return True

fin = open('words.txt')

for word in fin:
    if is_abecedarian(word):
        print(word)