# Exercise 1: Print first 10 natural numbers using while loop
#------------------------------------------------------------

def print_numbers(a):
    while a <= 10:
        #print(a)
        a += 1

print_numbers(0)


# Exercise 2: Print the following pattern
#----------------------------------------

# row = 5
# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1
# # run loop 5 times
# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")

row = 15

def print_numbers2(b):
    while b <= row:
        #print(b)
        b += 1
        for i in range(1, b):
            if b < row +1:
                #print(i, end=" ")
                i += 1

print_numbers2(1)

# Calculate sum of all numbers from 1 to a given number
#------------------------------------------------------

cal = 64
# run loop n times
# stop: n+1 (because range never include stop number in result)
def print_numbers3(d):
    s = 0
    for i in range(1, d + 1, 1):
        # add current number to sum variable
        s += i
    return s
res = (print_numbers3(cal))
#print(res)


# Print multiplication table of a given number
#---------------------------------------------

num = 6

def print_numbers4(f):
    for i in range(1, 11):
        e = i * f
        #print(f" {i} * {f} = {e}")
# is only for the outcome
    return e
#print(f" the end of the table of {num} = {print_numbers4(num)}")

#   Display numbers from a list using a loop
#--------------------------------------------

numbers = [12, 75, 150, 180, 145, 525, 50]
result = []
for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    # check if number is divisible by 5
    elif num % 5 == 0:

        result.append(num)  # Append num to the result list
        #print(num)
#print(result)  # Print the list of numbers that met the conditions
#print(sum(numbers))  # Print the sum of all numbers in the list


# Print the following pattern
#----------------------------

row = 6

def print_numbers5(f):

    for j in range(0, f +1 ):
        for i in range(f-j, 0, -1):
           print(i, end=" ")
        print()


print_numbers5(row)

# list1 = [10, 20, 30, 40, 50]
#
# def print_numbers6():
#     new_list = reversed(list1)
#     for item in new_list:
#         print(item)
#
# print_numbers6()

# dec = 10
# def print_numbers7(dec):
#     for i in range(dec * -1, 0):
#         #print(i)
#
# print_numbers7(dec)

num2 = 4

# def print_numbers8(num2):
#     for i in range(1, 5):
#         print(i, '\n')
#     print("done!")
#
# print_numbers8(num2)

# start = 25
# end = 125
#
# def print_numbers9(start, end):
#     for num in range(start, end + 1):
#         if num > 1:
#             for i in range(2, num):
#                 # check for factors
#                 if (num % i) == 0:
#                     # not a prime number so break inner loop and
#                     # look for next number
#                     break
#             else:
#                 print(num, end=" ")
#
#
#print_numbers9(start, end)

# num1 = 9863665
# def print_numbers10(num):
#     reverse_num = 0
#     while num > 0:
#         reminder = num % 10
#         reverse_num = reverse_num * 10 + reminder
#         num = num // 10
#     return reverse_num
#
#
#
#
# rev = print_numbers10(num1)
# print(rev)
#
max_row = 5
def print_numbers11(max_row):
    for i in range(1, max_row):
        print("* "* i)
        i += 1
        if i == max_row:
            for j in range(max_row , 0, -1):
                print("* " * j)
                if j == 0:
                    return

print_numbers11(max_row)

input_number = 6
def print_numbers12(input_number):
    for i in range(1, input_number + 1):
        cube = i ** 3
        #print(f"the cube of {i} = {cube}")
        if i == input_number:
            return cube

res2 = print_numbers12(input_number)
#print(res2)

numbera = 9
start = 2

def print_numbers13(start, numbera):
    total = 0
    for i in range(0, numbera):
        if i < numbera - 1:
            print(start ,end=" + ")
        else:
            print(start,  end=" ")
        total += start
        start = (start * 10) + 2
    return total

res5 = print_numbers13(start, numbera)
print( "=", res5)

