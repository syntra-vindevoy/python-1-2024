# Exercise 11.4.If you did Exercise 10.7, you already have a function
# named has_duplicates that takes a list as a parameter and returns True if there is any object that appears
# more than once in the list. Use a dictionary to write a faster, simpler version of has_duplicates.

#examples:
# def has_duplicates(list):
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] == list[j]:
#                 return True
#     return False
#
# def has_duplicates_2(list):
#     return len(list) != len(set(list))
#
# def has_duplicates_3(list):
#     for i in range(len(list) - 1):
#         if sorted(list)[i] == sorted(list)[i+1]:
#             return True

def has_duplicates(t):
    count_dict = {}
    for item in t:
        if item in count_dict:
            return True
        else:
            count_dict[item] = 1
    return False

def main():
    print(has_duplicates([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()