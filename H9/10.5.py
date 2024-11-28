def is_sorted(lst):
    if lst == sorted(lst):  # Compare the list to its sorted version
        return True
    else:
        return False

# Example usage:
lst1 = [1, 2, 2]
lst2 = ['b', 'a']
print(is_sorted(lst1))  # Output: True
print(is_sorted(lst2))  # Output: False
