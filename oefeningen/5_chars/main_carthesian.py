


from functions import *

@timing
def main_1():
    from collections import defaultdict

    def word_to_char_set(word):
        return set(word)

    def find_least_occurring_matches(list1, list2):
        comb_list_of_sets = [word_to_char_set(word) for word in comb_list]
        word_list_of_sets = [word_to_char_set(word) for word in word_list]
        match_counts = defaultdict(int)

        for word1, char_set1 in zip(comb_list, comb_list_of_sets):
            for word2, char_set2 in zip(word_list, word_list_of_sets):
                if char_set1 & char_set2:  # Check for common characters
                    match_counts[word1] += 1

        # Find the word with the least matches
        least_occurring_word = min(match_counts, key=match_counts.get)
        least_occurrences = match_counts[least_occurring_word]

        return least_occurring_word, least_occurrences

    # Example usage
    word_list = get_wordlist_from_file("words.txt")[0:]
    char_list = string.ascii_lowercase
    comb_list = get_char_combination_set(char_list, 1)  # Replace with your 60,000 words


    least_word, occurrences = find_least_occurring_matches(comb_list, word_list)
    print(f"The least occurring word is '{least_word}' with {occurrences} matches.")


if __name__ == "__main__":
    main_1() 