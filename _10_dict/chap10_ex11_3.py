import string

def has_duplicates1(word: string) -> bool:
    letters = {}

    for letter in word:
        if letter in letters:
            return True
        else:
            letters[letter] = True
    return False

def has_duplicates(word: string) -> bool:
    return len(word) != len(set(word))      #Set makes a unique list of your word

with open("words.txt", "r") as f:
    words = f.read().splitlines()

longest_word = ""
longest = 0

for word in words:
    if len(word) < longest:
        continue

    if has_duplicates(word):
        continue

    if len(word) > longest:
        longest_word = word
        longest = len(word)

print(longest_word, longest)



with open("words.txt", "r") as f:
    word_list = f.read().splitlines()

    words = [word for word in word_list if len(word) == len(set(word))]  #Put all unique words in list
    #print(words)
    word_lengths = {len(word):word for word in words}       #Make dict with key = length of word and value = word, word will be overwritten with the next one of the same length
    print(word_lengths)
    print(word_lengths[sorted(word_lengths, reverse=True)[0]])
    print(word_lengths[max(word_lengths.keys())])

#3rd Option
#First get the longest word
#find one without duplicates in the longest
#if not found descend