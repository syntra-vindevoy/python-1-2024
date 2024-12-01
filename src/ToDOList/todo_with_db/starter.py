import asyncio
import datetime

import asyncpg.connection

from src.ToDOList.todo_with_db.domain.statut import Status
from src.ToDOList.todo_with_db.domain.todo import Todo
from src.ToDOList.todo_with_db.repository import Repository


def setup_connection(dbname: str, user: str, password: str, host: str, port: str):
    return asyncpg.connect(
        database=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )


async def main():
    repo = Repository(await
                      setup_connection(dbname="todolist", password="", host="192.168.0.20", port="32768",
                                       user="progress"))
    await repo.delete_all()

    id = await repo.insert(Todo(due_date=datetime.datetime.now(), priority=1, description="test", title="fdfd"))
    one = await repo.get(id)
    print("--one")
    print(one)

    print("--all")
    result = await repo.all()
    for item in result:
        print(item)

    t = await repo.get(id)
    t.status = Status.DONE
    update_result = await repo.update(t)
    if not update_result:
        print("Update operation failed")

    print("--all update")
    result = await repo.all()
    for item in result:
        print(item)

    print("--bulk")
    for i in range(20):
        await repo.insert(
            Todo(due_date=datetime.datetime.now(), priority=1, description="test" + str(i), title="fdfd" + str(i)))

    print("--all")
    result = await repo.all()
    for item in result:
        print(item)

    filters = {'status': Status.NEW, 'priority': 1}
    for t in await repo.all_filter(filters):
        print(t)


# Run the main function in an event loop
asyncio.run(main())
