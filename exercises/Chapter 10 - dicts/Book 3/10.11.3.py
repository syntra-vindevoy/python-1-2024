# def has_duplicates(word: str) -> bool:
#
#     letter = {}
#
#     for letters in word:
#         if letters in letter:
#             return True
#
#         letters[letter] = True
#
def has_duplicates_2(word: str) -> bool:
    return len(word) != len(set(word))

#1st option

with open ('words.txt') as file:
    words = file.read().splitlines()
    longest = 0
    longest_word = ''

    for word in words:
        if len(word) < longest:
            continue

        if has_duplicates_2(word):
            continue

        if len(word) > longest:
            longest = len(word)
            longest_word = word

    print (longest_word, longest)

#2nd option

with open('words.txt') as file:
    words = file.read().splitlines()
    words = [word for word in words if len(word) == len(set(word))]
    word_length = {len(word): word for word in words}
    print(word_length[max(word_length.keys())])

#3rd option
#words in een dict steken
