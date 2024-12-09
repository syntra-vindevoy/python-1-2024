from abc import ABC, abstractmethod
from typing import List, Dict, Any

class PersonRepoInterface(ABC):

    @abstractmethod
    def get_all_persons():
        pass

    @abstractmethod
    def add_person():
        pass

    @abstractmethod
    def delete_person():
        pass


