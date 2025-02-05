def caesar2(word, incr: int):
    c = ""
    for letter in word:
        if letter.isupper():
            i = (string.ascii_uppercase.index(letter) + incr) % 26
            c += string.ascii_uppercase[i]
        elif letter.islower():
            i = (string.ascii_lowercase.index(letter) + incr) % 26
            c += string.ascii_lowercase[i]
        else:
            c += letter  # Leave non-alphabetic characters unchanged
    return c

assert caesar2("abc", 1) == "bcd"
assert caesar2("xyz", 1) == "yza"
assert caesar2("ABC", 1) == "BCD"
assert caesar2("XYZ", 1) == "YZA"
assert caesar2("abc", 2) == "cde"
assert caesar2("aBcE", 2) == "cDeG"
assert caesar2("cheer", 13) == "purre"
vowels = ["a", "e", "i", "o", "u"]
cities = ["Oudenaarde", "Opwijk", "Drongen", "Evergem", "Sint-Niklaas", "Gent", "Lede", "Dendermonde", "Wetteren",
          "Aalter", "Ursel"]
#must reverse
for t in cities[::-1]:
    if t in vowels:
        cities.remove(t)

steden = [stad for stad in cities if stad[0].lower() not in "aeuioy"]
print(steden)


def has_duplicates(birthdays):
    return len(birthdays) != len(set(birthdays))


def binary_search(sequence, item)->int:
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None




def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return binary_search(word_list, evens) and binary_search(word_list, odds)


def split_on_upper_and_space_re(s):
    # Use a regex to split on uppercase letters or spaces
    return re.findall(r'[A-Z][a-z0-9]*|[a-z0-9]+', s)

vowels = "aeiou"
import string

ascii_kit = string.ascii_lowercase

input_string = "hello world from world 123 of horror "
string_lower = input_string.lower().split(" ")
for word in string_lower:

    for count in range(len(word) - 1):
        if word[count] in vowels and word[count + 1] in vowels:
            print(word)

from itertools import combinations

# Sample text
text = """
Python is a versatile programming language used for data science, AI, and web development.

It is easy to learn, has a large community, and offers a wide variety of libraries and frameworks.

Many developers choose Python for its simplicity and powerful features.
"""

# Split the text into paragraphs
paragraphs = text.strip().split("\n\n")

# Keywords to search
keywords = ["Python", "AI", "web"]

# Generate keyword combinations (e.g., pairs or all subsets)
comb_length = 2  # You can adjust the combination length (2 for pairs)
keyword_combinations = list(combinations(keywords, comb_length))

# Dictionary to store matching paragraphs
matching_paragraphs = {}

# Search each paragraph
for i, paragraph in enumerate(paragraphs, start=1):
    found_keywords = [kw for kw in keywords if kw.lower() in paragraph.lower()]
    if found_keywords:
        # Store in the dictionary if at least one keyword is found
        matching_paragraphs[f"Paragraph {i}"] = {
            "text": paragraph.strip(),
            "found_keywords": found_keywords,
        }

# Output the matching paragraphs
print("Matching Paragraphs:")
for key, value in matching_paragraphs.items():
    print(f"{key}:\n  Text: {value['text']}\n  Found Keywords: {', '.join(value['found_keywords'])}\n")

def cumsum_list_comprehension(list_of_lists):
    """
    Exercise 2
    Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
    that is, a new list where the ith elneement is the sum of the first i+1 elements from the original list. For example:

    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """

    current_sum = 0
    return [current_sum := current_sum + number for number in list_of_lists]



def invert_dict(dict_words: dict):
    inverse = {}
    for key in dict_words:
        val = dict_words[key]
        inverse.setdefault(val, []).append(key)
    return inverse


assert invert_dict(dict(a=1, b=2, c=3, z=1)) == {1: ['a', 'z'], 2: ['b'], 3: ['c']}

def middle(list_of_lists):
    """
    Exercise 3
    Write a function called middle that takes a list and returns a new list that contains all
    but the first and last elements. For example:

    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    if len(list_of_lists) < 3:
        return []
    return list_of_lists[1:-1]


def find_repeats2(counter:dict):
    return [x for x,y in counter.items() if y> 1]

"""
Write a function called word_distance that takes two words with the same length and returns the number of places where the two words differ.

Hint: Use zip to loop through the corresponding letters of the words.
"""
def word_distance(word1, word2):
    """
    Calculates the number of differing positions between two strings
    of equal lengths. This is also known as the Hamming distance.

    Args:
        word1: The first string to compare.
        word2: The second string to compare.

    Returns:
        The integer Hamming distance between the two strings.
    """
    total_distance = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            total_distance += 1
    return total_distance

assert word_distance("cheer", "chaar") == 2


def avoids(word, forbidden):
    return any(ch in forbidden.lower() for ch in word.lower())


fin = open('van_studenten/words.txt')

for word in fin:
    if avoids(word, 'lobs') == True:
        print(word)

import re


# Define a function to find words with exactly 2 vowels
def find_words_with_two_vowels(text):
    # Regex to match words with exactly two vowels
    pattern = r'\b\w*[aeiouAEIOU]\w*[aeiouAEIOU]\w*\b'
    words = re.findall(pattern, text)

    # Filter out words with more than 2 vowels
    result = [word for word in words if sum(ch in "aeiouAEIOU" for ch in word) == 2]
    return result


# Sample text
text = """
Python is a versatile programming language with many features.
It excels in AI, web development, and scientific computing.
"""

# Find words with exactly 2 vowels
words_with_two_vowels = find_words_with_two_vowels(text)
print("Words with exactly 2 vowels:", words_with_two_vowels)


def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict


def merge_dictionaries1(dict1, dict2):
    merged_dict = dict1 | dict2  # Merge with the second dictionary overwriting common keys
    return merged_dict


assert merge_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, chars = zip(*pairs)

print(list(nums))  # Output: [1, 2, 3]
print(list(chars))  # Output: ['a', 'b', 'c']

words = ["apple", "banana", "cherry", "banana", "date"]

for i in range(len(words) - 1, -1, -1):  # Iterate backwards
    if words[i] == "banana":
        del words[i]  # Remove "banana"

print(words)  # Output: ['apple', 'cherry', 'date']

# Example CSV file content:
# name,age,job,city,country,email,phone,company,experience,skills
# Alice,30,Engineer,New York,USA,alice@example.com,1234567890,TechCorp,5,Python;Java
# Bob,25,Designer,Los Angeles,USA,bob@example.com,0987654321,DesignInc,3,Photoshop;Illustrator
# Charlie,35,Manager,Chicago,USA,charlie@example.com,1122334455,BizGroup,10,Leadership;Finance

# Open and read the CSV file
with open("cv.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Extract headers and data
headers = lines[0].strip().split(",")
cv_data = [dict(zip(headers, line.strip().split(","))) for line in lines[1:]]

# Print the list of dictionaries
print(cv_data)
