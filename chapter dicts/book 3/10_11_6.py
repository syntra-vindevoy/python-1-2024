from sortedcontainers import SortedDict


def interlocking():
    with open ("../words.txt", "r") as f:
        words = f.read().splitlines()
        words =set(words) #set gaat massas sneller!
    # interlocking = {}
    # for word in words:
    #     word1 = word[0::2]
    #     word2 = word[1::2]
    #     if word1 in words and word2 in words:
    #         interlocking[word] = word1, word2
    #onliner

    interlocking = SortedDict({word: (word[0::2], word[1::2]) for word in words if word[0::2] in words and word[1::2] in words})

    return interlocking

print (interlocking())
