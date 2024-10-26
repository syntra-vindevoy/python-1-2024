def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

    #>>> uses_none('banana', 'xyz')
    True
    #>>> uses_none('apple', 'efg')
    False
    """
    for letter in word.lower():
        if letter.lower() in forbidden.lower():
            return False
    return True

def maim():
    print(uses_none('apple', 'abc'))

    assert uses_none('banana', 'xyz') == True
    assert uses_none('apple', 'efg') == False
    assert uses_none('apple', 'abc') == False
    assert uses_none('banana', 'aBc') == False

if __name__ == '__main__':
    maim()
