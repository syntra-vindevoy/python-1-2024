from pathlib import Path
import os
print (Path(__file__).parent.absolute())
print (Path(__file__).parent.parent.absolute())
cwd = os.getcwd()
print(cwd)
namen = ("Kenneth\n, Teck\n")
with open (f"{cwd}/output.txt", "w") as file:
    file.writelines (namen)
current_dir = Path(__file__)
print (current_dir)
config_dir = current_dir.parent.joinpath("config", "settings")

try:
    with open ("onbestaand.txt", "r") as file:
        lines = file.readlines()
except:
    print("Error")
# except FileNotFoundError:
#     print ("File not found")
# except Exception as err:
#     print(f"Het was deze fout: {err}")
# finally:
#     print("Hier staat code die sowieso wordt uitgevoerd")

import yaml
# with open ("test.yaml", "r") as yaml_file:
#     yaml_file.writelines()
# with open ("test.yaml", "r") as yaml_file:
#     content = yaml.safe_load(yaml_file)
# print (content)

import yaml

# config_filename = 'config.yaml'
# with open(config_filename, "w") as yaml_file:
#     yaml.dump(config_filename)
# with open (config_filename, "r") as yaml_file:
#     content = yaml.safe_load(yaml_file)
# print(content)
#
# reader = open(config_filename)
# config_readback = yaml.safe_load(reader)
#
# print(config_readback)

import yaml

config = {
    'photo_dir': 'photos',
    'data_dir': 'photo_info',
    'extensions': ['jpg', 'jpeg'],
}

config_filename = 'config.yaml'
with open(config_filename, 'w') as file:
    yaml.dump(config, file)
writer = open(config_filename, 'w')
yaml.dump(config, writer)
writer.close()

readback = open(config_filename).read()
print(readback)

reader = open(config_filename)
config_readback = yaml.safe_load(reader)
print(config_readback)

import hashlib

with open("100_0017.JPG", "rb") as file:
    data = file.read()

md5_hash = hashlib.md5()
print(type(md5_hash))
md5_hash.update(data)
digest = md5_hash.hexdigest()
print (digest)

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
            with open(path, 'rb') as file:
                data = file.read()
            md5_hash.update(data)
            print (md5_hash.hexdigest())
        elif os.path.isdir(path):
            walk(path)
#walk("foto")

