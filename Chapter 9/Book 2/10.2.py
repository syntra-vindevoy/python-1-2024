#Write a function called cumsum that takes a list of numbers and returns the cumu- lative sum;
# that is, a new list where the ith element is the sum of the first i + 1 elements from the original list.
# For example:

# t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

def cumsum(t):
    result = []
    total = 0
    for num in t:
        total += num
        result.append(total)
    return result

t = [1, 5, 7, 9]
print(cumsum(t))

