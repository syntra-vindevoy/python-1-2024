# _00_b3_summary.py

# Chapter 8: Strings Summary (Think Python Book)

# 1. Introduction to Strings
# Strings are sequences of characters and are immutable in Python.

# Defining a string
example_string = "Hello, World"
# Attempt to modify the string (This will raise an error)
# example_string[0] = 'h'
# Strings are immutable, which means their content cannot be modified.

# 2. String Operations

# Concatenation (+)
concat_example = "Hello" + " " + "World"
# Repetition (*)
repeat_example = "Echo! " * 3
# Indexing ([])
index_example = concat_example[1]  # Accessing the second character
# print(concat_example, repeat_example, index_example)

# 3. Traversal with Loops

# Counting vowels in a string
vowels = "aeiou"
input_string = "Think Python is fun!"
vowel_count = 0
for char in input_string:
    if char.lower() in vowels:
        vowel_count += 1
# print(f"Number of vowels in '{input_string}': {vowel_count}")

# 4. String Methods

# Common string methods and their examples
method_example = "  Python Strings "
lower_example = method_example.lower()  # Convert to lowercase
upper_example = method_example.upper()  # Convert to uppercase
find_example = method_example.find("Strings")  # Find substring position
strip_example = method_example.strip()  # Remove surrounding whitespace
replace_example = method_example.replace("Strings", "Methods")

# 5. Search and Count

# Using 'in' operator and count method
search_string = "Python programming is fun. Python is powerful."
is_in = "fun" in search_string  # Check if "fun" is in the string
count_example = search_string.count("Python")  # Count occurrences of "Python"

# 6. String Comparisons

# Comparing strings lexicographically
string1 = "alpha"
string2 = "beta"
comparison_result = string1 < string2  # True because "alpha" comes before "beta"

# 7. The 'in' Operator

# Checking substring existence
sentence = "The quick brown fox jumps over the lazy dog."
is_word_in_sentence = "fox" in sentence  # True if "fox" is in the string

# 8. Immutability of Strings

# Operations on strings create new strings
original = "immutable"
modified = original + " strings"
# print(original)  # 'immutable'
# print(modified)  # 'immutable strings'

# 9. String Slicing and Advanced Techniques

# Slicing a string
slicing_example = "Think Python"
substring = slicing_example[6:12]  # Extract "Python"
reversed_string = slicing_example[::-1]  # Reverse the string

# 10. Case Study - Small Exercises

# Extracting palindromes
def is_palindrome(word):
    return word == word[::-1]

example_word = "radar"
is_palindrome_result = is_palindrome(example_word)  # True

# Analyzing word frequency
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

example_sentence = "This is a test. This is only a test."
frequency_result = word_frequency(example_sentence)

# Uncomment the print statements below for testing the examples.
print(concat_example, repeat_example, index_example)
print(f"Number of vowels in '{input_string}': {vowel_count}")
print(lower_example, upper_example, find_example, strip_example, replace_example)
print(is_in, count_example)
print(comparison_result)
print(is_word_in_sentence)
print(original, modified)
print(substring, reversed_string)
print(is_palindrome_result)
print(frequency_result)