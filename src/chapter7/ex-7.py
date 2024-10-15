def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

        >>> uses_none('banana', 'xyz')
        True
        >>> uses_none('apple', 'efg')
        False
        """
    for letter in word:
        if letter in forbidden:
            return False
    return True

# use only
def uses_only(word, available):
    """Checks whether a word uses only the available letters.

       >>> uses_only('banana', 'ban')
       True
       >>> uses_only('apple', 'apl')
       False
       """
    for letter in word:
        if not letter in available:
            return False
    return True


def uses_all(word,required):
    """Checks whether a word uses all required letters.

       >>> uses_all('banana', 'ban')
       True
       >>> uses_all('apple', 'api')
       False
       """
    for letter in word:
        if not letter in required:
            return False
    return True

def check_words(word,available,required):

    """Check whether a word is acceptable.

       >>> check_word('color', 'ACDLORT', 'R')
       True
       >>> check_word('ratatat', 'ACDLORT', 'R')
       True
       >>> check_word('rat', 'ACDLORT', 'R')
       False
       >>> check_word('told', 'ACDLORT', 'R')
       False
       >>> check_word('bee', 'ACDLORT', 'R')
       False
       """
    selected=0
    if not required.lower() in word.lower():
        return False
    for letter in word:
        if letter in available.lower():
            selected+=1
    if selected < 4:
        return False
    return True


def check_word(word, available_letters, required_letter):
    """
    Check if a word is acceptable in the Spelling Bee puzzle.

    Parameters:
    word (str): The word to check.
    available_letters (str): A string of seven available letters.
    required_letter (str): The single required letter that must be in the word.

    Returns:
    bool: True if the word is acceptable, False otherwise.

    Doctests:
    >>> check_word("color", "ACDLORT", "R")
    True
    >>> check_word("told", "ACDLORT", "R")
    False
    >>> check_word("rat", "ACDLORT", "R")
    False
    >>> check_word("ratatat", "ACDLORT", "R")
    True
    >>> check_word("lard", "ACDLORT", "R")
    True
    >>> check_word("ladd", "ACDLORT", "R")
    False
    """
    # Rule 1: Word must be at least 4 letters long
    if len(word) < 4:
        return False

    # Rule 2: Word must contain the required letter
    if required_letter.upper() not in word.upper():
        return False

    # Rule 3: All letters in the word must be from the available letters
    available_set = set(available_letters.upper())
    for letter in word.upper():
        if letter not in available_set:
            return False

    return True


def word_score(word, available_letters):
    """
        Calculate the score of an acceptable word in the Spelling Bee puzzle.

        Parameters:
        word (str): The word to score.
        available_letters (str): A string of available letters.


        Returns:
        int: The score of the word, or 0 if the word is not acceptable.

        Doctests:
        >>> word_score('card', 'ACDLORT')
        4
        >>> word_score('color', 'ACDLORT')
        5
        >>> word_score('cartload', 'ACDLORT')
        15
        """
    required_letter="R"
    # Ensure the word is at least 4 letters long
    if len (word) < 4:
        return 0

    # Ensure all letters in the word are in the available letters list
    word_upper = word.upper ()
    available_letters_set = set (available_letters)
    for letter in word_upper:
        if letter not in available_letters_set:
            return 0

    # Ensure the word contains the required letter
    if required_letter.upper () not in word_upper:
        return 0

    # Calculate the basic score (1 point per letter)
    score = len (word)

    # Add bonus if the word uses all available letters at least once
    if all (letter in word_upper for letter in available_letters):
        score += 7

    return score


def uses_none2(word, forbidden):
    """Checks whether a word avoids forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('', 'abc')
    True
    """
    return not uses_any(word, forbidden)

def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False



def main():
    print(uses_none("banana", "xyz"))
    print(uses_none("apple", "efs"))

    print(uses_none2("banana", "xyz"))
    print(uses_none2("apple", "efs"))

    print(uses_only("banana", "ban"))
    print(uses_only("apple", "apl"))

    print(uses_all("banana", "ban"))
    print(uses_all("apple", "api"))

    print(check_word("color", "ACDLORT", "R"))
    print(check_word("rat", "ACDLORT", "R"))
    print(check_word("ratatat", "ACDLORT", "R"))

    print(check_words("color", "ACDLORT", "R"))
    print(check_words("rat", "ACDLORT", "R"))
    print(check_words("ratatat", "ACDLORT", "R"))

    print(word_score("card", "ACDLORT"))
    print(word_score("color", "ACDLORT"))
    print(word_score("cartload", "ACDLORT"))

    available = 'ACDLORT'
    required = 'R'
    total = 0

    file_object = open('words.txt')
    for line in file_object:
        word = line.strip()
        if check_word(word, available, required):
            score = word_score(word, available)
            total = total + score
            print(word, score)

    print("Total score", total)

if __name__ == '__main__':
    main()