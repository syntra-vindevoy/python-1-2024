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
