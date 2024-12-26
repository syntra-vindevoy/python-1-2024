with open("output.txt", "w") as file:
    file.write("Thomas")                #New line is not added
    file.write("Meersschaut\n")
    file.write("Thomas\n")
    file.write("Meersschaut\n")
    file.writelines(["Thomas\n", "Meersschaut\n"])

