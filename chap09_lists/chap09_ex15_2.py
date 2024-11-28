from chap09_is_anagram import is_anagram

#Correct way, because the context manager "with" already closes the file for you at the end
with open("words.txt", "r") as f:
    words = f.read().split("\n")

#print(words)
#print(type(words))

for word in words:
    if is_anagram(word, "takes"):
        print(word)

anagrams = [word for word in words if is_anagram(word, "takes")]
print(anagrams)




###Classic way, but bad way, because you have to close the file at the end
#f = open("words.txt", "r")
#words = f.read().split("\n")
#f.close()

