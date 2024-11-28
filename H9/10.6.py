def has_duplicates(lst):
    for i in lst:
        if lst.count(i) > 1:  # Count occurrences of the element in the list
            return True
    return False  # If no duplicates are found, return False

# Example usage:
print(has_duplicates([1, 2, 3, 4]))  # Output: False
print(has_duplicates([1, 2, 3, 1]))  # Output: True
