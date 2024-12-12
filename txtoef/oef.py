#Geef de lettercombinatie die het meest aantal woorden heeft
#zoek een combinatie van 5 verschillende letters die in het minst aantal woorden voorkomt
#hier kan je iets voor vinden in de collectons klasse
#loopen van a tot v, van b tot w, van c tot x, van de tot y en van e tot z
#loop over u woorden en kijk of u karkater erin voorkomt, komt het er niet in voor gaat u counter omhoog
#doel is dit zo snel mogelijk te laten lopen (minder dan een minuut)
from collections import Counter
import itertools

# Read words from a text file
with open("words.txt", "r") as file:
    words = [line.strip() for line in file]

# Filter words with fewer than 5 unique letters
words = [word for word in words if len(set(word)) >= 5]

# Initialize counters
combo_counter = Counter()

# Loop through each word and generate combinations dynamically
for word in words:
    unique_letters = set(word)  # Get unique letters in the word
    word_combinations = itertools.combinations(unique_letters, 5)  # Generate combinations from the word's letters
    for combo in word_combinations:
        combo_counter[''.join(combo)] += 1

# Find the combination with the most and least words
most_common = combo_counter.most_common(1)[0]  # Most common combination
least_common = min(combo_counter.items(), key=lambda x: x[1])  # Least common combination

print("Most common combination:", most_common)
print("Least common combination:", least_common)
