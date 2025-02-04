import random


def nested_sum(list_of_lists):
    """
    Exercise 1
    Write a function called nested_sum that takes a list of lists of integers and adds up the elements
    from all of the nested lists. For example:

    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    total = 0
    for i in list_of_lists:
        for j in i:
            total += j
    return total


assert nested_sum([[1, 2], [3], [4, 5, 6]]) == 21


def nested_sum_list_comprehension(list_of_lists: [[], ]) -> int:
    """
    Exercise 1 with list comprehension
    Write a function called nested_sum that takes a list of lists of integers and adds up the elements
    from all of the nested lists. For example:

    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """

    return sum([y for row in list_of_lists for y in row])


assert nested_sum_list_comprehension([[1, 2], [3], [4, 5, 6]]) == 21


def cumsum_list_comprehension(list_of_lists):
    """
    Exercise 2
    Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
    that is, a new list where the ith elneement is the sum of the first i+1 elements from the original list. For example:

    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """

    current_sum = 0
    return [current_sum := current_sum + number for number in list_of_lists]


assert cumsum_list_comprehension([1, 2, 3]) == [1, 3, 6]


def cumsum(list_of_lists):
    """
    Exercise 2
    Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
    that is, a new list where the ith elneement is the sum of the first i+1 elements from the original list. For example:

    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    cumulative_sum = []
    current_sum = 0

    for number in list_of_lists:
        current_sum += number
        cumulative_sum.append(current_sum)
    return cumulative_sum


assert cumsum([1, 2, 3]) == [1, 3, 6]


def middle(list_of_lists):
    """
    Exercise 3
    Write a function called middle that takes a list and returns a new list that contains all
    but the first and last elements. For example:

    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    if len(list_of_lists) < 3:
        return []
    return list_of_lists[1:-1]


assert middle([1, 2, 3, 4]) == [2, 3]
assert middle([1, 2, 4]) == [2]
assert middle([1, 4]) == []


def chop(list_of_lists):
    """
    Exercise 4
    Write a function called chop that takes a list, modifies it by removing the first and last elements,
    and returns None. For example:

    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    if len(list_of_lists) < 3:
        list_of_lists.clear()
        return
    del list_of_lists[0]
    del list_of_lists[-1]
    return None


assert chop([1, 2, 3, 4]) is None
list_of_lists = [1, 2, 3, 4]
assert chop(list_of_lists) is None
assert list_of_lists == [2, 3]

list_of_lists = [2, 3, 4]
assert chop(list_of_lists) is None
assert list_of_lists == [3]
list_of_lists = [3, 4]
assert chop(list_of_lists) is None
assert list_of_lists == []


def is_sorted(list_of_lists):
    """
    Exercise 5   Write a function called is_sorted that takes a list as a parameter and returns True
    if the list is sorted in ascending order and False otherwise. For example:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    for i in range(len(list_of_lists) - 1):
        if list_of_lists[i] > list_of_lists[i + 1]:
            return False
    return True


assert is_sorted([1, 2, 3]) == True
assert is_sorted([1, 3, 2]) == False


def is_anagram(word1, word2):
    """
    Exercise 6
    Two words are anagrams if you can rearrange the letters from one to spell the other.
    Write a function called is_anagram that takes two strings and returns True if they are anagrams.
    """
    for letter in word2:
        if letter not in word1:
            return False
    return True


def is_anagram2(str1, str2):
    # Remove any spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)


assert is_anagram("anagram", "nagaram") == True
assert is_anagram("anagram", "nagarzm") == False
assert is_anagram2("anagram", "nagaram") == True
assert is_anagram2("anagram", "nagarzm") == False


def has_duplicates(list_int):
    """
    Exercise 7
    Write a function called has_duplicates that takes a list and returns True
    if there is any element that appears more than once. It should not modify the original list.
    """
    for i in list_int:
        if list_int.count(i) > 1:
            return True
    return False


assert has_duplicates([1, 2, 3, 4]) == False
assert has_duplicates([1, 2, 3, 1]) == True

"""
Exercise 8
This exercise pertains to the so-called Birthday Paradox, which you can read about at
http://en.wikipedia.org/wiki/Birthday_paradox.
If there are 23 students in your class, what are the chances that two of them have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for matches.
Hint: you can generate random birthdays with the randint function in the random module.

