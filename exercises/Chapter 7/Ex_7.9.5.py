def check_word(word: str, available: str, required: str) -> bool:
    """Check whether a word is acceptable.

    #>>> check_word('color', 'ACDLORT', 'R')
    True
    #>>> check_word('ratatat', 'ACDLORT', 'R')
    True
    #>>> check_word('rat', 'ACDLORT', 'R')
    False
    #>>> check_word('told', 'ACDLORT', 'R')
    False
    #>>> check_word('bee', 'ACDLORT', 'R')
    False
    """

    if len(word) < 4:
        return False

    if not all(letter in available.lower() for letter in word.lower()):
        return False

    if required.lower() not in word.lower():
        return False

    return True


def word_score(word, available):
    """Compute the score for an acceptable word.

    #>>> word_score('card', 'ACDLORT')
    1
    #>>> word_score('color', 'ACDLORT')
    5
    #>>> word_score('cartload', 'ACDLORT')
    15
    """

    word = word.lower()
    available = available.lower()

    if len(word) == 4:
        score = 1
    elif len(word) > 4:
        score = len(word)
        if all(letter in word for letter in available):
            score += 7
    else:
        score = 0

    return score


def main():
    print(check_word('color', 'ACDLORT', 'R'))

    assert check_word('ratatat', 'ACDLORT', 'R') == True
    assert check_word('rat', 'ACDLORT', 'R') == False
    assert check_word('told', 'ACDLORT', 'R') == False
    assert check_word('bee', 'ACDLORT', 'R') == False


    print(word_score('color', 'ACDLORT'))

    assert word_score('color', 'ACDLORT') == 5
    assert word_score('cartload', 'ACDLORT') == 15
    assert word_score('cart', 'ACDLORT') == 1

if __name__ == '__main__':
    main()
