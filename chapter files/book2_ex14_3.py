"""Exercise 14.3. In a large collection of MP3 files, there may be more than one copy of the same song,
stored in different directories or with different file names. The goal of this exercise is to search for
duplicates.
1. Write a program that searches a directory and all of its subdirectories, recursively, and returns
a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides
several useful functions for manipulating file and path names.
2. To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two
files have the same checksum, they probably have the same contents.
3. To double-check, you can use the Unix command diff"""

from pathlib import Path
import hashlib

def search_for_duplicates(search_dir, files_and_hash):
    if Path.exists(search_dir):
        print ("path exists")
    else:
        print ("path does not exist")
        return
    files = list(search_dir.glob("*.*"))
    for file in files:
        if file.is_file():
            with open (file, "rb") as f:
                data = f.read()
                file_hash = hashlib.md5(data).hexdigest()

                if file_hash in files_and_hash:
                    files_and_hash[file_hash].append(file)
                else:
                    files_and_hash[file_hash] = [file]

    dirs = list(search_dir.glob("*/"))
    for dir in dirs:
        search_for_duplicates(dir, files_and_hash)


    for file_hash, file_list in files_and_hash.items():
        if len(file_list) > 1:
            print(f"Hash: {file_hash}")
            for file in file_list:
                print(f"  {file}")

cwd = Path.cwd()
search_dir = cwd.absolute() / "foto"
files_and_hash = {}
search_for_duplicates(search_dir, files_and_hash)
