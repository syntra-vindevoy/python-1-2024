import sqlite3

# Connect to the SQLite database (or create it)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER
)
''')

# Insert data
cursor.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', ('John Doe', 'john@example.com', 28))
conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print('Users:', rows)

# Update data
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (30, 'John Doe'))
conn.commit()

# Delete data
#cursor.execute('DELETE FROM users WHERE name = ?', ('John Doe',))

#conn.commit()

# Close the connection
cursor.close()
conn.close()
