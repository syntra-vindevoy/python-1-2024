"""Exercise 14.1. Write a function called sed that takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit"""
from sys import exception


def sed(pattern, replacement, filename_original, filename_replacement):
    if not isinstance(filename_replacement, str) or not isinstance(filename_original, str):
        print ("insert valid filenames")
        return
    try:
        with open (filename_original, "r") as file:
            file_content = file.read()
    except FileNotFoundError:
        print("File not found")
        return
    except exception as err:
        print(f"this error occurs: {err}")
        return

    with open (filename_original, "r") as file:
        file_content = file.read()

    file_new_content = file_content.replace(pattern, replacement)

    with open (filename_replacement, "w") as file:
        file.write(file_new_content)

sed ("abc", "def", 15, "new_file.txt")
