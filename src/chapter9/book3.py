"""
Write a function called reverse_sentence that takes as an argument a string that contains any number
of words separated by spaces. It should return a new string that contains the same words in reverse order.
 For example, if the argument is “Reverse this sentence”, the result should be “Sentence this reverse”.

Hint: You can use the capitalize methods to capitalize the first word and convert the other words to lowercase.

"""


def reverse_sentence(sentence):
    """Reverse the words in a string and capitalize the first.

    >>> reverse_sentence('Reverse this sentence')
    'Sentence this reverse'

    >>> reverse_sentence('Python')
    'Python'

    >>> reverse_sentence('')
    ''

    >>> reverse_sentence('One for all and all for one')
    'One for all and all for one'
    """
    lower_sentence = " ".join(sentence.lower().split()[::-1])
    lower_sentence = lower_sentence.capitalize()
    return lower_sentence


assert reverse_sentence("Reverse this sentence") == "Sentence this reverse"
assert reverse_sentence("This is a test") == "Test a is this"
try:
    assert reverse_sentence("This is a test with multiple words") == "Multiple words with a is this is"
    raise AssertionError
except AssertionError:
    pass


# IP splitsen

def split_ip(ip: str):
    """
    Splits an IP address into its constituent parts.

    This function takes an IPv4 address in string format and splits it into
    four octets. The provided IP address must be in the format of x.x.x.x.

    :param ip: The IP address to split, provided as a string.
    :type ip: str
    :return: A tuple containing four parts of the IP address.
    :rtype: tuple

    :raises ValueError: If the IP address format is invalid.
    """
    if ip.count(".") != 3:
        raise ValueError("Invalid IP address. Must be in the format of x.x.x.x")
    else:
        G, H, K, L = ip.split(".")
        return G, H, K, L


assert split_ip("192.168.1.1") == ("192", "168", "1", "1")

# maak een lijst met steden = oudenaarde, drongen, sint-niklaas, gent, lede, dendermonde,wetteren
# die steden verwijderd die beginnen met een klinker. Maar geen nieuwe lijst maken.

vowels = ["a", "e", "i", "o", "u"]
cities = ["Oudenaarde", "Opwijk", "Drongen", "Evergem", "Sint-Niklaas", "Gent", "Lede", "Dendermonde", "Wetteren",
          "Aalter", "Ursel"]
print(cities)
print([city for city in cities if not city.lower().startswith(tuple(vowels))])
cities = ["Oudenaarde", "Opwijk", "Drongen", "Evergem", "Sint-Niklaas", "Gent", "Lede", "Dendermonde", "Wetteren",
          "Aalter", "Ursel"]

for i in range(len(cities) - 1, -1, -1):
    t = cities[i]
    if t[0].lower() in vowels:
        cities.remove(t)
print(cities)

cities = ["Oudenaarde", "Opwijk", "Drongen", "Evergem", "Sint-Niklaas", "Gent", "Lede", "Dendermonde", "Wetteren",
          "Aalter", "Ursel"]
#must reverse
for t in cities[::-1]:
    if t in vowels:
        cities.remove(t)

steden = [stad for stad in cities if stad[0].lower() not in "aeuioy"]
print(steden)


def reverse_word(word: str) -> str:
    """
    Reverses the given word.

    Takes a string input and returns its reverse.

    :param word: The word to be reversed
    :type word: str
    :return: The reversed word
    :rtype: str
    """
    return ''.join(reversed(word))


def is_palindrome(word: str) -> bool:
    """
    Checks if a given word is a palindrome.

    A palindrome is a word that reads the same backward as forward.
    This function returns True if the input word is a palindrome,
    otherwise, it returns False.

    :param str word: The word to be checked.
    :return: True if the word is a palindrome, False otherwise.
    :rtype: bool
    """
    return word == word[::-1]


assert is_palindrome("bob") == True
assert is_palindrome("alice") == False
assert is_palindrome("a") == True
assert is_palindrome("") == True


def is_voodoo(word: str):
    return word[:1] == word[1:][::-1]


def is_anagram(str1, str2):
    # Remove any spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)


def read_words_lc() -> [str]:
    words = []
    with open("words.txt", encoding='utf-8') as file:
        return [word.strip() for word in file]


"""
anagrams
"""


def search_datagram_simple():
    anagrams = []
    words = read_words_lc()
    #for v in words:
    #    if is_anagram(v.lower(),"takes"):
    #       anagrams.append((v,"takes"))
    return [t for t in words if is_anagram(t.lower(), "takes")]


def search_anagram():
    anagrams = []
    words = read_words_lc()
    for v in words:
        for word2 in words:
            if is_anagram(v, word2) and v is not word2:
                anagrams.append((v, word2))
    return anagrams


def search_anagram_lc():
    words = read_words_lc()
    res = [(w1, w1) for w1 in words for w2 in words if w1 != w2 and sorted(w1) == sorted(w2)]
    return res

#15.5
def total_length(words: []) -> int:
    return sum([len(x) for x in words])

def read_words() -> []:
    with open("words.txt", encoding='utf-8') as f:
        return f.read().splitlines()


assert total_length(read_words()) == 902728



if __name__ == '__main__':
    pass
# data = search_anagram_lc()
# print(data)
