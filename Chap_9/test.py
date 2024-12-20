from datetime import datetime


def avoids(word, forbidden_letters):
    """
    Check if the word contains any of the forbidden letters.

    :param word: The word to check.
    :param forbidden_letters: A string of forbidden letters.
    :return: True if the word does not contain any forbidden letters, False otherwise.
    """
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True


def count_avoided_words(words, forbidden_letters):
    """
    Count the number of words that do not contain any forbidden letters.

    :param words: A list of words.
    :param forbidden_letters: A string of forbidden letters.
    :return: The number of words that don't contain forbidden letters.
    """
    count = 0
    for word in words:
        if avoids(word, forbidden_letters):
            count += 1
    return count


def generate_combinations(letters, combination_length):
    """
    Generate combinations of a given length from the input letters.

    :param letters: A string of all possible letters.
    :param combination_length: The length of each combination.
    :yield: Each combination as a tuple.
    """
    if combination_length == 0:
        yield ()
    elif len(letters) < combination_length:
        return
    else:
        first = letters[0]
        for subcomb in generate_combinations(letters[1:], combination_length - 1):
            yield (first,) + subcomb
        for subcomb in generate_combinations(letters[1:], combination_length):
            yield subcomb


def calculate_letter_frequencies(words):
    """
    Calculate the frequency of each letter in the list of words.

    :param words: A list of words.
    :return: A dictionary containing letters as keys and their frequencies as values.
    """
    letter_counts = {}
    for word in words:
        unique_letters = set(word)  # Count each letter only once per word
        for letter in unique_letters:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts


def find_min_excluded_letters(words, all_letters):
    """
    Find a combination of 5 forbidden letters that excludes the smallest number of words.

    :param words: A list of words to analyze.
    :param all_letters: A string of all possible letters.
    :return: A tuple containing the optimal set of 5 letters and the number of excluded words.
    """
    # Calculate letter frequencies and sort letters by frequency (descending order)
    letter_counts = calculate_letter_frequencies(words)
    sorted_letters = sorted(all_letters, key=lambda x: -letter_counts.get(x, 0))

    min_excluded = len(words)
    best_combination = None

    # Generate combinations of 5 letters from the most frequent ones
    for combo in generate_combinations(sorted_letters, 5):
        excluded_count = len(words) - count_avoided_words(words, combo)
        if excluded_count < min_excluded:
            min_excluded = excluded_count
            best_combination = combo

    return best_combination, min_excluded


if __name__ == "__main__":
    start = datetime.now()
    # Read a list of words from a file (assumes "words.txt" contains one word per line)
    try:
        with open("words.txt", "r") as file:
            words_list = file.read().splitlines()
            total_words = len(words_list)
            print(f"Total words: {total_words}")
    except FileNotFoundError:
        print("Error: 'words.txt' file not found.")
        exit()

    # Ask the user for forbidden letters
    forbidden_input = "qwzxj"

    # Count and display the number of words that avoid the forbidden letters
    num_avoided = count_avoided_words(words_list, forbidden_input)
    end = datetime.now()
    print(f"Number of words that don't contain '{forbidden_input}': {num_avoided}")
    print(f"Time taken: {end - start}")
    # Find and display the combination of 5 letters that excludes the smallest number of words
    all_letters = "abcdefghijklmnopqrstuvwxyz"  # Assuming English alphabet
    best_letters, excluded_count = find_min_excluded_letters(words_list, all_letters)
    print(f"Best combination of 5 letters to exclude the smallest number of words: {''.join(best_letters)}")
    print(f"Number of excluded words: {excluded_count}")

