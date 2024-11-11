from collections import Counter


def main():
    counter = Counter('banana')
    print(counter)
    print(is_anagram('banana', 'nana'))

    counter2 = Counter('bans')
    counter + counter2
    print(counter)


def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)


if __name__ == '__main__':
    main()
