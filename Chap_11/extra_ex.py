
# Write a program to create a new string made of an input string’s first,
# middle, and last character.
def first_middle_last(input_str):
    length = len(input_str)
    middle_index = length // 2
    new_str = input_str[0] + input_str[middle_index] + input_str[-1]
    return new_str

# Write a program to create a new string made of the middle three characters
# of an input string.
def middle_thee(input_str):
    length = len(input_str)
    middle = length // 2
    return input_str[middle -1:middle + 2]

# Given two strings, s1 and s2. Write a program to create a new string s3 by
# appending s2 in the middle of s1.
def append_middle(input_str1, input_str2):
    length = len(input_str1) // 2
    return input_str1[:length] + input_str2 + input_str1[length:]

# Given two strings, s1 and s2, write a program to return a new string made of
# s1 and s2’s first, middle, and last characters.
# def combine_letters(input_str1, input_str2 ):
#     length1 = len(input_str1) // 2
#     length2 = len(input_str2) // 2
#     output_str1 = input_str1[:1] + input_str2[:1]
#     output_str2 = input_str1[length1:length1 + 1] + input_str2[length2:length2 + 1]
#     output_str3 = input_str1[-1:] + input_str2[-1:]
#
#     return output_str1 + output_str2 + output_str3
# chatgpt answer
def combine_letters(input_str1, input_str2):
    mid1 = len(input_str1) // 2
    mid2 = len(input_str2) // 2
    return (input_str1[0] + input_str2[0] +
            input_str1[mid1] + input_str2[mid2] +
            input_str1[-1] + input_str2[-1])

# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase
# letters should come first.
# def sort_lower_and_upper(string1):
#     lower = []
#     upper = []
#     for char in string1:
#         if char.islower():
#             lower.append(char)
#         else:
#             upper.append(char)
#     return "".join(lower) + "".join(upper)
# Chatgpt answer
def sort_lower_and_upper(string1):
    lower, upper = [], []
    [lower.append(c) if c.islower() else upper.append(c) for c in string1]
    return "".join(lower + upper)

# def count_string(string2):
#     spec_char, letter, digit = [], [], []
#     # [spec_char.append(char) if char.isalnum() else digit.append(char) for char in string2]
#     for char in string2:
#         if char.isalpha():
#             letter.append(char)
#         elif char.isdigit():
#             digit.append(char)
#         else:
#             spec_char.append(char)
#     return f"letters: {len(letter)}, digits: {len(digit)}, special characters: {len(spec_char)}"

# Chatgpt answer
def count_string(string2):
    letter, digit, spec_char = [], [], []
    [(letter.append(c) if c.isalpha() else (digit.append(c) if c.isdigit()
                                        else spec_char.append(c))) for c in string2]
    return f"letters: {len(letter)}, digits: {len(digit)}, special characters: {len(spec_char)}"

def are_strings_balanced(s1, s2):

    set_s1 = set(s1.lower())
    set_s2 = set(s2.lower())
    return set_s2.issubset(set_s1)




# Example usage:
if __name__ == "__main__":
    test_str = "James"
    result = first_middle_last(test_str)
    print(result)  # Should print: Jms
    test2 = "JaSonAy"
    result2 = middle_thee(test2)
    print(result2)
    # s1 = "Ault"
    # s2 = "Kelly"
    # result3 = append_middle(s1, s2)
    # print(result3)
    s1 = "America"
    s2 = "Japan"
    result4 = combine_letters(s1, s2)
    print(result4)
    s3 = "PyNaTive"
    result5 = sort_lower_and_upper(s3)
    print(result5)
    s4 = "P@#yn26at^&i5ve"
    result6 = count_string(s4)
    print(result6)
    s5 = "pNti"
    s6 = "PYnative"
    result7 = are_strings_balanced(s6, s5)
    print(result7)

