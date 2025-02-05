import yaml

config = {
    'photo_dir': 'photos',
    'data_dir': 'photo_info',
    'extensions': ['jpg', 'jpeg'],
}

config_filename = 'config.yaml'
writer = open(config_filename, 'w')
yaml.dump(config, writer)
writer.close()

readback = open(config_filename).read()
print(readback)

reader = open(config_filename)
config_readback = yaml.safe_load(reader)
print(config_readback)