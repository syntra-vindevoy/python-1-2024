# Exercise 11.5. Two words are “rotate pairs” if you can rotate one of them and get the other (see
# rotate_word in Exercise 8.5). Write a program that reads a wordlist and finds all the rotate pairs.

python


def rotate_word(word, shift):
    """Rotates each lowercase letter in 'word' by 'shift' positions, wrapping from 'a' to 'z'."""
    result = []
    for char in word:
        if char.isalpha() and char.islower():
            # Shift within 'a' - 'z'> ASCII range
            new_char_code = ((ord(char) - ord('a') + shift) % 26) + ord('a')
            result.append(chr(new_char_code))
        else:
            result.append(char)
    return "".join(result)


def find_rotate_pairs_dict(words):
    """
    Returns a dictionary where each key is a word from 'words' that has
    one or more rotate matches, and the value is a list of (rotated_word, shift) pairs.
    """
    # Convert the list to a set for faster lookup
    words_set = set(words)
    rotate_pairs = {}

    for word in words_set:
        for shift in range(1, 26):
            rotated = rotate_word(word, shift)
            if rotated in words_set:
                # Collect the pairing in the dictionary
                rotate_pairs.setdefault(word, []).append((rotated, shift))

    return rotate_pairs


# Example usage:
if __name__ == "__main__":
    # 1. Read all words from the wordlist
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        wordlist = [line.strip().lower() for line in file if line.strip()]

    # 2. Find rotate pairs using a dictionary
    rotate_dict = find_rotate_pairs_dict(wordlist)

    # 3. Print results
    for original_word, pairs in rotate_dict.items():
        for (rotated_word, shift) in pairs:
            print(f"'{original_word}' rotates by {shift} -> '{rotated_word}'")
