'''
Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
'''

def has_all_chars_in_word(char_combination: str, word: str):
    return all(char in word for char in char_combination)