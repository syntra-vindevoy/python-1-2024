# Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in
# column 70 of the display.
# >>> right_justify('monty')

def right_justify(s):
    print((70 - len(s)) * " " + s)
    return

# Main
right_justify("monty")