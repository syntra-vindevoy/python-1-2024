def addition(a, b):
    return a + b

#main program
def main():
nim1 = float(input("Enter the first number:\n "))
nim2 = float(input("Enter the second number:\n "))

#calling our function
result = addition(nim1, nim2)
print("The result is", result)

main()