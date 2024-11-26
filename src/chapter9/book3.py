"""
Write a function called reverse_sentence that takes as an argument a string that contains any number
of words separated by spaces. It should return a new string that contains the same words in reverse order.
 For example, if the argument is “Reverse this sentence”, the result should be “Sentence this reverse”.

Hint: You can use the capitalize methods to capitalize the first word and convert the other words to lowercase.

"""


def reverse_sentence(sentence):
    """
    Args:
        sentence: A string input sentence to be reversed.

    Returns:
        A new string where the words in the input sentence are reversed, made lowercase,
        and capitalized only at the beginning.
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


# IP spliten

def split_ip(ip: str):
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
