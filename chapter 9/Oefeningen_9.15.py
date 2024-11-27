
def is_anagram (x,y):
    return sorted(x.upper()) == sorted(y.upper())
print(is_anagram("Oude", "eduo"))

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

print (total_lenght(["Count", "the", "lenght", "of", "This", "list", "of", "strings"]))
