from operator import truediv

letters = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def find_longest_word(letters):
    # Initialize variables to track the longest valid word
    longest_word = ""
    # Open the file and iterate through each word
    with open('words.txt', 'r') as file:
        for line in file:
            word = line.strip()  # Remove any surrounding whitespace or newlines

            # Check if the word can be formed using the given letters
            if all(word.count(letter) <= letters.count(letter) for letter in word):
                # Update the longest word if the current word is longer
                if len(word) > len(longest_word):
                    longest_word = word

    return longest_word if longest_word else None

print(find_longest_word(letters))

def has_duplicates(word: str) -> bool:
    for letter in word:
        if letter in letters:
            return True
        letters[letter] = True

def has_duplicates2(word: str) -> bool:
    return len(word) > len(set(word))
    #set maakt er een unieke lijst van, dus smijt automatisch de duplicates eruit

with open('words.txt', 'r') as file:
    words = file.read().splitlines()
    longest = 0
    longest_word = ""

    for word in words:
        if len(word) < longest:
            continue
        if has_duplicates(word):
            continue

        if len(word) > longest:
            longest = len(word)
            longest_word = word

with open('words.txt', 'r') as file:
    words = file.read().splitlines()
    words = [word for word in words if len(word) == len(set(word))]
    word_lengths = {len(word): word for word in words}
    print(word_lengths[max(word_lengths.keys())])

with open('words.txt', 'r') as file:
    words = file.read().splitlines()
    # Filter words to ensure each word has unique letters only
    words = [word for word in words if len(word) == len(set(word))]

    # Group words by their lengths
    word_lengths = {}
    for word in words:
        word_lengths.setdefault(len(word), []).append(word)

    # Find the maximum word length
    max_length = max(word_lengths.keys())

    # Print all words with the maximum length
    print(word_lengths[max_length])

#herschrijf zodat dit er meerdere toont als er meerder zijn
