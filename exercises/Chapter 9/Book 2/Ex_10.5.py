# Exercise 10.5.
# Write a function called is_sorted that takes a list as a parameter
# and returns True if the list is sorted in ascending order
# and False otherwise.
# For example:
# >>> is_sorted([1, 2, 2]) True
# >>> is_sorted(['b', 'a']) False

def is_sorted(t):
    if t == sorted(t):
        return True
    else:
        return False

def main():
    print(is_sorted([1, 2, 2]))

    assert is_sorted([1, 2, 2]) == True
    assert is_sorted(['b', 'a']) == False
    assert is_sorted(["a", "b", "C"]) == True
    assert is_sorted(["a", "c", "b"]) == False

if __name__ == '__main__':
    main()