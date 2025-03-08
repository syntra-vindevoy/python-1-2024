"""What is the longest English word, that remains a valid English word, as you remove its
letters one at a time?
Now, letters can be removed from either end, or the middle, but you can’t rearrange any
of the letters. Every time you drop a letter, you wind up with another English word. If
you do that, you’re eventually going to wind up with one letter and that too is going
to be an English word—one that’s found in the dictionary. I want to know what’s the
longest word and how many letters does it have?
I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
you take a letter off, one from the interior of the word, take the r away, and we’re left
with the word spite, then we take the e off the end, we’re left with spit, we take the s off,
we’re left with pit, it, and I.
Write a program to find all words that can be reduced in this way, and then find the longest one.
This exercise is a little more challenging than most, so here are some suggestions:
1. You might want to write a function that takes a word and computes a list of all the words that
can be formed by removing one letter. These are the “children” of the word.
2. Recursively, a word is reducible if any of its children are reducible. As a base case, you can
consider the empty string reducible.
3. The wordlist I provided, words.txt, doesn’t contain single letter words. So you might want
to add “I”, “a”, and the empty string.
4. To improve the performance of your program, you might want to memoize the words that are
known to be reducible"""
from pathlib import Path

words_dir = Path("C:/Syntra")
file_name = "words.txt"
file = words_dir / file_name

def reduce_words(file):
    with open (file, 'r') as f:
        words = f.read().splitlines()
        words.append ("a")
        words.append ("i")
        words.append ("")
        children_words = {}
        count = 0
    # for word in words:
    #     for i in range (0, len(word)):
    #         nieuw_woord = word[:i] + word[i+1:]
    #         if nieuw_woord in words:
    #             children_words[word] = children_words.get(word, []) + [nieuw_woord]
    #             print (count)
    #             count += 1
    y = 0
    for word in words:
        x = len(word)
        if x > y: y = x
    print (y)
    sorted_by_length = {}
    for word in words:
        sorted_by_length[f"lenght_{len(word)}"] = sorted_by_length.get(f"lenght_{len(word)}", []) + [word]

    for key, value in sorted_by_length.items():
        print (key, value)
    print (sorted_by_length.keys())
reduce_words(file)