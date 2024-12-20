string = "banana"

print(string.count("a"))


# Example string
string = "banana"

# Every second character
print(string[0:6:2])  # Output: 'bnn'

# Every third character
print(string[0:6:3])  # Output: 'ba'

# Reverse the string
print(string[::-1])  # Output: 'ananab'

# Reverse string with a step of 2
print(string[::-2])  # Output: 'aaa'

def palindrome(string):
    return string == string[::-1]

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s): # c is a string and had to be a counter
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s): # C
    for c in s:
        flag = c.islower()
        return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True

print(any_lowercase1("Abba"))
print(any_lowercase2("Abba"))
print(any_lowercase3("Abba"))
print(any_lowercase4("Abba"))
print(any_lowercase5("Abba"))

#zoek alle woorden met een e uit words
#zoek alle woorden meest en minst uit words
#zoek de letter combo die zorgt voor de meeste woorden
#neem een combo van 5 verschillend letters en zoek de combo die in het
# minst aantal woorden voorkomt.

import string


def ceaser(word, inc: int):
    c=""
    caps = string.ascii_uppercase + string.ascii_uppercase
    for letter in word:
        if letter.isupper():
           # i = (string.ascii_uppercase.index(letter)+inc) % 26
           # c += string.ascii_uppercase[i]
           i = caps.index(letter) + inc
           c += caps[i]

        elif letter.islower():
            c += string.ascii_lowercase[(string.ascii_lowercase.index(letter) + inc) % 26]

        else:
            c += letter

        return c
print(ceaser("Hello", 3))

