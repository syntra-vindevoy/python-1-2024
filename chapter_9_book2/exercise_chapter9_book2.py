with open("words.txt", "r") as f:
    words = f.read().split("\n")

def has_no_e(word):
    if word.find("e") == -1: return True

def check_e_in_list():
    a = [word for word in words if has_no_e(word)]
    percentage = len (a) / len(words) * 100
    print (f"There are {percentage:.2f}% of the words without an 'e' \n {a}")

#check_e_in_list()

def cons_dubble (word):
    for letter in word:
        pos = word.find(letter)
        if len(word) - pos < 6 : return False #stopt wanneer er maar 5 letters over blijven
        if letter == word[pos + 1] and word[pos + 2] == word[pos + 3] and word[pos + 4] == word[pos + 5]: return True

def check_cons_dubble():
    a = [word for word in words if cons_dubble(word)]
    print (f"({len(a)} words found: {a}")

#check_cons_dubble()
