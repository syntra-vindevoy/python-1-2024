def main ():
    t = 'l', 'u', 'p', 'i', 'n'
    print (type (t))
    t = tuple ("masker from zorro")
    for i in t:
        print (i)
    print (sorted (t))
    print (tuple (reversed (t)))
    email = 'monty@python.org'
    username, domain = email.split ('@')
    print (username, domain)
    print (domain)

    d = {'one': 1, 'two': 2}

    for item in d.items ():
        key, value = item
        print (key, '->', value)

    for key, value in d.items ():
        print (key, '->', value)

    a, b = 1, 2
    a, b = b, a

    print (a, b)

    print (divmod (7, 3))

    def min_max (t):
        return min (t), max (t)

    print (min_max ([2, 4, 1, 3]))

    def mean (*args):
        return sum (args) / len (args)

    print (mean (1, 2, 3, 10))

    def trimmed_mean (*args):
        low, high = min_max (args)
        trimmed = list (args)
        trimmed.remove (low)
        trimmed.remove (high)
        return mean (*trimmed)

    print (trimmed_mean (1, 2, 3, 10,))

    scores1 = [1, 2, 4, 5, 1, 5, 2]
    scores2 = [5, 5, 2, 2, 5, 2, 3]
    for pair in zip (scores1, scores2):
        print (pair)

    wins = 0
    for team1, team2 in zip (scores1, scores2):
        if team1 > team2:
            wins += 1

    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = range (len (letters))
    letter_map = dict (zip (letters, numbers))

    def value_counts (string):
        counter = {}
        for letter in string:
            if letter not in counter:
                counter[letter] = 1
            else:
                counter[letter] += 1
        return counter

    counter = value_counts ('banana')
    print (counter)
    items = counter.items ()

    def second_element (t):
        return t[1]

    sorted_items = sorted (items, key=second_element)
    sorted_items
    print (sorted_items)
    print (max (items, key=second_element))

    print (wins)

    def invert_dict (d):
        new = {}
        for key, value in d.items ():
            if value not in new:
                new[value] = [key]
            else:
                new[value].append (key)
        return new

    print (invert_dict (counter))

def f (*args):
    for arg in args:
        print (arg)

def toto(**kwargs):
    for key, value in kwargs.items ():
        print (key, value)
    print (kwargs)

def home(request,*args,**kwargs):
    print(request)
    print(args)
    print(kwargs)

def version_part(part):
   if part.isdigit():
       return int(part),0
   else:
       return 0,part

def normalize_version(version):
    if isinstance(version, int):
        return (version,)  # Single integer becomes a one-element tuple
    return tuple(int(part) for part in version.split('.') if part.isdigit())

def normalize_version2(version):
    if isinstance(version, int):
        return (version,)  # Single integer becomes a one-element tuple
   # return tuple(int(part) for part in version.split('.') if part.isdigit())
    return tuple(version_part(part) for part in version.split('.'))

def is_version_less_than(current_version, new_version):

    current_version_tuple = normalize_version(current_version)
    new_version_tuple = normalize_version(new_version)
    return current_version_tuple < new_version_tuple

def is_version_less_than2(current_version, new_version):

    current_version_tuple = normalize_version2(current_version)
    new_version_tuple = normalize_version2(new_version)
    return current_version_tuple < new_version_tuple

# Tests
assert is_version_less_than(1, 2) == True
assert is_version_less_than(2, 1) == False
assert is_version_less_than("1.0", "1.1") == True
assert is_version_less_than("3.0", "11.0") == True
assert is_version_less_than("1.0.0", "1.1.0") == True
assert is_version_less_than(5, "6.0") == True
assert is_version_less_than("7.5", 8) == True
assert is_version_less_than("7.a", "8.b") == True
assert is_version_less_than("7.0_alpha", "8.0") == True

assert is_version_less_than2("7.5", "8.0") == True
assert is_version_less_than2("7.a", "8.b") == True
assert is_version_less_than2("7.0_alpha", "8.0") == True

import re
import re
def is_version_less_than3(current_version, new_version):
    """
    Compares two version strings or integers and determines if current_version is less than new_version.
    Handles mixed types and returns False for invalid or non-numeric inputs.

    Args:
        current_version: The current version (string, int, or similar format).
        new_version: The new version (string, int, or similar format).

    Returns:
        bool: True if current_version is less than new_version, False otherwise.
    """

    def parse_version(version):
        """Converts a version into a list of numeric components. Returns None for invalid formats."""
        if isinstance(version, int):  # Convert integer to list
            return [version]
        if isinstance(version, str):  # Split string into parts and check they are numeric
            parts = version.split('.')
            if all(part.isdigit() for part in parts):  # Ensure all parts are numeric
                return [int(part) for part in parts]
            return None
        return None

    current_parts = parse_version(current_version)
    new_parts = parse_version(new_version)

    if current_parts is None or new_parts is None:
        return False  # Invalid versions should return False

    # Pad shorter version with zeros
    max_length = max(len(current_parts), len(new_parts))
    current_parts.extend([0] * (max_length - len(current_parts)))
    new_parts.extend([0] * (max_length - len(new_parts)))

    return current_parts < new_parts


# Running assertions
assert is_version_less_than3(1, 2) == True
assert is_version_less_than3(2, 1) == False
assert is_version_less_than3("1.0", "1.1") == True
assert is_version_less_than3("3.0", "11.0") == True
assert is_version_less_than3("1.0.0", "1.1.0") == True
assert is_version_less_than3(5, "6.0") == True
assert is_version_less_than3("7.5", 8) == True
assert is_version_less_than3("7.a", "8.b") == False  # Non-numeric, invalid
assert is_version_less_than3("7.0_alpha", "8.0") == False  # Non-numeric, invalid


"All assertions passed successfully."

if __name__ == '__main__':
    main ()
    toto (one=1, two=2)
    feels = 'good'
    f (feels, 'nice', 'to', 'see', 'you')
    home(1,2,3,4,5,6,7,8,9,10,r="fdgfdgd")

    print((1,2,3) == ('a','b','c'))
