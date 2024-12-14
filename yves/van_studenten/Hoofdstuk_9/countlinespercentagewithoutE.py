def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

with open(r"words.txt", 'r') as wordlist:
    num_of_words = len(wordlist.readlines())
    print('Total lines: ', num_of_words)

fin = open('words.txt')
count = 0

for line in fin:
    if has_no_e(line) == True:
        count += 1

print("Lines without e: ", count)
print(count / num_of_words * 100, '%')


