
#Write a program to create a function that takes two arguments, name and age,
# and print their value.
def names(names, age):
    print(names, age)

names("John","23")


# Write a program to create function func1() to accept a variable length of
# arguments and print their value.
#
# Note: Create a function in such a way that we can pass any number of arguments to
# this function, and the function should process them and display each argument’s value.

def func1(*b):
    for i in b:
        print(i)

func1(1,2,3,4,5)

#Write a program to create function calculation() such that it can accept two
# variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.

def calculation(a, b):
    subtraction = (a - b)
    add = (a + b)
    return( add, subtraction)
res = calculation(40, 10)
print(res)

# Write a program to create a function show_employee() using the following conditions.
#
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary = 9000):
    print(f"Name: {name}, salary: {salary}")

show_employee("Ben", 12000)
show_employee("Jessa")

#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
#A recursive function is a function that calls itself again and again.


def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(30)
print(res)

print(list(range(4, 30, 2)))

def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)

#Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=", ")


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))