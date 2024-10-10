#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

def main():
    name = input("What is your name?")
    print(f"Your name is {name}")


    age = input("How old are you?")
    print(f"You are {age} years old")

if __name__ == '__main__':
    main()