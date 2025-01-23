def dict_words():
    with open ("words.txt", "r") as f:
        words_dict = { word: 1 for word in f.read().splitlines()}

        return words_dict
#print (dict_words())

def is_in(word):
    return word in dict_words()

#print (is_in("chocolate"))

