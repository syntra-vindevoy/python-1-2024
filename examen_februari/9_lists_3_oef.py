def is_anagram(woord_a, woord_b):
    return sorted(woord_a) == sorted(woord_b)

is_anagram('tops','stop')

word_list = []
for line in open('words.txt'):
    word = line.strip()
    if is_anagram(word, 'takes'):
        word_list.append(word)

print(word_list)

# oefening 3:

with open("words.txt", "r") as f:
    words = f.read().split("\n")

def is_palindrome(word):
    return word == word[::-1]

word_list_palindrome = []
for word in words:
    if len(word) >= 7:
        if is_palindrome(word):
            word_list_palindrome.append(word)

print(word_list_palindrome)

def method_2():
    return [word for word in words if len(word) >= 7 and is_palindrome(word)]

print(method_2())

#return word == word[::-1]

#def method_2():
    #return [word for word in word_list if is_anagram(word, "takes")]

#print(word_list)

#print(sorted(woord_a))
#print(sorted(woord_b))

# oefening 4:

def total_lenght(lists):
    total = 0
    for list in lists:
        total += len(list)
    return total

print(total_lenght(words))


