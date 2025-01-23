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


def binary_search(sequence, item) -> (int, int):
    begin_index = 0
    end_index = len(sequence) - 1
    counter = 0
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        counter += 1
        if midpoint_value == item:
            return midpoint, counter

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None


def check_word_in_list(word: str):
    with open("words.txt") as f:
        lines = f.read().splitlines()
        return binary_search(lines, word)


if __name__ == '__main__':
    print(check_word_in_list("tiger"))
