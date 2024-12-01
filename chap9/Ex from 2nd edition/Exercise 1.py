# Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all the nested lists.
# For example:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21

def nested_sum(l: list) -> int:
    return sum(sum(inner) for inner in l)

print(nested_sum([[1, 2], [3], [4, 5, 6]]))  #