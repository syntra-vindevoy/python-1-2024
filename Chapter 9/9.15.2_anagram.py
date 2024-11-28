#Two words are anagrams if you can rearrange the letters from one to spell the other. For example, tops is an anagram of stop.
#Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(word_1: str, word_2: str) -> bool:
    return ''.join(sorted(word_1)) == ''.join(sorted(word_2))

assert is_anagram("pot", "top") == True
assert is_anagram("stop", "top") == False
assert is_anagram("stoep", "poets") == True

with open("words.txt") as f:
    words = f.read().split("\n") #split so it removes the "\n" characters

for word in words:
    if is_anagram(word, "takes"):
        print(word)

#list with anagrams
anagrams = [word for word in words if is_anagram(word, "takes")]
print(anagrams)