

"""
Write a function called most_frequent_letters that takes a string and prints the letters in decreasing order of frequency.

To get the items in decreasing order, you can use reversed along with sorted or you can pass reverse=True as a keyword parameter to sorted.
"""

def most_frequent_letters(value, reverse=True):
    # Remove non-letter characters and normalize to lowercase
    letters = [char.lower() for char in value if char.isalpha()]
    # Count the frequency of each letter
    frequency = {}
    for char in letters:
        frequency[char] = frequency.get(char, 0) + 1
    # Sort by frequency (and alphabetically for ties)
    sorted_letters = sorted(frequency.keys(), key=lambda x: (-frequency[x], x) if reverse else (frequency[x], x))
    # Return the sorted letters as a single string
    return "".join(sorted_letters)




"""
In a previous exercise, we tested whether two strings are anagrams by sorting the letters in both words and checking 
whether the sorted letters are the same. Now let’s make the problem a little more challenging.

We’ll write a program that takes a list of words and prints all the sets of words that are anagrams. Here is an example
 of what the output might look like:
"""
def find_anagrams(word_list):
    """Finds and groups anagrams from the given list of words."""
    anagram_dict = {}  # Dictionary to store groups of anagrams

    for word in word_list:
        # Sort the word to create a key
        sorted_word = ''.join(sorted(word))

        # Use the sorted word as a key to group anagrams
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    # Return the groups of anagrams as lists
    return [group for group in anagram_dict.values() if len(group) > 1]


# Example input
input_words = [
    'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',
    'retainers', 'ternaries',
    'generating', 'greatening',
    'resmelts', 'smelters', 'termless'
]

# Find anagrams
result = find_anagrams(input_words)

# Print the anagram groups
for group in result:
    print(group)




"""
Write a function called word_distance that takes two words with the same length and returns the number of places where the two words differ.

Hint: Use zip to loop through the corresponding letters of the words.
"""
def word_distance(word1, word2):
    total_distance = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            total_distance += 1
    return total_distance

assert word_distance("cheer", "chaar") == 2

"""
“Metathesis” is the transposition of letters in a word. Two words form a “metathesis pair” if you can transform one 
into the other by swapping two letters, like converse and conserve. Write a program that finds all of the metathesis
 pairs in the word list.
"""


def find_metathesis_pairs(word_list):
    def is_metathesis_pair(word1, word2):
        return word_distance(word1, word2) == 2

    # Group words into anagrams
    anagrams = find_anagrams(word_list)

    # Find metathesis pairs within each group of anagrams
    metathesis_pairs = []
    for group in anagrams:
        for i, word1 in enumerate(group):
            for word2 in group[i + 1:]:
                if is_metathesis_pair(word1, word2):
                    metathesis_pairs.append((word1, word2))

    return metathesis_pairs


# Example input
input_words = [
    'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',
    'retainers', 'ternaries',
    'generating', 'greatening',
    'resmelts', 'smelters', 'termless'
]

# Find metathesis pairs
pairs = find_metathesis_pairs(input_words)

# Print the metathesis pairs
for pair in pairs:
    print(pair)


if __name__ == "__main__":
    print(most_frequent_letters("abracadabra",reverse=True))



