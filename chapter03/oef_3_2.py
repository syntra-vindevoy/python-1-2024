def triangle(letter, height):
    for i in range(height):
        leading_spaces = (height - (i+1)) * " "
        #print(f"{letter}{height},{i}, {leading_spaces}")
        print(leading_spaces + letter * (2* i+1))

def triangle_90(letter, height):
    for i in range(height):
        print(letter * (i+1))   #hier gaat elke lijn een berekening gebeuren

def triangle_90_betere_oplossing(letter, height):
    for i in range(1, height +1):  #hier gebeurt maar 1 berekening
        print(letter * i)


def main():
    triangle("T", 4)
    triangle_90("T", 4)
    triangle_90_betere_oplossing("*", 4)

if __name__ == "__main__":
    main()