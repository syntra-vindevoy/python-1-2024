word_list = []

for line in open('words.txt'):
    word = line.strip()
    word_list.append(word)

print(len(word_list))

oneliner = open('words.txt').read()
print(len(oneliner))

oneliner_list = oneliner.split()
print(len(oneliner_list))

for word in word_list:
    if word == 'demotic':
        print(word)

