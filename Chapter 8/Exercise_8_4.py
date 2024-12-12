# # Exercise 8.4. The following functions are all intended to check whether a string contains any lowercase letters
# # but at least some of them are wrong. For each function, describe what the function actually does
# # (assuming that the parameter is a string).
#
# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False
# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'
# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag
# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
# return flag
# def any_lowercase5(s):
#     for c in s:
#         if not c.islower():
#             return False
# return True

# #Summary
# Correct function: any_lowercase4(s) works as intended.
# Issues with others:
# any_lowercase1: Only checks the first character.
# any_lowercase2: Always returns 'True'.
# any_lowercase3: Only checks the last character.
# any_lowercase5: Checks if all characters are lowercase instead of any.