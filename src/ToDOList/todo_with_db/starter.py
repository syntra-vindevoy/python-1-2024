import datetime

from src.ToDOList.todo_with_db.domain.todo import Todo
from src.ToDOList.todo_with_db.repository import Repository


def start():
    repo = Repository(dbname="todolist", password="", host="192.168.0.174", port="32768", user="progress")
    repo.delete_all()
    repo.insert(Todo(due_date=datetime.datetime.now(), priority=1, description="test", title="fdfd"))
    result = repo.all()
    for item in result:
        print(item)


if __name__ == '__main__':
    start()
