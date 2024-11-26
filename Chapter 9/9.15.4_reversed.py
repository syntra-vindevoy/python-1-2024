#Write a function called reverse_sentence that takes as an argument a string that contains any number of words separated by spaces.
# It should return a new string that contains the same words in reverse order. For example, if the argument is “Reverse this sentence”,
# the result should be “Sentence this reverse”.


#Hint: You can use the capitalize methods to capitalize the first word and convert the other words to lowercase.

def reverse_sentence(string):
    # Split the sentence into words, reverse the list, and join back
    reversed_sentence = ' '.join(string.split()[::-1])
    reversed_sentence = reversed_sentence.lower().capitalize()
    print(reversed_sentence)


reverse_sentence("Ik ben Séba")