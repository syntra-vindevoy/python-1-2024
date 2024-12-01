import psycopg2
import os

# Establish a connection to the database
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    # in bash terminal: export DB_PASSWORD="your_password"
    host="127.0.0.1",
    port="5432"
)




cur = conn.cursor()

def get_column_names_and_types():
    cur.execute("""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = 'test2'
    """)

    for column in cur.fetchall():
        print(column)

def show_table_content():
    cur.execute("SELECT * FROM test2")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def get_table_content(table_name:str="test2"):
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    return rows

def rename_column(old_name:str,new_name:str,table_name:str):
    cur.execute(f"""
        ALTER TABLE {table_name}
        RENAME COLUMN {old_name} TO {new_name}
    """)
    conn.commit()

if __name__ == "__main__":
    '''
    get_column_names_and_types()
    show_table_content()
    '''
    table_content = get_table_content('test2') 
    for row in table_content:
        id,voornaam,achternaam = row
        print(id)
        print(voornaam)
        print(achternaam)

cur.close()
conn.close()