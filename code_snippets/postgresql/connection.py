import psycopg2
import os

def get_column_names_and_types(cursor):
    cursor.execute("""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = 'test2'
    """)
    for column in cursor.fetchall():
        print(column)

def show_table_content(cursor):
    cursor.execute("SELECT * FROM test2")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def get_table_content(cursor, table_name:str="test2"):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows

def rename_column(cursor, old_name:str, new_name:str, table_name:str):
    cursor.execute(f"""
        ALTER TABLE {table_name}
        RENAME COLUMN {old_name} TO {new_name}
    """)
    cursor.connection.commit()

if __name__ == "__main__":

    db_params = {
        "dbname": "test",
        "user": "postgres",
        "password": os.getenv("DB_PASSWORD"),
        # enter your password in the environment variables
        # bash: export DB_PASSWORD="your_password"
        "host": "127.0.0.1",
        "port": "5432"
    }

    with psycopg2.connect(**db_params) as connection, \
         connection.cursor() as cursor:
        
        table_content = get_table_content(cursor, 'test2')
        for row in table_content:
            id, voornaam, achternaam = row
            print(id)
            print(voornaam)
            print(achternaam)

    print("Connection closed.")
