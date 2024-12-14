def avoids(word, forbidden):
    return any(ch in forbidden.lower() for ch in word.lower())

fin = open('words.txt')

for word in fin:
   if avoids(word, 'lobs') == True:
       print(word)