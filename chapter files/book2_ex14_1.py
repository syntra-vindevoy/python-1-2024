"""Exercise 14.1. Write a function called sed that takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit"""
from sys import exception


def sed(pattern, replacement, filename_original, filename_replacement):

    try:
        with open (filename_original, "r") as file:
            file_content = file.read()
    except FileNotFoundError:
        print("File not found")
        return
    except Exception as err:
        print(f"this error occurs: {err}")
        return

    file_new_content = file_content.replace(pattern, replacement)

    try:
        with open(filename_replacement, "a") as file:
            file.write(file_new_content)

    except Exception as err:
        print(f"Could not write to file: {err}")
        return


sed ("abc", "def", "original.txt", "new.txt")
