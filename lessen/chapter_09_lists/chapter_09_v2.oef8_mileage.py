opdracht = """
Exercise 8   Heres another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
“I was driving on the highway the other day and I happened to notice my odometer. Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And you ready for this? One mile later, all 6 were palindromic!
“The question is, what was on the odometer when I first looked?”
Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements. Solution: https://thinkpython.com/code/cartalk2.py.

"""

def is_palindrome(numberstring: str)->bool:
    return numberstring == numberstring[::-1]

def int_to_str(number: int) -> str:
    return str(number).rjust(6,"0")

for x in range(1_000_000):
    if not is_palindrome(int_to_str(x)[-4:]):continue # x = last 4 digits are palindromic       
    if not is_palindrome(int_to_str(x+1)[-5:]):continue # x + 1 = last 5 digits are palindromic
    if not is_palindrome(int_to_str(x+2)[1:5]):continue # x + 2 = middle 4 out of 6 digits are palindromic
    if not is_palindrome(int_to_str(x+3)):continue # x + 3 = all 6 digits are palindromic        
    print(x,x+1,x+2,x+3)
print("finished")

