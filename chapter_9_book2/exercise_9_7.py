from operator import truediv

with open("words.txt", "r") as f:
    words = f.read().split("\n")
def has_no_e(word):
    if word.find("e") == -1: return True

#print (has_no_e("hllo"))


def cons_dubble (word):
    for letter in word:
        pos = word.find(letter)
        if len(word) - pos < 6 : return False #stopt wanneer er maar 5 letters over blijven
        if letter == word[pos + 1] and word[pos + 2] == word[pos + 3] and word[pos + 4] == word[pos + 5]: return True

a = []
for word in words:
    if len(word) > 3:
        if cons_dubble(word):
            a.append(word)

print (f"({len(a)} words found: {a}")
