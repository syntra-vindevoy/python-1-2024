"""
common one-syllable, five-letter word 

When you remove the first letter, the remaining letters form a homophone of the original word, that is a word that sounds exactly the same. 

Replace the first letter, that is, put it back and remove the second letter and the result is yet another homophone of the original word. And the question is, what’s the word?

Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter word, ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first letter, I am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the rack on that buck! It must have been a nine-pointer!’ It’s a perfect homophone. If you put the ‘w’ back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is a real word, it’s just not a homophone of the other two words.

But there is, however, at least one word that Dan and we know of, which will yield two homophones if you remove either of the first two letters to make two, new four-letter words. The question is, what’s the word?

"""

from module import read_dictionary
import os

file_path = os.path.join(os.path.dirname(__file__), "words.txt")
with open(file_path, "r") as file:
    word_list = file.read().splitlines()

file_path = os.path.join(os.path.dirname(__file__), "c06d.txt")
with open(file_path, "r") as file:
    soundslike_dictionary = read_dictionary(file_path)


def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word if char in vowels)


five_letter_word_list = [
    word for word in word_list if len(word) == 5 and count_vowels(word) == 1
]

four_letter_word_list = [word for word in word_list if len(word) == 4]


for word in five_letter_word_list:
    word_1 = word[1:]
    word_2 = word[0] + word[2:]
    if word_1 in word_list and word_2 in four_letter_word_list:
        if soundslike_dictionary.get(word) == soundslike_dictionary.get(
            word_1
        ) and soundslike_dictionary.get(word) == soundslike_dictionary.get(word_2):
            print(f"{word} -> {word_1} -> {word_2}")
            print(
                f"{soundslike_dictionary.get(word)} -> {soundslike_dictionary.get(word_1)} -> {soundslike_dictionary.get(word_2)}"
            )

# oplossing is scent cent sent, andere woorden worden ook weergegeven omdat woorduitspraak ontbreekt
