import random
import re

"""
8.12.2. Exercise
See if you can write a function that does the same thing as the shell command !head. It should take as arguments the
name of a file to read, the number of lines to read, and the name of the file to write the lines into.
 If the third parameter is None, it should display the lines rather than write them to a file.

Consider asking a virtual assistant for help, but if you do, tell it not to use a with statement or a try statement.
"""


def head (filename, lines=10, out=None):
    """
    :param filename: The name of the file to read.
    :param lines: The maximum number of lines to read from the file. Default is 10.
    :param out: Optional. The name of the output file to write the lines to. If not provided, the lines are printed to the standard output.
    :return: None
    """
    with open (filename, encoding='utf-8', errors='replace') as file:
        if out is None:
            for i, line in enumerate (file):
                if i >= lines:
                    break
                print (line, end='')
        else:
            with open (out, 'w', encoding='utf-8', errors='replace') as out_file:
                for i, line in enumerate (file):
                    if i >= lines:
                        break
                    out_file.write (line)


def head_new (input_filename, num_lines=10, output_filename=None):
    """

    :param input_filename:
    :param num_lines:
    :param output_filename:
    """

    def read_lines (file, max_lines):
        for line_number, line_content in enumerate (file):
            if line_number >= max_lines:
                break
            yield line_content

    def write_lines (file, lines):
        for line in lines:
            file.write (line)

    with open (input_filename, encoding='utf-8', errors='replace') as input_file:
        lines = read_lines (input_file, num_lines)

        if output_filename is None:
            for line in lines:
                print (line, end='')
        else:
            with open (output_filename, 'w', encoding='utf-8', errors='replace') as output_file:
                write_lines (output_file, lines)


"""
“Wordle” is an online word game where the objective is to guess a five-letter word in six or fewer attempts.
 Each attempt has to be recognized as a word, not including proper nouns.
  After each attempt, you get information about which of the letters you guessed appear in the target word,
   and which ones are in the correct position.

For example, suppose the target word is MOWER and you guess TRIED. 
You would learn that E is in the word and in the correct position, 
R is in the word but not in the correct position, and T, I, and D are not in the word.

As a different example, suppose you have guessed the words SPADE and CLERK, 
and you’ve learned that E is in the word, but not in either of those positions, 
and none of the other letters appear in the word. Of the words in the word list,
 how many could be the target word? Write a function called check_word that takes a five-letter word and
  checks whether it could be the target word, given these guesses.
"""


def game_wordle ():
    word_list = ["tedstr", "master", "breuki"]
    word_to_guest = random.choice (word_list)
    print (word_to_guest)
    arr = ['*'] * len (word_to_guest)
    max_attempts = 6
    word_lenght = 6
    attempts = 1
    correct = 0
    while attempts <= max_attempts and correct < word_lenght:
        print (f"attempt:{attempts}")
        word = input ("Enter a word: ")
        if len (word) != word_lenght:
            print ("Bad word")
        else:
            correct = check_word (arr, correct, word, word_to_guest)
            print (arr)
        attempts += 1

    if correct == max_attempts:
        print ("You win")
    else:
        print ("You lose")


def check_word (arr, correct, word, word_to_guest):
    for i in range (0, len (word)):
        if word[i] == word_to_guest[i] and arr[i] == '*':
            arr[i] = word[i]
            correct += 1
    return correct


"""
8.12.5. Exercise
The Count of Monte Cristo is a novel by Alexandre Dumas that is considered a classic.
 Nevertheless, in the introduction of an English translation of the book,
  the writer Umberto Eco confesses that he found the book to be “one of the most badly written novels of all time”.

In particular, he says it is “shameless in its repetition of the same adjective,
” and mentions in particular the number of times “its characters either shudder or turn pale.”

To see whether his objection is valid, let’s count the number number of lines that contain the word pale in any form, 
including pale, pales, paled, and paleness, as well as the related word pallor. 
Use a single regular expression that matches all of these words and no others.
"""


def monte_cristo_count_pale ():
    occurrences = 0
    pattern = re.compile (r'\b(pale|pales|paled|paleness|pallor)\b', re.IGNORECASE)
    for line in open ('pg1184.txt', encoding='utf-8', errors='replace'):
        occurrences += count_words (line, pattern)

    print (occurrences)


def count_words (line, pattern):
    return len (re.findall (pattern, line))


if __name__ == '__main__':
    head ('pg345.txt')
    head ('pg345.txt', 5)
    head ('pg345.txt', 5, "out.txt")
    # game_wordle()
    monte_cristo_count_pale ()
