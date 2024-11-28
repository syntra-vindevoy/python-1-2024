import datetime

from src.ToDOList.todo_with_db.domain.statut import Status
from src.ToDOList.todo_with_db.domain.todo import Todo
from src.ToDOList.todo_with_db.repository import Repository


def start():
    repo = Repository(dbname="todolist", password="", host="192.168.0.20", port="32768", user="progress")
    repo.delete_all()
    id = repo.insert(Todo(due_date=datetime.datetime.now(), priority=1, description="test", title="fdfd"))
    one = repo.get(id)
    print("--one")
    print(one)
    print("--all")
    result = repo.all()
    for item in result:
        print(item)
    t = repo.get(id)
    t.status = Status.DONE
    repo.update(t)

    print("--all update")
    result = repo.all()
    for item in result:
        print(item)

    print("--bulk")
    for i in range(0, 20):
        repo.insert(
            Todo(due_date=datetime.datetime.now(), priority=1, description="test" + str(i), title="fdfd" + str(i)))
    print("--all ")
    result = repo.all()
    for item in result:
        print(item)
    for t in repo.all_filter(status=Status.DONE):
        print(t)
    repo.close()
if __name__ == '__main__':
    start()
