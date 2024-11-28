#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
# For example:
#>>> t = [1, 2, 3, 4]
#>>> middle(t)


def middle(t):
    t.pop(0)
    t.reverse()
    t.pop(0)
    t.reverse()
    return t

t = [1, 2, 3, 4, 5, 6, 7]
print(middle(t))