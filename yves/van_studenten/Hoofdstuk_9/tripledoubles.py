def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

fin = open('words.txt')

def find_triple_double():
    for word in fin:
        if is_triple_double(word):
            print(word)


print ('Here are all the words in the list that have')
print ('three consecutive double letters.')
find_triple_double()
