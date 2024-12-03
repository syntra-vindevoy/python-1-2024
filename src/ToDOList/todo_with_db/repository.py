import logging
from abc import ABC, abstractmethod
from typing import Any, Optional

import asyncpg
from asyncpg import PostgresError
from psycopg2 import DatabaseError

from src.ToDOList.todo_with_db.domain.statut import Status
from src.ToDOList.todo_with_db.domain.todo import Todo

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IRepository[T](ABC):
    @abstractmethod
    async def insert(self, t: T) -> None:
        pass

    @abstractmethod
    async def all(self) -> list[T]:
        pass

    @abstractmethod
    async def get(self, id) -> T | None:
        pass

    @abstractmethod
    async def delete(self, id) -> None:
        pass

    @abstractmethod
    async def delete_all(self) -> None:
        pass

    @abstractmethod
    async def all_filter(self, status: str) -> list[T] | list[Any]:
        pass

    @abstractmethod
    async def update(self, t: T) -> bool:
        pass




class RepositoryException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        logger.error(str(message))


class Repository:
    def __init__(self, connection: asyncpg.connection):
        self.__conn: asyncpg.connection = connection


    async def update(self, todo: Todo) -> bool:
        try:
            await self.__conn.execute("""
                       UPDATE todos
                       SET title = $1, description = $2, due_date = $3, priority = $4, status = $5
                       WHERE id = $6;
                   """, todo.title, todo.description, todo.due_date, todo.priority, todo.status.value, todo.id_todo)
            return True
        except PostgresError as e:
            # Consider logging the exception
            raise RepositoryException(f"Failed to update todo with id {todo.id_todo}: {str(e)}")

    async def insert(self, todo: Todo):
        try:
            todo_id = await self.__conn.fetchval("""
                       INSERT INTO todos (title, description, due_date, priority, status)
                       VALUES ($1, $2, $3, $4, $5) RETURNING id;
                   """, todo.title, todo.description, todo.due_date, todo.priority, todo.status.value)

            return todo_id
        except PostgresError as e:  # Replace with specific exception
            raise RepositoryException(str(e))

    async def all(self) -> list[Todo]:
        try:
            rows = await self.__conn.fetch("SELECT * FROM todos")

            todos = [
                Todo(id_todo=row[0], priority=row[4], due_date=row[3], description=row[2],
                     title=row[1], status=row[5])
                for row in rows
            ]
            return todos
        except PostgresError as e:
            raise RepositoryException(f"Error fetching all todos: {str(e)}")

    async def get(self, id) -> Optional[Todo]:
        try:
            stmt = await self.__conn.prepare("SELECT * FROM todos WHERE id = $1;")
            row = await stmt.fetchrow(id)
            if row is None:
                return None
            return Todo(
                id_todo=row['id'],
                title=row['title'],
                description=row['description'],
                due_date=row['due_date'],
                priority=row['priority'],
                status=row['status']
            )
        except DatabaseError as e:
            raise RepositoryException(f"An error occurred: {e}")

    async def delete(self, id) -> None:
        try:
            await self.__conn.execute("DELETE FROM todos WHERE id = %s;", (id,))
        except PostgresError as e:
            raise RepositoryException(str(e))

    async def delete_all(self) -> None:
        try:
            # assuming async context management is possible
            await self.__conn.execute("DELETE FROM todos;")

        except PostgresError as e:
            raise RepositoryException(f"An unexpected error occurred: {str(e)}")

    async def all_filter(self, filters: dict) -> list[Todo]:
        try:
            query = "SELECT id AS id_todo, title, description, due_date, priority, status FROM todos WHERE "
            conditions = []
            values = []
            for i, (field, value) in enumerate(filters.items(), start=1):
                conditions.append(f"{field} = ${i}")
                # Convert Status enums to their string values
                if isinstance(value, Status):
                    values.append(value.value)
                else:
                    values.append(value)
            query += " AND ".join(conditions) + ";"

            rows = await self.__conn.fetch(query, *values)

            todos = [
                Todo(id_todo=row['id_todo'], title=row['title'], description=row['description'],
                     due_date=row['due_date'], priority=row['priority'], status=row['status'])
                for row in rows
            ]
            return todos
        except Exception as e:
            raise RepositoryException(f"An error occurred: {e}")
