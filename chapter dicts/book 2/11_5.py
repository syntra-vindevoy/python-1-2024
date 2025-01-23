from string import ascii_lowercase


def rotate_word(word, rotation):
    word = word.lower()
    alphabet = ascii_lowercase * 2
    #alphabet_list = list(alphabet)
    new_word = ""
    for letter in word:
        i = (alphabet.index(letter))
        new_word += alphabet[i+rotation]
    return new_word

def find_pairs():
    with open("words.txt", "r") as f:
        words_dict = {word: 1 for word in f.read().splitlines()}
        pairs_list = []
    for word in words_dict:
        new_word = rotate_word(word, 2)
        if new_word in words_dict: pairs_list.append((word, new_word))

    return len(pairs_list), pairs_list

print (find_pairs())






