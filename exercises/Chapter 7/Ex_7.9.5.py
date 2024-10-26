def check_word(word, available, required):
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
    return False

def main():
    print(check_word('color', 'ACDLORT', 'R'))

if __name__ == '__main__':
    main()
