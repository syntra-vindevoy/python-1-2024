from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IPersonRepo(ABC):


    @abstractmethod
    def get_all_persons(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def add_person(self, employee_data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def delete_employee(self, employee_id: int) -> None:
        pass