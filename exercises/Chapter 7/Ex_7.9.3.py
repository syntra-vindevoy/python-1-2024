def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    #>>> uses_only('banana', 'ban')
    True
    #>>> uses_only('apple', 'apl')
    False
    """

    for letter in word:
        if letter not in available:
            return False
    return True

def main():
    print(uses_only('banana', 'ban'))

    assert uses_only('apple', 'apl') == False
    assert uses_only('banana', 'ban') == True
    assert uses_only('boot', 'bto') == True

if __name__ == '__main__':
    main()