#What is the longest word you can think of where each letter appears only once?
#Let’s see if we can find one longer than unpredictably.

#Write a function named has_duplicates that takes a sequence – like a list or string
#– as a parameter and returns True if there is any element that appears in the sequence more than once.

def has_duplicates(sequence):
    counter = {}
    for item in sequence:
        if item in counter:
                return True
        counter[item] = 1
    return False

print(has_duplicates("sébastien"))
print(has_duplicates("Thomas"))