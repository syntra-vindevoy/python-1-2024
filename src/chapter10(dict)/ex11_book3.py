"""
11.11.3. Exercise
In this chapter we made a dictionary that maps from each letter to its index in the alphabet.

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))
For example, the index of 'a' is 0.

letter_map['a']
0
To go in the other direction, we can use list indexing. For example, the letter at index 1 is 'b'.

letters[1]
'b'
We can use letter_map and letters to encode and decode words using a Caesar cipher.

A Caesar cipher is a weak form of encryption that involves shifting each letter by a fixed number of places in the
 alphabet, wrapping around to the beginning if necessary. For example, 'a' shifted by 2 is 'c' and 'z' shifted by 1 is
 'a'.

Write a function called shift_word that takes as parameters a string and an integer, and returns a new string that
contains the letters from the string shifted by the given number of places.

To test your function, confirm that “cheer” shifted by 7 is “jolly” and “melon” shifted by 16 is “cubed”.

Hints: Use the modulus operator to wrap around from 'z' back to 'a'. Loop through the letters of the word,
shift each one, and append the result to a list of letters. Then use join to concatenate the letters into a string.
"""


def letter_map () -> dict:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = range (len (letters))
    return dict (zip (letters, numbers))


LETTERS = letter_map ()


def shift_word (word: str, shift: int) -> str:
    new_word = ""
    for letter in word:
        letter_index = LETTERS[letter]
        new_letter_index = (letter_index + shift) % len (LETTERS)
        new_letter = list (LETTERS.keys ())[new_letter_index]
        new_word += new_letter
    return new_word


assert shift_word ("cheer", 7) == "jolly"
assert shift_word ("melon", 16) == "cubed"

"""
11.11.4. Exercise
Write a function called most_frequent_letters that takes a string and prints the letters in decreasing order of frequency.

To get the items in decreasing order, you can use reversed along with sorted or you can pass reverse=True as a 
keyword parameter to sorted."""


def most_frequent_letters (word: str) -> dict[str, int]:
    letters_count = {}
    for letter in word:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    return dict (sorted (letters_count.items (), key=lambda item: item[1], reverse=True))


assert most_frequent_letters ("cheer") == {'e': 2, 'r': 1, 'c': 1, 'h': 1}

"""
11.11.5. Exercise
In a previous exercise, we tested whether two strings are anagrams by sorting the letters in both words and checking 
whether the sorted letters are the same. Now let’s make the problem a little more challenging.

We’ll write a program that takes a list of words and prints all the sets of words that are anagrams. Here is an example
 of what the output might look like:

['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: For each word in the word list, sort the letters and join them back into a string. Make a dictionary that maps
 from this sorted string to a list of words that are anagrams of it.

"""


def anagram_sets (word_list: list[str]) -> {}:
    anagram_sets = {}
    for word in word_list:
        sorted_word = "".join (sorted (word))
        if sorted_word in anagram_sets:
            anagram_sets[sorted_word] = anagram_sets[sorted_word].append (word)
        else:
            anagram_sets[sorted_word] = [sorted_word]
    return anagram_sets


assert anagram_sets (["cheer", "huekr"]) == {'ceehr': ['ceehr'], 'ehkru': ['ehkru']}
assert anagram_sets (["cheer", "huekr", "melon"]) == {'ceehr': ['ceehr'], 'ehkru': ['ehkru'], 'elmno': ['elmno']}

"""
11.11.6. Exercise
Write a function called word_distance that takes two words with the same length and returns the number of places where 
the two words differ.

Hint: Use zip to loop through the corresponding letters of the words.
"""


def word_distance (word1: str, word2: str) -> int:
    total_distance = 0
    for w1, w2 in zip (word1, word2):
        if w1 != w2:
            total_distance += 1
    return total_distance


assert word_distance ("cheer", "chaar") == 2

"""
11.11.7. Exercise
“Metathesis” is the transposition of letters in a word. Two words form a “metathesis pair” if you can transform one 
into the other by swapping two letters, like converse and conserve. Write a program that
 finds all of the metathesis pairs in the word list.

Hint: The words in a metathesis pair must be anagrams of each other.
"""


def metathesis_pairs (word_list: list[str]) -> list[tuple[str, str]]:
    return_list = []
    for word1 in word_list:
        for word2 in word_list:
            if word1 != word2 and word_distance (word1, word2) == 2 and return_list.count ((word2, word1)) == 0:
                return_list.append ((word1, word2))
    return return_list


assert metathesis_pairs (["cheer", "chaar"]) == [('cheer', "chaar")]
assert metathesis_pairs (["cheer", "huekr", "chaar"]) == [('cheer', 'chaar')]
