# counter = value_counts('brontosaurus')
#
# counter.get('b', 0)
#
# counter.get('c', 0)

# oef 3

def has_duplicates(t):
    return len(t) != len(set(t))

print(has_duplicates('banana'))  # True, 'a' and 'n' repeat
print(has_duplicates('ambidextrously'))  # False, no duplicates
print(has_duplicates([1, 2, 2]))  # True, 2 repeats
print(has_duplicates([1, 2, 3]))  # False, no duplicates

# ex 3

lst = ['zero', 'one', 'two']