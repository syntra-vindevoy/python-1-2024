import unittest
from typing import TypeVar
from unittest.mock import patch, MagicMock

from src.ToDOList.todo_with_db.domain.todo import Todo
from src.ToDOList.todo_with_db.repository import Repository

T = TypeVar('T', bound=Todo)


class TestRepository(unittest.TestCase):
    @patch('repository.psycopg2.connect')
    def test_all_function(self, mock_connect):
        # Create a mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        # Set the return value of the connect function to our mock connection
        mock_connect.return_value = mock_conn

        # Set the return value of the cursor function to our mock cursor
        mock_conn.cursor.return_value = mock_cursor

        # Define what the fetchall method should return
        mock_cursor.fetchall.return_value = [
            (1, 'Sample Title 1', 'Description 1', None, 1, 0),
            (2, 'Sample Title 2', 'Description 2', None, 2, 0)
        ]

        # Instantiate the repository
        repo = Repository[T](dbname='testdb', user='testuser', password='testpassword', host='localhost', port='5432')

        # Call the all method
        todos = repo.all()

        # Check that the cursor was created and executed the expected query
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM todos")

        # Check that the cursor's fetchall method was called
        mock_cursor.fetchall.assert_called_once()

        # Check that the cursor was closed
        mock_cursor.close.assert_called_once()

        # Verify the results
        self.assertEqual(len(todos), 2)
        self.assertEqual(todos[0].id_todo, 1)
        self.assertEqual(todos[0].title, 'Sample Title 1')
        self.assertEqual(todos[1].id_todo, 2)
        self.assertEqual(todos[1].title, 'Sample Title 2')


if __name__ == '__main__':
    unittest.main()
