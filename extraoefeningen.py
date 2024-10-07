import math

# Exercise Character Input

name = input("What is your name? ")

#de lange manier
age = input("What is your age? ")
age = int(age)
#de korte manier zou zijn: age = int(input("What is your age?")

year = 2024 - age + 100


print(f"Hello nice to meet you {name}, you'll be 100 years old in {year} ")


# Odd or Even

number = int(input("What is your number? "))
mod = number % 2
if mod > 0:
    print("Your number is ODD")
else:
    print("Your number is EVEN")

# Extra

num = int(input("Give me a number to check "))
div = int(input("Give me a number to divide by "))
if num % 4 == 0:
    print("Your nr is a multiple of 4")
elif num % 2 == 0:
    print("Your nr is EVEN")
else:
    print("Your nr is ODD")

# Rock Scissor Paper

hand = input("Rock Scissor, Paper ")
if hand == "Rock":







