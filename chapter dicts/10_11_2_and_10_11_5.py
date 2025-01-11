def value_counts(word):
    d = {}
    for letter in word:
        d [letter] = d.get(letter, 0) + 1
    return (d)

value_counts("hallo")

# def merge_counts():
#     first = value_counts("hallo")
#     second = value_counts("okidoki")
#     merge = first.copy()
#     for letter in second:
#         if letter in first:
#             merge[letter] += second.get(letter)
#         else: merge[letter] = second.get(letter)
#     print (merge)

def merge_counts():
    first = value_counts("hallo")
    second = value_counts("okidoki")
    merge = first.copy()
    for letter in second:
        merge[letter] = merge.get(letter, 0) + second[letter]
    print(merge)
    return merge


merge_counts()
