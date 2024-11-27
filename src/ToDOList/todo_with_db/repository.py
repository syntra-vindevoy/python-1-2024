import logging
from typing import Any

import psycopg2

from src.ToDOList.todo_with_db.domain.todo import Todo

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RepositoryInterface[T]:
    def insert(self, t: T) -> None:
        pass

    def all(self) -> list[T]:
        pass

    def get(self, id) -> T | None:
        pass

    def delete(self, id) -> None:
        pass

    def delete_all(self) -> None:
        pass

    def all_filter(self, status: str) -> list[Todo] | list[Any]:
        pass

    def update(todo: Todo) -> bool:
        pass

    def close(self):
        pass


class RepositoryException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        logger.error(f"Error connecting to the database: {str(message)}")


class Repository[T:Todo]:

    def __init__(self, dbname: str, user: str, password: str, host: str, port: str):
        try:
            logger.info("Connecting to the database")
            self.__conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            logger.info("Connected to the database successfully")
        except Exception as e:
            raise RepositoryException(f"Error deleting all todos: {str(e)}")

    def update(self, todo: Todo) -> bool:
        try:
            cur = self.__conn.cursor()
            cur.execute("""
                UPDATE todos
                SET title = %s, description = %s, due_date = %s, priority = %s, status = %s
                WHERE id = %s;
            """, (todo.title, todo.description, todo.due_date, todo.priority, todo.status))
            self.__conn.commit()
            cur.close()
            return True
        except Exception as e:
            raise RepositoryException(f"Error deleting all todos: {str(e)}")

    def insert(self, todo: T):
        try:
            cur = self.__conn.cursor()
            cur.execute("""
                   INSERT INTO todos (title, description, due_date, priority, status)
                   VALUES (%s, %s, %s, %s, %s) RETURNING id;
               """, (todo.title, todo.description, todo.due_date, todo.priority, todo.status))
            todo_id = cur.fetchone()[0]
            self.__conn.commit()
            return todo_id
        except Exception as e:
            raise RepositoryException(f"Error deleting all todos: {str(e)}")

    def all(self) -> list[T]:
        try:
            cur = self.__conn.cursor()
            cur.execute("SELECT * FROM todos;")
            rows = cur.fetchall()
            cur.close()
            if rows is not None:
                todos = []
                for row in rows:
                    todos.append(Todo(id_todo=row[0], priority=row[3], due_date=row[3], description=row[2],
                                      title=row[1], status=row[5]))
                return todos
            else:
                return []
        except Exception as e:
            raise RepositoryException(f"Error deleting all todos: {str(e)}")

    def get(self, id) -> T | None:
        try:
            cur = self.__conn.cursor()
            cur.execute("SELECT * FROM todos WHERE id = %s;", (id,))
            row = cur.fetchone()
            cur.close()
            self.__conn.close()
            if row is None:
                return None
            return Todo(id_todo=row[0], priority=row[3], due_date=row[3], description=row[2], title=row[1],
                        status=row[5])

        except Exception as e:
            logger.error(f"Error updating todo: {str(e)}")
            raise RepositoryException(f"Error deleting all todos: {str(e)}")

    def delete(self, id) -> None:
        try:
            cur = self.__conn.cursor()
            cur.execute("DELETE FROM todos WHERE id = %s;", (id,))
            self.__conn.commit()
            cur.close()
        except Exception as e:
            raise RepositoryException(f"Error deleting all todos: {str(e)}")

    def delete_all(self) -> None:
        try:
            cur = self.__conn.cursor()
            cur.execute("DELETE FROM todos;")
            self.__conn.commit()
            cur.close()
        except Exception as e:
            raise RepositoryException(f"Error deleting all todos: {str(e)}")

    def all_filter(self, status: str) -> list[Todo] | list[Any]:
        try:
            cur = self.__conn.cursor()
            cur.execute("SELECT * FROM todos WHERE status = %s;", (status,))
            rows = cur.fetchall()
            cur.close()
            if rows is not None:
                todos = []
                for row in rows:
                    todos.append(
                        Todo(id_todo=row[0], priority=row[3], due_date=row[3], description=row[2], title=row[1],
                             status=row[5]))
                return todos
            else:
                return []
        except Exception as e:
            raise RepositoryException(f"Error deleting all todos: {str(e)}")

    def close(self):
        self.__conn.close()
