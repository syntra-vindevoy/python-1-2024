"""
9.2  Exercises
There are solutions to these exercises in the next section. You should at least attempt each one before you
read the solutions.

Exercise 1   Write a program that reads words.txt and prints only the words with more than 20 characters
(not counting whitespace).
Exercise 2
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”.
 Since “e” is the most common letter in English, that’s not easy to do.

In fact, it is difficult to construct a solitary thought without using that most common symbol. I
t is slow going at first, but with caution and hours of training you can gradually gain facility.

All right, I’ll stop now.

Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

Write a program that reads words.txt and prints only the words that have no “e”. Compute the percentage of
words in the list that have no “e”.

Exercise 3
Write a function named avoids that takes a word and a string of forbidden letters, and that returns T
rue if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and then prints the number
of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the
smallest number of words?

Exercise 4
Write a function named uses_only that takes a word and a string of letters, and that returns True if the
word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than
“Hoe alfalfa”?

Exercise 5
Write a function named uses_all that takes a word and a string of required letters, and that returns True
if the word uses all the required letters at least once. How many words are there that use all the vowels aeiou?
How about aeiouy?

Exercise 6
Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical
 order (double letters are ok). How many abecedarian words are there?


 Exercise 7
This question is based on a Puzzler that was broadcast on the radio program Car Talk
(http://www.cartalk.com/content/puzzlers):

Give me a word with three consecutive double letters. I’ll give you a couple of words that almost qualify, but don’t.
For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’
that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it
 would work. But there is a word that has three consecutive pairs of letters and to the best of
 my knowledge this may be the only word. Of course there are probably 500 more but I can only think of one.
 What is the word?
Write a program to find it. Solution: https://thinkpython.com/code/cartalk1.py.

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

Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
these requirements. Solution: https://thinkpython.com/code/cartalk2.py.

Exercise 9   Here’s another Car Talk Puzzler you can solve with a search (http://www.cartalk.com/content/puzzlers):
“Recently I had a visit with my mom and we realized that the two digits that make up my a
ge when reversed resulted in her age. For example, if she’s 73, I’m 37. We wondered how often
this has happened over the years but we got sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times so far.
 I also figured out that if we’re lucky it would happen again in a few years, and if we’re really lucky it would
  happen one more time after that. In other words, it would have happened 8 times over

"""

def ex1_word_more_then_20():
    with open("../words.txt") as file:
        for line in file:
            word = line.strip()
            if len(word) > 20:
                print(word)


def ex2_word_no_e():
    with open("../words.txt") as file:
        for line in file:
            word = line.strip()
            if "e" not in word:
                print(word)

def ex3_avoid_letters(word: str, forbidden_letters: str):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

def ex3_avoid_letters_2(word: str, forbidden_letters: str):
    return word.index(forbidden_letters) == -1

def ex4_uses_only(word: str, letters: str):
    for letter in word:
        if letter not in letters:
            return False


assert ex3_avoid_letters("cat", "a") == True
assert ex3_avoid_letters_2("cat", "a") == True






if __name__ == "__main__":
    ex1_word_more_then_20()