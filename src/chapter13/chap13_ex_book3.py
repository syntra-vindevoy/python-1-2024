"""
13.10.2. Exercise
Write a function called replace_all that takes as arguments a pattern string, a replacement string, and two filenames.
 It should read the first file and write the contents into the second file (creating it if necessary).
 If the pattern string appears anywhere in the contents, it should be replaced with the replacement string.

To test your function, read the file photos/notes.txt, replace 'photos' with 'images', and write the result to the file photos/new_notes.txt.
"""
import hashlib
import os
import shelve

import yaml


def replace_all (pattern, replacement, filename):
    with open (filename, 'r') as file:
        contents = file.read ()
        contents = contents.replace (pattern, replacement)
        with open (filename, 'w') as file:
            file.write (contents)
            return contents


assert replace_all ('photos', 'images', 'photos/notes.txt') != None
"""
13.10.3. Exercise
In a previous section, we used the shelve module to make a key-value store that maps from a sorted 
string of letters to a list of anagrams. To finish the example, write a function called add_word that takes as
 arguments a string and a shelf object.

It should sort the letters of the word to make a key, then check whether the key is already in the shelf.
 If not, it should make a list that contains the new word and add it to the shelf. If so, 
 it should append the new word to the existing value.
"""


def add_word (word, shelf):
    pass


"""
13.10.4. Exercise
In a large collection of files, there may be more than one copy of the same file, stored in different directories 
or with different file names. The goal of this exercise is to search for duplicates. As an example, 
we’ll work with image files in the photos directory.

Here’s how it will work:
We’ll use the walk function from Walking directories to search this directory for files that end with one of
the extensions in config['extensions'].

For each file, we’ll use md5_digest from Checking for equivalent files to compute a digest of the contents.
Using a shelf, we’ll make a mapping from each digest to a list of paths with that digest.
Finally, we’ll search the shelf for any digests that map to multiple files.
If we find any, we’ll use same_contents to confirm that the files contain the same data.
I’ll suggest some functions to write first, then we’ll bring it all together.

To identify image files, write a function called is_image that takes a path and a list of file extensions, 
and returns True if the path ends with one of the extensions in the list. Hint: Use os.path.splitext – 
or ask a virtual assistant to write this function for you.

Write a function called add_path that takes as arguments a path and a shelf. 
It should use md5_digest to compute a digest of the file contents. Then it should update the shelf, 
either creating a new item that maps from the digest to a list containing the path, or appending the path to the list if it exists.

Write a version of walk called walk_images that takes a directory and walks through the files in the directory and 
its subdirectories. For each file, it should use is_image to check whether it’s an image file and add_path 
to add it to the shelf.

When everything is working, you can use the following program to create the shelf, search the photos directory 
and add paths to the shelf, and then check whether there are multiple files with the same digest.

db = shelve.open('photos/digests', 'n')
walk_images('photos')

for digest, paths in db.items():
    if len(paths) > 1:
        print(paths)
You should find one pair of files that have the same digest. Use same_contents to check whether they contain the same data.
"""


def is_image (path, extensions):
    return os.path.splitext (path)[1].lower ()[1:] in extensions


assert is_image ("photos/feb-2023/photo1.jpg", ["jpg", "jpeg"])


def add_path (path, shelf):
    digest = md5_digest (path)
    if digest in shelf:
        shelf[path].append (path)
    else:
        shelf[path] = [digest]


config_filename = 'config.yaml'


def walk_images (directory, config, db):
    for name in os.listdir (directory):
        path = os.path.join (directory, name)
        if is_image (path, config):
            add_path (path, db)
        elif os.path.isdir (path):
            walk_images (path, config, db)


def load_config ():
    reader = open (config_filename)
    config = yaml.safe_load (reader).get ('extensions')
    db = shelve.open ('photos/digests', 'n')
    db.clear ()
    return config, db


def md5_digest (filename):
    data = open (filename, 'rb').read ()
    md5_hash = hashlib.md5 ()
    md5_hash.update (data)
    digest = md5_hash.hexdigest ()
    return digest


def searches_for_same_digets (digets, digets2) -> {}:
    pass


if __name__ == '__main__':
    doublets = {}
    config, db = load_config ()
    walk_images ('photos', config, db)
    for paths, digest in db.items ():
        print (paths)
    db.close ()
