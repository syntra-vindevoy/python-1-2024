import random
import time


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

assert cumsum([1, 2 , 3]) == [1, 3, 6]


def middle (list_of_lists):
    """
    Exercise 3
    Write a function called middle that takes a list and returns a new list that contains all
    but the first and last elements. For example:

    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    if len (list_of_lists) < 3:
        return []
    return list_of_lists[1:-1]


assert middle ([1, 2, 3, 4]) == [2, 3]
assert middle ([1, 2, 4]) == [2]
assert middle ([1, 4]) == []


def chop (list_of_lists):
    """
    Exercise 4
    Write a function called chop that takes a list, modifies it by removing the first and last elements,
    and returns None. For example:

    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    if len (list_of_lists) < 3:
        list_of_lists.clear ()
        return
    del list_of_lists[0]
    del list_of_lists[-1]
    return None


assert chop ([1, 2, 3, 4]) is None
list_of_lists = [1, 2, 3, 4]
assert chop (list_of_lists) is None
assert list_of_lists == [2, 3]

list_of_lists = [2, 3, 4]
assert chop (list_of_lists) is None
assert list_of_lists == [3]
list_of_lists = [3, 4]
assert chop (list_of_lists) is None
assert list_of_lists == []


def is_sorted (list_of_lists):
    """
    Exercise 5   Write a function called is_sorted that takes a list as a parameter and returns True
    if the list is sorted in ascending order and False otherwise. For example:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    for i in range (len (list_of_lists) - 1):
        if list_of_lists[i] > list_of_lists[i + 1]:
            return False
    return True


assert is_sorted ([1, 2, 3]) == True
assert is_sorted ([1, 3, 2]) == False


def is_anagram (word1, word2):
    """
    Exercise 6
    Two words are anagrams if you can rearrange the letters from one to spell the other.
    Write a function called is_anagram that takes two strings and returns True if they are anagrams.
    """
    for letter in word2:
        if letter not in word1:
            return False
    return True


def is_anagram2 (str1, str2):
    # Remove any spaces and convert to lowercase
    str1 = str1.replace (" ", "").lower ()
    str2 = str2.replace (" ", "").lower ()

    # Check if sorted characters of both strings are equal
    return sorted (str1) == sorted (str2)


assert is_anagram ("anagram", "nagaram") == True
assert is_anagram ("anagram", "nagarzm") == False
assert is_anagram2 ("anagram", "nagaram") == True
assert is_anagram2 ("anagram", "nagarzm") == False


def has_duplicates (list_of_lists):
    """
    Exercise 7
    Write a function called has_duplicates that takes a list and returns True
    if there is any element that appears more than once. It should not modify the original list.
    """
    for i in list_of_lists:
        if list_of_lists.count (i) > 1:
            return True
    return False


assert has_duplicates ([1, 2, 3, 4]) == False
assert has_duplicates ([1, 2, 3, 4, 1]) == True

"""
Exercise 8
This exercise pertains to the so-called Birthday Paradox, which you can read about at
http://en.wikipedia.org/wiki/Birthday_paradox.
If there are 23 students in your class, what are the chances that two of them have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for matches.
Hint: you can generate random birthdays with the randint function in the random module.

You can download my solution from https://thinkpython.com/code/birthday.py.
"""


def has_duplicates (birthdays):
    return len (birthdays) != len (set (birthdays))


def has_duplicates2 (birthdays):
    for i in range (len (birthdays)):
        for j in range (i + 1, len (birthdays)):
            if birthdays[i] == birthdays[j]:
                return True
    return False


def generate_birthdays (num_people):
    return [random.randint (1, 365) for _ in range (num_people)]


def generate_birthdays2 (num_people):
    birthdays = []
    for _ in range (num_people):
        birthdays.append (random.randint (1, 365))
    return birthdays


def birthday_paradox (num_people, num_simulations):
    duplicate_count = 0
    for _ in range (num_simulations):
        birthdays = generate_birthdays (num_people)
        if has_duplicates (birthdays):
            duplicate_count += 1

    return duplicate_count / num_simulations


num_people = 23
num_simulations = 10000
probability = birthday_paradox (num_people, num_simulations)
print (f"Probability of at least two people sharing a birthday in a group of {num_people} people: {probability:.2f}")

"""
Exercise 9
Write a function that reads the file words.txt and builds a list with one element per word.
 Write two versions of this function, one using the append method and the other using the idiom t = t + [x].
 Which one takes longer to run? Why?

Elapsed time: 0.01 seconds
Elapsed time: 8.34 seconds
"""


def read_words () -> [str]:
    words = []
    with open ("words.txt", encoding='utf-8') as file:
        for line in file:
            word = line.strip ()
            words.append (word)
        return words


start_time = time.perf_counter ()
assert len (read_words ()) == 113783
end_time = time.perf_counter ()

elapsed_time = end_time - start_time
print (f"Elapsed time: {elapsed_time:.2f} seconds")


def read_words2 () -> [str]:
    words = []
    for line in open ('words.txt', encoding='utf-8'):
        word = line.strip ()
        words = words + [word]
    return words


start_time = time.perf_counter ()
assert len (read_words2 ()) == 113783
end_time = time.perf_counter ()

elapsed_time = end_time - start_time
print (f"Elapsed time: {elapsed_time:.2f} seconds")

"""
Exercise 10
To check whether a word is in the word list, you could use the in operator,
but it would be slow because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a bisection search
(also known as binary search), which is similar to what you do when you look a word up in the dictionary
(the book, not the data structure). You start in the middle and check to see whether the word you are looking for
 comes before the word in the middle of the list. If so, you search the first half of the list the same way.
 Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words,
it will take about 17 steps to find the word or conclude that it’s not there.

Write a function called in_bisect that takes a sorted list and a target value and returns True i
f the word is in the list and False if it’s not.

Or you could read the documentation of the bisect module and use that! S
"""
def binary_search(sequence, item):
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

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = 3


"""
Exercise 11
Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
"""


def reverse_pair (word1, word2):
    return word2 == word1[::-1]


def search_for_reverse_pairs (words):
    reverse_pairs = []
    for word1 in words:
        for word2 in words:
            if reverse_pair (word1, word2):
                reverse_pairs.append ((word1, word2))
    return reverse_pairs


assert reverse_pair ("tiger", "gerti") == False
assert reverse_pair ("tiger", "regit") == True
# assert len(search_for_reverse_pairs(read_words())) > 0
"""
Exercise 12
Two words “interlock” if taking alternating letters from each forms a new word. For example,
“shoe” and “cold” interlock to form “schooled”. S
This exercise is inspired by an example S

Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
Can you find any words that are three-way interlocked; that is, every third letter forms a word,
 starting from the first, second or third?

"""
