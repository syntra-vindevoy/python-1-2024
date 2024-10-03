def triangle(letter, height):
    for i in range(height):
        leading_spaces = (height - (i+1)) * " "
        #print(f"{letter}{height},{i}, {leading_spaces}")
        print(leading_spaces + letter * (2* i+1))

triangle("T", 4)