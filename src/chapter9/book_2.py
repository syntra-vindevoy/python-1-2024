"""
Exercise 1
Write a function called nested_sum that takes a list of lists of integers and adds up the elements
from all of the nested lists. For example:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""
def nested_sum(list_of_lists):
    total = 0
    for i in list_of_lists:
        for j in i:
            total += j
    return total

assert nested_sum([[1, 2], [3], [4, 5, 6]]) == 21


"""
Exercise 2
Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
that is, a new list where the ith elneement is the sum of the first i+1 elements from the original list. For example:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""
def cumsum(list_of_lists):
    cumulative_sum = []
    current_sum = 0

    for number in list_of_lists:
        current_sum += number
        cumulative_sum.append(current_sum)
    return cumulative_sum

assert cumsum([1, 2 , 3]) == [1, 3, 6]

"""

Exercise 3
Write a function called middle that takes a list and returns a new list that contains all
but the first and last elements. For example:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
Exercise 4
Write a function called chop that takes a list, modifies it by removing the first and last elements,
and returns None. For example:

>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
Exercise 5   Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
Exercise 6
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.

Exercise 7
Write a function called has_duplicates that takes a list and returns True i
f there is any element that appears more than once. It should not modify the original list.

Exercise 8
This exercise pertains to the so-called Birthday Paradox, which you can read about at
http://en.wikipedia.org/wiki/Birthday_paradox.


If there are 23 students in your class, what are the chances that two of them have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for matches.
Hint: you can generate random birthdays with the randint function in the random module.

You can download my solution from https://thinkpython.com/code/birthday.py.

Exercise 9
Write a function that reads the file words.txt and builds a list with one element per word.
 Write two versions of this function, one using the append method and the other using the idiom t = t + [x].
 Which one takes longer to run? Why?

Solution: https://thinkpython.com/code/wordlist.py.

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

Exercise 11
Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.

Exercise 12
Two words “interlock” if taking alternating letters from each forms a new word. For example,
“shoe” and “cold” interlock to form “schooled”. S
This exercise is inspired by an example S

Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
Can you find any words that are three-way interlocked; that is, every third letter forms a word,
 starting from the first, second or third?

"""