
def has_duplicates(*words):
    dict_words_count = {}
    for word in words:
        dict_words_count[word] = dict_words_count.get(word, 0) + 1
        if dict_words_count[word] > 1:
            return True
    return False
print (has_duplicates( "b", "f", "a", "b"))
