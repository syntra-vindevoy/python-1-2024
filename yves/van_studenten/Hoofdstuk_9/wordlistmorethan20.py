fin = open('words.txt')

for line in fin:
    if len(line) > 20:
        print(line)
    else:
        pass