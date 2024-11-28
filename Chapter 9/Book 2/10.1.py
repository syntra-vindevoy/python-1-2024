#Exercise 10.1. Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists.
#For example:
#>>> t = [[1, 2], [3], [4, 5, 6]]
#>>> nested_sum(t)

t = [[1, 2], [3], [4, 5, 6]]
def nested_sum(t: list) -> int:
    total = 0
    for sublist in t:  # Iterate through each sublist in t
        total += sum(sublist)  # Add the sum of the current sublist to total
    return total  # Return the total sum

# Test the function
print(nested_sum(t))  # Output: 21