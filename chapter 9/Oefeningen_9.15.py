with open("words.txt", "r") as f:
    words = f.read().split("\n")

def is_anagram (x,y):
    return sorted(x.upper()) == sorted(y.upper())
print(is_anagram("Oude", "eduo"))

def anagram_list():
    anagram =[]
    for word in words:
        if is_anagram (word,"takes"):
            anagram.append(word)
    print (anagram)
anagram_list()

def method_yves():
    i = "takes"
    w = [word for word in words if len(word) == len(i)]
    for a in i:
        w =[word for word in w if a in word]
    return [word for word in w if sorted(w) == sorted(i)]
print(method_yves())

def is_palindrome(word):
    return word.upper() == word[::-1].upper()
print (is_palindrome("odo"))

def is_voodoo (word):
    return is_palindrome(word[1:])
print(is_voodoo("voodoo"))

def reverse_sentence(sentence):
    sent = sentence.lower().split()
    sent = sent [::-1]
    sent [0] = sent[0].capitalize()
    sent = " ".join(sent)
    print (sent)

reverse_sentence("Reverse this sentence")


def total_lenght(lijst):
    total = 0
    for word in lijst:
        total += len(word)
    return total

print (total_lenght(words))

def total_lenght_2():
    total = "".join(words)
    return len(total)
print (total_lenght_2())

def total_lenght_3():
    with open("words.txt", "r") as f:
        words = f.read()
    words = words.replace("\n", "")
    print (len(words))
total_lenght_3()

def total_lenght_4():
    with open("words.txt", "r") as f:
        words = f.read()
    print (len(words) - words.count("\n"))
total_lenght_4()
