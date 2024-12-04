import asyncio
import datetime

import asyncpg.connection

from src.ToDOList.todo_with_db.domain.statut import Status
from src.ToDOList.todo_with_db.domain.todo import Todo
from src.ToDOList.todo_with_db.repository import Repository
import yaml
import hashlib


def setup_connection_from_yaml():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return asyncpg.connect(
        database=config['db']['database'],
        user=config['db']['username'],
        password=config['db']['password'],
        host=config['db']['host'],
        port=config['db']['port']
    )

def verify_sha1(original_string, hash_to_compare):
    # Hash the original string
    sha1_hash = hashlib.sha1(original_string.encode()).hexdigest()

    # Compare the computed hash to the provided hash
    return sha1_hash == hash_to_compare


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
                      setup_connection_from_yaml())
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
