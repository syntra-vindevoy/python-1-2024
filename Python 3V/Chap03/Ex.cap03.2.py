# https://colab.research.google.com/github/AllenDowney/ThinkPython/blob/v3/chapters/chap03.ipynb#scrollTo=b47467fa
# Write a function called triangle that takes a string and an integer and
# draws a pyramid with the given height, made up using copies of the string.
# Here's an example of a pyramid with 5 levels, using the string 'L'.

#Docent oefening
def triangle(char, number):
    for i in range(number):
        #for j in range(i + 1):
         #   print(char, end= "")

        print( char * ( i + 1 ))
triangle( char="*", number=5)

# Betere oplossing
# def triangle(char, number):
#     for i in range(1, number + 1):
#         #for j in range(i + 1):
#          #   print(char, end= "")
#
#         print( char * i)
# triangle( char="*", number=5)

