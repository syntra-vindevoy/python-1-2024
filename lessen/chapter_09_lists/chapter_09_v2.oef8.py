opdracht = """
Exercise 8   Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
“I was driving on the highway the other day and I happened to notice my odometer. Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.

“Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.

“One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And you ready for this? One mile later, all 6 were palindromic!

“The question is, what was on the odometer when I first looked?”

Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements. Solution: https://thinkpython.com/code/cartalk2.py.

"""


def get_palindromes_in_range(lower, upper):
    return [i for i in range(lower, upper) if str(i) == str(i)[::-1]]


def get_4_digit_palindromes():
    get_palindromes_in_range(1000, 10000)


def get_all_mileages_containing_4_digit_palindromes():
    solutions = []
    solutions.extend(get_all_mileages_with_4_digit_ending_palindromes())
    solutions.extend(get_all_mileages_with_4_digit_starting_palindromes())
    solutions.extend(get_all_mileages_with_4_digit_mid_palindromes())
    return solutions


def get_all_mileages_with_4_digit_ending_palindromes():
    solutions = []
    palindromes = get_4_digit_palindromes()
    for prefix in range(0, 100):
        for palindrome in palindromes:
            solutions.append(str(prefix) + palindrome)
    return solutions


def get_all_mileages_with_4_digit_starting_palindromes():
    solutions = []
    palindromes = get_4_digit_palindromes()
    for suffix in range(0, 100):
        for palindrome in palindromes:
            solutions.append(palindrome + str(suffix))
    return solutions


def get_all_mileages_with_4_digit_mid_palindromes():
    solutions = []
    palindromes = get_4_digit_palindromes()
    for prefix in range(0, 10):
        for suffix in range(0, 10):
            for palindrome in palindromes:
                solutions.append(str(prefix) + palindrome + str(suffix))
    return solutions


def get_5_digit_palindromes():
    get_palindromes_in_range(10000, 100000)


def get_all_milages_with_5_digit_ending_palindromes():
    solutions = []
    palindromes = get_5_digit_palindromes()
    for prefix in range(0, 10):
        for palindrome in palindromes:
            solutions.append(str(prefix) + palindrome)
    return solutions


def get_all_mileages_with_5_digit_starting_palindromes():
    solutions = []
    palindromes = get_5_digit_palindromes()
    for suffix in range(0, 10):
        for palindrome in palindromes:
            solutions.append(palindrome + str(suffix))
    return solutions


def get_all_mileages_containing_5_digit_palindromes():
    solutions = []
    solutions.extend(get_all_milages_with_5_digit_ending_palindromes())
    solutions.extend(get_all_mileages_with_5_digit_starting_palindromes())


def get_6_digit_palindromes():
    get_palindromes_in_range(100000, 1000000)


def get_odometer():
    """
    check_1
    x = last 4 digits are palindromic

    check2
    x + 1 = last 5 digits are palindromic

    check3
    x + 2 = middle 4 out of 6 digits are palindromic

    check4
    x + 3 = all 6 digits are palindromic

    what was x?
    """

    return odometer
