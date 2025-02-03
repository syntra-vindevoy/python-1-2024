"""
Write a function called word_distance that takes two words with the same length and returns the number of places where the two words differ.

Hint: Use zip to loop through the corresponding letters of the words.

Here's an outline of the function with doctests you can use to check your function.


def word_distance(word1, word2):
    Computes the number of places where two word differ.

    >>> word_distance("hello", "hxllo")
    1
    >>> word_distance("ample", "apply")
    2
    >>> word_distance("kitten", "mutton")
    3

    return None

"""


def word_distance(word1, word2):
    zip_difference = 0
    for pair in zip(word1, word2):
        if pair[0] != pair[1]:
            zip_difference += 1
    return zip_difference


assert word_distance("hello", "hxllo")
assert word_distance("ample", "apply")
assert word_distance("kitten", "mutton")
