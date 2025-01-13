"""
ex 2
There is a string method called count that is similar to the function in Section 8.7.
 Read the documentation of this method and write an invocation that counts the number of a’s in 'banana'.
"""
import string

word ="battaan path"
occurents_letters={}

for letter in word:
    if not letter.isspace() and letter.isalpha():
     occurents_letters[letter]=word.count(letter)

print(occurents_letters)
print(word.count("a"))

"""
ex 3
Use this idiom to write a one-line version of is_palindrome from Exercise 3.
"""

word="rattar"

rev_word=word[::1]

assert rev_word == word,"Oh no! This assertion failed!"



"""
ex 4
The following functions are all intended to check whether a string contains any lowercase letters, 
but at least some of them are wrong. For each function, describe what the function actually does 
(assuming that the parameter is a string).
"""
#ok
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
#bad
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


#Ok
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
assert any_lowercase3("FFFaFd") == True

#bad always true
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#bad
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


"""
ex 5
A Caesar cypher is a weak form of encryption that involves “rotating” each letter by a fixed number of places. 
To rotate a letter means to shift it through the alphabet, wrapping around to the beginning 
if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.

To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7 is “jolly” and “melon”
 rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the ship computer is called HAL, 
 
 which is IBM rotated by -1.

Write a function called rotate_word that takes a string and an integer as parameters, 
and returns a new string that contains the letters from the original string rotated by the given amount.

You might want to use the built-in function ord, which converts a character to a numeric code, and chr, 
which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical order, so for example:

>>> ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case letters are different.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar cypher with rotation 13.
"""



def rotate_word(word:str, rotate_word_times: int):
    """
    Args:
        word: The string to be rotated.
        rotate_word_times: The number of positions each character in the word will be shifted in the ASCII table.

    Returns:
        A new string where each character from the original word is shifted by the specified number of positions in the ASCII table.
    """
    new_word = ""
    for l in word:
        if l.isalpha():  # Process only alphabetic characters
            if l.islower():  # Lowercase letters
                t = ord(l) + rotate_word_times
                if t > ord('z'):  # Wrap around 'z'
                    t -= 26
                new_word += chr(t)
            elif l.isupper():  # Uppercase letters
                t = ord(l) + rotate_word_times
                if t > ord('Z'):  # Wrap around 'Z'
                    t -= 26
                new_word += chr(t)
        else:
            # Leave non-alphabet characters as is
            new_word += l
    return new_word

rotate_word_times= 13
word = "cheer"
print(rotate_word(word, rotate_word_times))
assert rotate_word(word, rotate_word_times) == "purre"


word = "Varkenskop"
assert rotate_word(word, rotate_word_times)  =="Inexrafxbc"


def caesar(word: str, incr: int) -> str:
    result = ""
    for l in word:
        if l.isupper():
            # Handle uppercase letters
            new_char = string.ascii_uppercase[(string.ascii_uppercase.index(l) + incr) % 26]
        elif l.islower():
            # Handle lowercase letters
            new_char = string.ascii_lowercase[(string.ascii_lowercase.index(l) + incr) % 26]
        else:
            # Leave non-alphabetic characters unchanged
            new_char = l
        result += new_char
    return result


import string

assert caesar("cheer", 13) == "purre"


def caesar2(word, incr: int):
    c = ""
    for letter in word:
        if letter.isupper():
            i = (string.ascii_uppercase.index(letter) + incr) % 26
            c += string.ascii_uppercase[i]
        elif letter.islower():
            i = (string.ascii_lowercase.index(letter) + incr) % 26
            c += string.ascii_lowercase[i]
        else:
            c += letter  # Leave non-alphabetic characters unchanged
    return c

assert caesar2("abc", 1) == "bcd"
assert caesar2("xyz", 1) == "yza"
assert caesar2("ABC", 1) == "BCD"
assert caesar2("XYZ", 1) == "YZA"
assert caesar2("abc", 2) == "cde"
assert caesar2("aBcE", 2) == "cDeG"
assert caesar2("cheer", 13) == "purre"

def caesar4(word, shift):
    csr = ""
    for letter in word:
        offset = (ord("a") - ord("A")) * letter.isupper()
        lower = letter.lower()
        if ord(lower) + shift > ord("z"):
            csr += chr(ord("a") + ord("z") - ord(lower) + shift - offset - 1)
        else:
            csr += chr(ord(lower) + shift - offset)

    return csr


assert caesar4("abc", 1) == "bcd"
assert caesar4("xyz", 1) == "yza"
assert caesar4("ABC", 1) == "BCD"
assert caesar4("XYZ", 1) == "YZA"
assert caesar4("abc", 2) == "cde"
assert caesar4("aBcE", 2) == "cDeG"


