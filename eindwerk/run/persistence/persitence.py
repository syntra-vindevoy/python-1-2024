import psycopg2
import os



def get_table_content(cursor, table_name:str="test2"):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":

    db_params = {
        "dbname": "persistence",
        "user": "postgres",
        "password": os.getenv("DB_PASSWORD"),
        # enter your password in the environment variables
        # bash: 
        # export DB_PASSWORD="your_password"
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
