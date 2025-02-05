from pathlib import Path

# Get the current working directory
cwd = Path.cwd()
print(f"The current directory is: {cwd}")

# Get the absolute path of the file
abs_path = Path("memo.txt").resolve()
print(f"The absolute path of memo.txt is: {abs_path}")

# List the contents of a directory
directory = Path("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_13_files")
list_dir = list(directory.iterdir())
print(f"The 2nd item of this directory is: {list_dir[1]}")

# Check if a path exists
path_exists = directory.exists()
print(f"This path exists: {path_exists}")

non_existent_path = Path("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_03_files")
path_exists = non_existent_path.exists()
print(f"This path exists: {path_exists}")

# Check if a path is a directory
is_dir = directory.is_dir()
print(f"This path is a directory: {is_dir}")

memo_path = directory / "memo.txt"
is_dir = memo_path.is_dir()
print(f"This path is a directory: {is_dir}")

# Check if a path is a file
is_file = directory.is_file()
print(f"This path is a file: {is_file}")

is_file = memo_path.is_file()
print(f"This path is a file: {is_file}")

# Join paths
new_path = Path("C:/Users/thoma/Documents/Python/Syntra/python-1-2024/_13_files") / "memo.txt"
print(new_path)