# Exercise 10.3
# Write a function called middle that takes a list and returns a
# new list that contains all but the first and last elements. For
# example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]

t = [1, 2, 3, 4]

def middle(t):
    return t[1:-1]

def main():
    print(middle(t))
    print(t)

if __name__ == "__main__":
    main()