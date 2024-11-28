# Exercise 10.5. Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted
# in ascending order and False otherwise. For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])

def is_sorted(t):
    if t == sorted(t):
        return "True"
    else:
        return "False"

t = [1, 2, 3, 4, 5]
print(is_sorted(t))

t = ["b", "a", "c"]
print(is_sorted(t))