import logging

import yaml

from src.OO.singelton import Singleton


class ConfigLoader(metaclass=Singleton):
    def __init__(self, filename="config.yml"):
        logging.basicConfig(level=logging.INFO, filename="config_loader.log")
        self.__filename = filename
        self.__config = {}
        self.__load()

    @property
    def config(self):
        return self.__config

    def __load(self):
        try:
            with open(self.__filename, "r") as file:
                self.__config = yaml.safe_load(file) or {}
        except FileNotFoundError:
            logging.error(f"The file {self.__filename} does not exist.")
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML file: {e}")


if __name__ == "__main__":
    loader = ConfigLoader()
    print(loader.config)
    loader2 = ConfigLoader()
    assert loader is loader2
