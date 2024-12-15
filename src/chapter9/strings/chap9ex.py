
from itertools import combinations

def load_words(filename):

    with open(filename) as file:
        return [line.strip() for line in file]


def ex1_word_more_then_20():
    """
    Exercise 1   Write a program that reads words.txt and prints only the words with more than 20 characters
(not counting whitespace).
Exercise 2
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”.
 Since “e” is the most common letter in English, that’s not easy to do.
    :return:
    """
    with open("../words.txt") as file:
        for line in file:
            word = line.strip()
            if len(word) > 20:
                print(word)


def ex2_word_no_e():
    """
    n fact, it is difficult to construct a solitary thought without using that most common symbol. I
    t is slow going at first, but with caution and hours of training you can gradually gain facility.

    All right, I’ll stop now.

    Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

    Write a program that reads words.txt and prints only the words that have no “e”. Compute the percentage of
    words in the list that have no “e”.
    :return:
    """
    with open("../words.txt") as file:
        for line in file:
            word = line.strip()
            if "e" not in word:
                print(word)

def ex3_avoid_letters(word: str, forbidden_letters: str):
    """

    Exercise 3
    Write a function named avoids that takes a word and a string of forbidden letters, and that returns T
    rue if the word doesn’t use any of the forbidden letters.

    Write a program that prompts the user to enter a string of forbidden letters and then prints the number
    of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the
    smallest number of words?

    :param word:
    :param forbidden_letters:
    :return:
    """
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

def ex3_avoid_letters_2(word: str, forbidden_letters: str):
    return word.index(forbidden_letters) == -1

def find_best_forbidden_letters(word_list):
    """
    1. **Loading Words**: `load_words` reads all the words from a file into a list.
    2. **Avoids Function**: `avoids` checks if a word avoids a given set of forbidden letters.
    3. **Finding the Best Combination**:
    - `itertools.combinations` generates all combinations of 5 letters from the alphabet.
    - For each combination, the program counts the number of words excluded using the `avoids` function.
    - The program keeps track of the combination that results in the smallest number of excluded words.
    :param word_list:
    :return:
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    min_excluded = len(word_list)  # Start with the maximum possible value
    best_combination = None

    for combo in combinations(alphabet, 5):
        combo_str = ''.join(combo)
        excluded_count = sum(1 for word in word_list if not avoids(word, combo_str))
        if excluded_count < min_excluded:
            min_excluded = excluded_count
            best_combination = combo_str

    return best_combination, min_excluded



def uses_all(word, required_letters):
    """Check if a word contains all the required letters."""
    for letter in required_letters:
        if letter not in word:
            return False
    return True

def ex4_uses_only(word: str, letters: str):
    """
    Exercise 4
    Write a function named uses_only that takes a word and a string of letters, and that returns True if the
    word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than
    “Hoe alfalfa”?

    :param word:
    :param letters:
    :return:
    """
    for letter in word:
        if letter not in letters:
            return False

def count_words_with_all_vowels(word_list, vowels):
    """Count how many words in the list use all the specified vowels."""
    return sum(1 for word in word_list if uses_all(word, vowels))



def ex5_uses_all(word: str, letters: str):
    """
    Exercise 5
    Write a function named uses_all that takes a word and a string of required letters, and that returns True
    if the word uses all the required letters at least once. How many words are there that use all the vowels aeiou?
    How about aeiouy?
    :param word:
    :param letters:
    :return:
    """
    for letter in letters:
        if letter not in word:
            return False
        else:
            word = word.replace(letter, "", 1)








def avoids(word, forbidden_letters):
    """Check if a word avoids the forbidden letters."""
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True


def is_abecedarian(word)->bool:
    """
    Exercise 6
    Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical
     order (double letters are ok). How many abecedarian words are there?
    :return:
    """

    for i in range(len(word)-1):
        if word[i+1]<word[i]:
            return False
    return True
assert is_abecedarian("hhnnx") == True
assert is_abecedarian("abcdef") == True
assert is_abecedarian("hello") == False
assert is_abecedarian("cherry") == False

def uses_all(word, required_letters):
    """Check if a word contains all the required letters."""
    for letter in required_letters:
        if letter not in word:
            return False
    return True


def check_double_letters(word:str):

    for i in range(len(word)-1):
        if word[i+1]==word[i]:
            return True


assert check_double_letters("hello") == True


def count_double_letters(word:str)->int:
    """
    Exercise 7
    This question is based on a Puzzler that was broadcast on the radio program Car Talk
    (http://www.cartalk.com/content/puzzlers):

    Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t.
    For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’
    that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it
     would work. But there is a word that has three consecutive pairs of letters and to the best of
     my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one.
     What is the word?
    :param word:
    :return:
    """
    count=0
    pointer=0
    while pointer < len(word)-1:
        if word[pointer+1]==word[pointer]:
            pointer+=2
            count+=1
        else:
            pointer+=1
    return count


assert count_double_letters("Mississippi") == 3
assert count_double_letters("committee") == 3

"""

Exercise 9   
“Recently I had a visit with my mom and we realized that the two digits that make up my age 
when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered how often
this has happened over the years but we got sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times so far.
 I also figured out that if we’re lucky it would happen again in a few years, and if we’re really lucky it would
  happen one more time after that. In other words, it would have happened 8 times over

"""
def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.
    """
    return s == s[::-1]


def find_odometer_reading():
    """
    Exercise 8   Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
    “I was driving on the highway the other day and I happened to notice my odometer. Like most odometers,
    it shows six digits, in whole miles only. So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
    “Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic;
    that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my odometer
    could have read 3-1-5-4-4-5.

    “One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6.
    One mile after that, the middle 4 out of 6 numbers were palindromic. And you ready for this?
    One mile later, all 6 were palindromic!

    “The question is, what was on the odometer when I first looked?”
    :return:

    Find the 6-digit odometer number that satisfies the conditions:
    - Last 4 digits are palindromic.
    - After 1 mile, last 5 digits are palindromic.
    - After 2 miles, middle 4 digits are palindromic.
    - After 3 miles, all 6 digits are palindromic.
    """
    for odometer in range(100000, 999997):  # Stop at 999996 since we check 3 miles ahead.
        odometer_str = str(odometer)
        # Condition 1: Last 4 digits are palindromic
        if not is_palindrome(odometer_str[2:]):
            continue

        # Condition 2: Last 5 digits are palindromic (one mile later)
        odometer_1 = str(odometer + 1)
        if not is_palindrome(odometer_1[1:]):
            continue

        # Condition 3: Middle 4 digits are palindromic (two miles later)
        odometer_2 = str(odometer + 2)
        if not is_palindrome(odometer_2[1:5]):
            continue

        # Condition 4: All 6 digits are palindromic (three miles later)
        odometer_3 = str(odometer + 3)
        if not is_palindrome(odometer_3):
            continue

        # If all conditions are met, print the result
        print(f"Odometer reading when you first looked: {odometer_str}")
        break



if __name__ == "__main__":


    #ex1_word_more_then_20()
    #best_comb, num_excluded = find_best_forbidden_letters(load_words("../words.txt"))
    #print(f"The best combination of forbidden letters is: {best_comb}")
    #print(f"It excludes {num_excluded} words.")

    the_word=""
    list_word=load_words("../words.txt")
    most_doubles=0
    for  w in list_word:
        d = count_double_letters(w)
        if d>0:
            if d>most_doubles:
                most_doubles=d
                the_word=w
                print(f"The word with  double letters is: {the_word} - {most_doubles}")

    print(f"The word with most double letters is: {the_word} - {most_doubles}")\

    find_odometer_reading()


