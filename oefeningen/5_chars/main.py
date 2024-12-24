
'''
Exercise 9.3. 

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. 

Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
'''

from time import time
from functions import *
from constants import *

from icecream import ic

@timing
def main():
    word_list = {"auto",'bus','step'}
    chars = 'abc'
    word_combinations = get_char_combination_set(chars,2) 
    print(word_combinations)


if __name__ == '__main__':
    main()






