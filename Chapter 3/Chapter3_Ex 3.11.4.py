# Write a function called rectangle that takes a string
# and two integers and draws a rectangle with the given width and height, made up using copies of the string.
# Here’s an example of a rectangle with width 5 and height 4, made up of the string 'H'.

# def rectangle(char , height , width):
#     for i in range(height):
#         print(char * width)
#
# rectangle('*',4,5)

# OR
def triangle(char, number):
    for i in range(1 , number + 1):
        print(char * i)

triangle("*" , 5)


