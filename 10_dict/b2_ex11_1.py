# Write a function that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn’t matter what the values are. Then you can use the "in" operator as a fast way to
# check whether a string is in the dictionary.

def is_in_word_list(word:str) -> bool:
    with open("words.txt", "r") as f:
        word_list = f.read().splitlines()

    words = {word for word in word_list}

    return word in words

print(is_in_word_list("stone"))
print(is_in_word_list("thomas"))