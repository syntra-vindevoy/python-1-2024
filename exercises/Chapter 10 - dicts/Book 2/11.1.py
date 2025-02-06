# Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
#  dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
#  check whether a string is in the dictionary.

def read_words():

    with open ('words.txt') as file:
            words = file.read().splitlines()

    words_dicts = {word: None for word in words}

    return words_dicts

def check_word(word: str, words_dicts: dict):
    return True if word in words_dicts else False

def main():
    words_dicts = read_words()
    print(words_dicts)

    print(check_word('apple', words_dicts))

if __name__ == "__main__":
    main()