from os import getcwd, listdir
from os.path import abspath, exists, isdir, isfile, join

cwd = getcwd()
print(f"The current directory is: {cwd}")

abs_path = abspath("memo.txt")
print(f"The absolute path of memo.txt is: {abs_path}")

list_dir = listdir("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_13_files")
print(f"The 2nd item of this directory is: {list_dir[1]}")

path_exists = exists("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_13_files")
print(f"This path exists: {path_exists}")

path_exists = exists("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_03_files")
print(f"This path exists: {path_exists}")

is_dir = isdir("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_13_files")
print(f"This path is a directory: {is_dir}")

is_dir = isdir("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_13_files/memo.txt")
print(f"This path is a directory: {is_dir}")

is_file = isfile("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_13_files")
print(f"This path is a file: {is_file}")

is_file = isfile("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_13_files/memo.txt")
print(f"This path is a file: {is_file}")

new_path = join("C:","Users","thoma","Documents", "Python", "Syntra", "python-1-2024", "_13_files", "memo.txt")
print(new_path)