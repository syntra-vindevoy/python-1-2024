
# Write a function called nested_sum that takes a list of lists of integers and adds up
# the elements from all of the nested lists. For example:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21

t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t):
    sumt = 0
    for i in t:
        for j in i:
            sumt += j
    return sumt

def main():
    print(nested_sum(t))

if __name__ == "__main__":
    main()
