# https://colab.research.google.com/github/AllenDowney/ThinkPython/blob/v3/chapters/chap03.ipynb#scrollTo=b47467fa
# Write a function called triangle that takes a string and an integer and
# draws a pyramid with the given height, made up using copies of the string.
# Here's an example of a pyramid with 5 levels, using the string 'L'.

# Voorbeeld Yves
# def triangle(char, number):
#     for i in range(number):
#         #for j in range(i + 1):
#          #   print(char, end= "")
#
#         print( char * ( i + 1 ))
# triangle( char="*", number=5)

# Voorbeeld 2 Yves "Voor meer driehoeken te printen en snelheid python controlleren."
from datetime import datetime


def triangle(char, number):
    for i in range(1, number + 1):
        print(char * i)

def triangle2(char, number):
    # Generate the lines of the triangle in a list
    lines = [char * i for i in range(1, number + 1)]
    # Join all the lines into a single string separated by newline characters and print it
    print("\n".join(lines))

n = 1000000

start = datetime.now()

for m in range(n):
    triangle2("*", 5)

end = datetime.now()

print(end - start)

# Betere oplossing code.
# def triangle(char, number):
#     for i in range(1, number + 1):
#         #for j in range(i + 1):
#          #   print(char, end= "")
#
#         print( char * i)
# triangle( char="*", number=5)

