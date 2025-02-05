# Open a file named "output.txt" in write mode ("w")
# This will create the file if it doesn't exist or overwrite it if it does
with open("output.txt", "w") as file:
    # Write the string "Thomas" to the file (no newline character is added)
    file.write("Thomas")  # New line is not added

    # Write the string "Meersschaut" followed by a newline character to the file
    file.write("Meersschaut\n")

    # Write the string "Thomas" followed by a newline character to the file
    file.write("Thomas\n")

    # Write the string "Meersschaut" followed by a newline character to the file
    file.write("Meersschaut\n")

    # Write a list of strings to the file, each followed by a newline character
    file.writelines(["Thomas\n", "Meersschaut\n"])

    file.writelines(["Thomas", "Meersschaut"])
