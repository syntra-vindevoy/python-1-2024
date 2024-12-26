import hashlib
import os
from pathlib import Path
import yaml
import shelve

#todo
def walk (dir_path):
    dir_path = Path(dir_path)
    files = list(dir_path.iterdir())
    for name in files:
        if name.is_file():
            print (name)
        elif name.is_dir():
            walk (name)


def md5_digest (filename):
    try:
        with open (filename, 'rb') as file:
            data = file.read ()
            md5_hash = hashlib.md5 ()
            md5_hash.update (data)
            digest = md5_hash.hexdigest ()
            return digest
    except FileNotFoundError:
        print (f"File not found: {filename}")
        return None


def yaml_demo():
    config = {
        'photo_dir': 'photos',
        'data_dir': 'photo_info',
        'extensions': ['jpg', 'jpeg'],
    }

    config_filename = 'config.yaml'
    with open (config_filename, 'w') as writer:
        yaml.dump (config, writer)

    with open (config_filename) as reader:
        config_readback = yaml.safe_load (reader)
        print (config_readback)




    # Find all text files inside a directory
def main ():
    for file in Path.cwd().iterdir():
        if file.is_dir ():
            print (f"is dir {file} {file.name}")
            print (file.name, end=' ')
        else:
            print (f"file size {file}  bytes")
            print (file)
        print (file, end=' ')
    print (os.path.exists ('photos'))
    print (os.path.join ('photos', 'jan-2023', 'photo1.jpg'))

    num_years = 1.5
    num_camels = 23
    with open ('camel-spotting-book.txt', 'w') as writer:
        writer.write (str (num_years))
        writer.write (str (num_camels))
        writer.write(f'Years of observation: {num_years}\n')
        writer.write(f'Camels spotted: {num_camels}\n')



def shelf_demo ():
    def sort_word(word_in):
        return ''.join(sorted(word_in))

    word = 'tops'

    shelf_filename = 'mydata.shelf'
    shelf = shelve.open (shelf_filename, 'c')
    shelf['animals'] = ['bear', 'tiger', 'penguin', 'zebra']
    print ("animals:")
    print (list (shelf.keys ()))
    shelf.close ()
    shelf = shelve.open (shelf_filename)
    print (shelf['animals'])
    for key in shelf:
        print (key, ':', shelf[key])
    anagram_list = shelf[key]
    anagram_list.append (sort_word (word))
    shelf[key] = anagram_list
    shelf.close ()




if __name__ == '__main__':
    walk (os.getcwd ())
    yaml_demo()
    shelf_demo ()
    main ()
    current_path = Path(__file__)
    print (current_path)
