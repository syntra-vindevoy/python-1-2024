"""
Exercise 1
Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames; it should
read the first file and write the contents into the second file (creating it if necessary). If the pattern string
appears anywhere in the file, it should be replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files, your program should catch the exception,
print an error message, and exit. Solution: https://thinkpython.com/code/sed.py.
"""
import pathlib


def sed(pattern, replacement, file1, file2):
    try:
        with open(file1) as file_1:
            with open(file2, 'w') as file_2:
                for line in file_1:
                    file_2.write(line.replace(pattern, replacement))
    except Exception as e:
        print(f"Error: {e}")


"""
Exercise 3  
In a large collection of MP3 files, there may be more than one copy of the same song,
 stored in different directories or with different file names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories, recursively, 
and returns a list of complete paths
 for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for 
 manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for each files. 
If two files have the same checksum, they probably have the same contents.
To double-check, you can use the Unix command diff.
Solution: https://thinkpython.com/code/find_duplicates.py.

"""
import hashlib
from pathlib import Path

def walk_dir (dir_path,suffix)->[pathlib.Path]:
    filenames = []
    for f in Path(dir_path).iterdir():
        if f.is_file() and f.suffix[1:]==suffix:
            filenames.append(f)
        elif f.is_dir():
            filenames.extend(walk_dir(f.resolve(),suffix))
    return filenames


def checksum (filename:str)->str:
    with open (filename, 'rb') as file_c:
        data = file_c.read ()
        md5_hash = hashlib.md5 ()
        md5_hash.update (data)
        digest = md5_hash.hexdigest ()
        return digest

def find_duplicates (dir_path:Path, suffix:str)->[(Path,Path)]:
    double_files = []
    files=walk_dir (dir_path,suffix)
    for file_1 in files:
        for file_2 in files:
            if file_1.name != file_2.name:
                if checksum (file_1)==checksum(file_2):
                   double_files.append((file_1,file_2))
    return double_files


if __name__ == '__main__':
    sed('project', '*******', 'AI.txt', 'change.txt')
    doubles_f=find_duplicates(Path.joinpath(Path(__file__).parent,"photos"),"jpg")
    for file,file2 in doubles_f:
        print (f"checksum equal : {file} --- {file2}")