You can download my solution from https://thinkpython.com/code/birthday.py.
"""


# beste oplossing
def has_duplicates(birthdays):
    return len(birthdays) != len(set(birthdays))


def has_duplicates2(birthdays):
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return True
    return False


def generate_birthdays(num_people):
    return [random.randint(1, 365) for _ in range(num_people)]


def generate_birthdays2(num_people):
    birthdays = []
    for _ in range(num_people):
        birthdays.append(random.randint(1, 365))
    return birthdays


def birthday_paradox(num_people, num_simulations):
    duplicate_count = 0
    for _ in range(num_simulations):
        birthdays = generate_birthdays(num_people)
        if has_duplicates(birthdays):
            duplicate_count += 1

    return duplicate_count / num_simulations


num_people = 23
num_simulations = 10000
probability = birthday_paradox(num_people, num_simulations)
print(f"Probability of at least two people sharing a birthday in a group of {num_people} people: {probability:.2f}")



def binary_search(sequence, item)->int:
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None





"""
Exercise 11
Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
"""


def reverse_pair(word1, word2):
    return word2 == word1[::-1]


assert reverse_pair("tiger", "gerti") == False
assert reverse_pair("tiger", "regit") == True


def search_for_reverse_pairs(words):
    reverse_pairs = []
    for word1 in words:
        for word2 in words:
            if reverse_pair(word1, word2):
                reverse_pairs.append((word1, word2))
    return reverse_pairs


assert search_for_reverse_pairs(["tiger", "gerti", "regit"]) == [("tiger", "regit"), ("regit", "tiger")]


def search_for_reverse_pairs_lc(words):
    """
    Searches for all reverse pairs in a list of words.

    The function identifies all pairs of words where one is the reverse
    of the other. It uses a list comprehension to achieve this in a concise
    manner.

    :param words: List of words to search through.
    :type words: list of str
    :return: List of tuples containing reverse pairs of words.
    :rtype: list of tuple of (str, str)
    """
    return [(w, sw) for w in words for sw in words if reverse_pair(w, sw)]


assert search_for_reverse_pairs_lc(["tiger", "gerti", "regit"]) == [("tiger", "regit"), ("regit", "tiger")]

"""
Exercise 12
Two words “interlock” if taking alternating letters from each forms a new word. For example,
“shoe” and “cold” interlock to form “schooled”. S
This exercise is inspired by an example S

Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
Can you find any words that are three-way interlocked; that is, every third letter forms a word,
 starting from the first, second or third?

"""


def interlock_pair():
    interlocks = []
    try:
        with open("words.txt") as f:
            lines = f.read().splitlines()
            for line_word in lines:
                word1 = ""
                word2 = ""
                res1 = ""
                res2 = ""
                if len(line_word) > 2:
                    for i in range(len(line_word)):
                        if i % 2 == 0:
                            word1 += line_word[i]
                        else:
                            word2 += line_word[i]
                    if binary_search(lines, word1) is not None:  # Assuming binary_search returns None if not found
                        res1 = word1
                    if binary_search(lines, word2) is not None:
                        res2 = word2
                    if len(res1) > 0 and len(res2) > 0:
                        interlocks.append((line_word, res1, res2))
    except FileNotFoundError:
        print("The file 'words.txt' was not found.")
    except IOError:
        print("An error occurred trying to read 'words.txt'.")

    return interlocks


def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return binary_search(word_list, evens) and binary_search(word_list, odds)


def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not binary_search(word_list, inter):
            return False
    return True


if __name__ == '__main__':
    with open("words.txt") as f:
        word_list = f.read().splitlines()

    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])


    print("Interlock")
    inter = interlock_pair()
    print(inter)
    print(len(inter))

    print("Interlock")


