
from itertools import product


def combine_two_iterables(list1, list2):
    result = set()
    for item1 in list1:
        for item2 in list2:
            result.add((item1, item2))
    return result

def product_two_iterables(iter_1, iter_2):
    return set(product(iter_1, iter_2))

# Example usage:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = combine_two_iterables(list1, list2)
print(combined)

list1 = [2, 3, 4]
list2 = ['a', 'b', 'c']
product = product_two_iterables(list1, list2)
print(product)

combined.update(product)
print(combined)