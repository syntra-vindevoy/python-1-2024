def has_no_e(word):
    for letter in word:
        if letter == 'e':
            break
    else:
        print(word)

fin = open('words.txt')

for line in fin:
    word = line.strip()
    has_no_e(word)



