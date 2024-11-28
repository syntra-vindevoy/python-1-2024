def is_anagram(word1: str , word2: str) -> str:
    return sorted(word1) == sorted(word2)

with open("words.txt", "r") as f:
    words = f.read().split("\n")

def method_5():
    w = [word for word in words if word == len(word)]
    w = [word for word in words if "t" in word]
    w = [word for word in words if "a" in word]
    w = [word for word in words if "k" in word]
    w = [word for word in words if "e" in word]
    w = [word for word in words if "s" in word]

    return [word for word in w if is_anagram(word, "takes")]
print(method_5())