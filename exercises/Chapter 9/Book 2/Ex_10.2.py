
# Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumu
# lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
# original list. For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

t = [1, 2, 3]

def cumsum(t):
    s = []
    listsum = 0
    for i in t:
        listsum += i
        s.append(listsum)

    return s

def cumsum_AI(t):
    return [sum(t[:i + 1]) for i in range(len(t))]

def main():
    print(cumsum_AI(t))

if __name__ == "__main__":
    main()
