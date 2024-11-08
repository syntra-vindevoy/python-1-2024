import hashlib
import os

import yaml


def walk (dirname):
    for name in os.listdir (dirname):
        path = os.path.join (dirname, name)

        if os.path.isfile (path):
            print (path)
        elif os.path.isdir (path):
            walk (path)


def md5_digest (filename):
    data = open (filename, 'rb').read ()
    md5_hash = hashlib.md5 ()
    md5_hash.update (data)
    digest = md5_hash.hexdigest ()
    return digest


def main ():
    print (os.getcwd ())
    file_name = os.getcwd ()
    list_files = os.listdir ()
    for file in list_files:
        if os.path.isdir (os.path.join (file_name, file)):
            print (f"is dir {file} {os.path.isdir (file)}")
            print (file, end=' ')
        else:
            print (f"file size {file} {os.path.getsize (file)} bytes")
            print (file)
        print (file, end=' ')
    print (os.path.exists ('photos'))
    print (os.path.join ('photos', 'jan-2023', 'photo1.jpg'))

    num_years = 1.5
    num_camels = 23
    writer = open ('camel-spotting-book.txt', 'w')
    writer.write (str (num_years))
    writer.write (str (num_camels))
    writer.close ()

    line = f'In {round (num_years * 12)} months I have spotted {num_camels} camels'
    writer = open ('camel-spotting-book.txt', 'w')
    writer.write (f'Years of observation: {num_years}\n')
    writer.write (f'Camels spotted: {num_camels}\n')
    writer.close ()

    # YAML

    config = {
        'photo_dir': 'photos',
        'data_dir': 'photo_info',
        'extensions': ['jpg', 'jpeg'],
    }

    config_filename = 'config.yaml'
    writer = open (config_filename, 'w')
    yaml.dump (config, writer)
    writer.close ()

    reader = open (config_filename)
    config_readback = yaml.safe_load (reader)
    print (config_readback)
    reader.close ()

    def sort_word (word):
        return ''.join (sorted (word))

    # Shelve
    word = 'tops'
    import shelve
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

    walk (os.getcwd ())


if __name__ == '__main__':
    main ()
