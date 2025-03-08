with open("words.txt", "r") as f:
    words = f.read().split("\n")

def has_no_e(word):
    if word.find("e") == -1: return True

def check_e_in_list():
    a = [word for word in words if has_no_e(word)]
    percentage = len (a) / len(words) * 100
    print (f"There are {percentage:.2f}% of the words without an 'e' \n {a}")

#check_e_in_list()

def cons_dubble (word):
    for letter in word:
        pos = word.find(letter)
        if len(word) - pos < 6 : return False #stopt wanneer er maar 5 letters over blijven
        if letter == word[pos + 1] and word[pos + 2] == word[pos + 3] and word[pos + 4] == word[pos + 5]: return True

def check_cons_dubble():
    a = [word for word in words if cons_dubble(word)]
    print (f"({len(a)} words found: {a}")

#check_cons_dubble()

def uses_none(word, forbidden):
    for letter in forbidden:
        if letter in word: return False
    return True

from itertools import combinations
import string

def generate_unique_combinations():
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    return [''.join(combo) for combo in combinations(alphabet, 5)]

unique_combinations = generate_unique_combinations()
#print(f"Aantal combinaties: {len(unique_combinations)}")


def search_uses_none(forbidden):
    n = 0
    for word in words:
        if uses_none(word, (forbidden)): n += 1
    #print (f"total number of words: {len(words)}, number of forbidden words: {n}")
    return n
#search_uses_none ()

def calculate_used_letters():
    alphabet = string.ascii_lowercase
    letter_counts = {letter: 0 for letter in alphabet}

    for word in words:
        for letter in alphabet:
            if letter in word:
                letter_counts[letter] += 1

    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1])
    return sorted_letters

#most used letters:
#search_uses_none("qjxzw")
#least used letters:
#search_uses_none("esiar")
def search_all_combinations():
    result_max = 0
    result_min = 100000
    combination_max = ""
    combination_min = ""
    count = 0
    for n in unique_combinations:
        count += 1
        result = search_uses_none(n)
        if result > result_max:
            result_max = result
            combination_max = n

        if result < result_min:
            result_min = result
            combination_min = n
        print (f"{count / len(unique_combinations) * 100:.2f}%") if count % 200 == 0 else None
    print (f"{combination_max} = {result_max} and {combination_min} = {result_min}")
#search_all_combinations()

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


def avoids(word, forbidden):
    """Returns True if the word doesn't use any of the forbidden letters."""
    return not any(letter in forbidden for letter in word)



def letter_frequencies(words):
    """Count the frequency of each letter in the words."""
    from collections import Counter
    freq = Counter()
    for word in words:
        freq.update(word)
    return freq

def find_optimal_letters(words, k=5):
    letter_freq = letter_frequencies(words)
    excluded_words = set()
    selected_letters = set()

    for _ in range(k):
        best_letter = None
        best_exclusion = 0

        for letter, freq in letter_freq.items():
            if letter in selected_letters:
                continue

            current_exclusion = sum(1 for word in words if letter in word and word not in excluded_words)

            if current_exclusion > best_exclusion:
                best_letter = letter
                best_exclusion = current_exclusion

        if best_letter:
            selected_letters.add(best_letter)
            excluded_words.update(word for word in words if best_letter in word)

    return selected_letters, len(words) - len(excluded_words)


if __name__ == "__main__":
    forbidden, remaining = find_optimal_letters(words, k=5)
    print(f"Optimal forbidden letters: {''.join(forbidden)}")
    print(f"Number of words that remain: {remaining}")


