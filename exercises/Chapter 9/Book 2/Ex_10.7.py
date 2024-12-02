# Exercise 10.7.
# Write a function called has_duplicates that takes a list and returns True
# if there is any element that appears more than once.It should not modify
# the original list.

def has_duplicates(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                return True
    return False

def main():
    print(has_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7]))

if __name__ == '__main__':
    main()