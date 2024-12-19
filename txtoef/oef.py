#Geef de lettercombinatie die het meest aantal woorden heeft
#zoek een combinatie van 5 verschillende letters die in het minst aantal woorden voorkomt
#hier kan je iets voor vinden in de collectons klasse
#loopen van a tot v, van b tot w, van c tot x, van de tot y en van e tot z
#loop over u woorden en kijk of u karkater erin voorkomt, komt het er niet in voor gaat u counter omhoog
#doel is dit zo snel mogelijk te laten lopen (minder dan een minuut)
import string

# Read words from a text file
with open("words.txt", "r") as file:
    words = [line.strip() for line in file]

# Function to generate combinations of letters without itertools
def generate_combinations(letters, r):
    if r == 0:
        return [""]
    if not letters:
        return []
    with_first = [letters[0] + combo for combo in generate_combinations(letters[1:], r - 1)]
    without_first = generate_combinations(letters[1:], r)
    return with_first + without_first

# Initialize counters
combo_counter = {}

# Loop through each word and generate combinations dynamically
for word in words:
    for combo in generate_combinations(string.ascii_lowercase, 5):  # Generate all 5-letter combinations
        if not any(letter in word for letter in combo):  # Check if none of the letters are in the word
            combo = ''.join(sorted(combo))  # Sort letters to ensure consistent keys
            if combo in combo_counter:
                combo_counter[combo] += 1
            else:
                combo_counter[combo] = 1

# Find the combination with the most and least words
most_common = max(combo_counter.items(), key=lambda x: x[1])
least_common = min(combo_counter.items(), key=lambda x: x[1])

print("Most common combination:", most_common)
print("Least common combination:", least_common)
