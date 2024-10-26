def uses_all(word, required):
    """Checks whether a word uses all required letters.

    #>>> uses_all('banana', 'ban')
    True
    #>>> uses_all('apple', 'api')
    False
    """
    for letter in required:
        if letter not in word:
            return False
    else:
        return True

def main():
    print(uses_all('banana', 'ban'))

    assert uses_all('apple', 'api') == False
    assert uses_all('banana', 'ban') == True
    assert uses_all('boot', 'bts') == False
    assert uses_all('boot', 'bto') == True

if __name__ == '__main__':
    main()