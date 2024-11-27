from _datetime import datetime

from src.ToDOList.domain.statut import Status


class Todo:
    def __init__(self, title: str, description: str, due_date: datetime, priority: int, status=Status.NEW,
                 id_todo=None):
        self.__id_todo = id_todo
        self.__priority: int = priority
        self.__status: Status = status
        self.__title: str = title
        self.__description: str = description
        self.__due_date: datetime = due_date

    @property
    def id_todo(self):
        return self.__id_todo

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def due_date(self):
        return self.__due_date

    @id_todo.setter
    def id_todo(self, id_todo: int):
        self.__id_todo = id_todo

    @title.setter
    def title(self, title):
        self.__title = title

    @description.setter
    def description(self, description):
        self.__description = description

    @due_date.setter
    def due_date(self, due_date):
        self.__due_date = due_date

    @property
    def priority(self):
        return self.__priority

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @priority.setter
    def priority(self, priority):
        self.__priority = priority

    def __str__(self):
        return f"{self.__title} - {self.__description} - {self.__due_date}"

    def __repr__(self):
        return f"{self.__title} - {self.__description} - {self.__due_date}"

    def __eq__(self, other):
        return self.__id_todo == other.__id_todo

    def __hash__(self):
        return hash(self.__id_todo)
