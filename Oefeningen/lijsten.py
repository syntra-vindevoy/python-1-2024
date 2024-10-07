#Find the biggest value in a given list.

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

biggest = max(the_list)
print(biggest)

biggest=the_list[0]
for f in the_list:
    if f > biggest:
        biggest = f
print(biggest)

#Counting words
whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object oriented programming. This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. For a description of standard objects and modules..."
def count_words(string):
    words = string.split()  # Split the string into words
    return len(words)

print(count_words(whetting_your_appetite))

typeWord={}


def add_type (upper:str):
    if not upper in typeWord:
        typeWord[upper]=1
    else:
        typeWord[upper]+=1


split = whetting_your_appetite.split ()
for w in split:
    if w[0].isupper():
        add_type("upper")
    if w[0] == ".":
        add_type ("point")
    if w[0].isnumeric():
        add_type ("nmbt")

print(typeWord)