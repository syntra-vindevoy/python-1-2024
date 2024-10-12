import os


def search_file(directory, target_file):
    # Get the list of files and subdirectories in the current directory
    for item in os.listdir(directory):
        # Create full path of the item
        item_path = os.path.join(directory, item)

        # If the item is a directory, recursively search within it
        if os.path.isdir(item_path):
            result = search_file(item_path, target_file)
            if result:  # If the file was found in the subdirectory, return the result
                return result

        # If the item is a file and matches the target, return its path
        elif item == target_file:
            return item_path

    # If the file is not found, return None
    return None





def main():
    # Example usage:
    start_directory = 'C:\\temp'  # Replace with the directory where you want to start searching
    target_filename = 'ht.htmx'  # Replace with the file you want to search for

    file_path = search_file(start_directory, target_filename)
    if file_path:
        print(f"File found: {file_path}")
    else:
        print("File not found.")


if __name__ == '__main__':
    main()