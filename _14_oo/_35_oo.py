from pathlib import Path  # Import Path from pathlib to work with filesystem paths

# Two lists for demonstration
list_1 = ["a", "b", "c", "d", "e"]  # First list
list_2 = ["b", "d", "f"]  # Second list

# Concatenate the two lists and print the result
print(list_1 + list_2)

# Subtract elements in list_2 from list_1 using a set operation
# print(list_1 - list_2)  # This is commented because lists don't support subtraction directly
print(set(list_1) - set(list_2))  # Print the difference as a set
print(list(set(list_1) - set(list_2)))  # Convert the result to a list and print

# Print elements in list_2 but not in list_1
print(list(set(list_2) - set(list_1)))

# Get all `.txt` files in the "old" and "new" directories
dir_old = list(Path("old").glob("*.txt"))  # List all .txt files in the "old" directory
dir_new = list(Path("new").glob("*.txt"))  # List all .txt files in the "new" directory

# Print the list of files in the "old" and "new" directories
print(dir_old)
print(dir_new)

# Convert the files in each directory to relative paths and store them in sets
dir_old = set({path.relative_to("old") for path in Path("old").glob("*.txt")})
dir_new = set({path.relative_to("new") for path in Path("new").glob("*.txt")})

# Calculate new files and deleted files by comparing the directories
new_files = dir_new - dir_old  # Files in "new" but not in "old"
deleted_files = dir_old - dir_new  # Files in "old" but not in "new"

# Print the sets of files for debugging purposes
print(dir_old)
print(dir_new)

# Print the new and deleted files
print("new", new_files)
print("deleted", deleted_files)