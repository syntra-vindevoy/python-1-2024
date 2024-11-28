def chop(lst):
    if len(lst) > 1:
        del lst[0]  # Remove the first element
        del lst[-1]  # Remove the last element


# Example usage:
t = [1, 2, 3, 4]
chop(t)
print(t)  # Output: [2, 3]
