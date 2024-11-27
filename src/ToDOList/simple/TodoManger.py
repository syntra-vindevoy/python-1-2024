from src.ToDOList.domain.todo import Todo


class ToDoManager:
    __instance = None
    __name: str = "Manager"
    __to_do_set: set = set()

    def add_to_do(self, to_do: Todo):
        self.__to_do_set.add(to_do)

    def remove_to_do(self, to_do: Todo):
        self.__to_do_set.remove(to_do)

    def get_to_do_list(self):
        return list(self.__to_do_set)

    def get_to_do_list_status(self, status: str):
        return [t for t in self.__to_do_set if t.status == status]

    def delete_task(self, todo):
        self.__to_do_set.remove(todo)

    def delete_all_task(self):
        self.__to_do_set.clear()

    def __iter__(self):
        return iter(self.__to_do_set)

    def __len__(self):
        return len(self.__to_do_set)

    @classmethod
    def get_instance(cls, s):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            __name = s
        return cls.__instance
