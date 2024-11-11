def is_palindrome(word):
    """Check if a word is a palindrome."""
    return word[::-1] == word


def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters."""
    return not any(letter in forbidden for letter in word)


def main():
    title = 'monty python and the holy grail'
    t = [word.capitalize() for word in title.split()]

    out = ' '.join(t)
    print(out)
    word_list = [line.strip() for line in open('../resources/words.txt')]
    for word in word_list:
        print(word, end=" ")

    palindromes = [word for word in word_list if is_palindrome(word)]
    print(palindromes)

    print(list(filter(is_palindrome, word_list)))

    print(sum(1 / 2 ** n for n in range(10)))

    print(any(letter == 't' for letter in 'monty'))


if __name__ == '__main__':
    main()
