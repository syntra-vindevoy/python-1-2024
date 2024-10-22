# gewoon een test file

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('car_parts.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for car parts
cursor.execute('''
CREATE TABLE IF NOT EXISTS parts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')
conn.commit()


def add_part(name, brand, quantity, price):
    cursor.execute('''
    INSERT INTO parts (name, brand, quantity, price)
    VALUES (?, ?, ?, ?)
    ''', (name, brand, quantity, price))
    conn.commit()
    print(f"Added part: {name}")


def view_parts():
    cursor.execute('SELECT * FROM parts')
    parts = cursor.fetchall()
    for part in parts:
        print(part)


def update_part(part_id, name, brand, quantity, price):
    cursor.execute('''
    UPDATE parts
    SET name = ?, brand = ?, quantity = ?, price = ?
    WHERE id = ?
    ''', (name, brand, quantity, price, part_id))
    conn.commit()
    print(f"Updated part ID {part_id}")


def delete_part(part_id):
    cursor.execute('DELETE FROM parts WHERE id = ?', (part_id,))
    conn.commit()
    print(f"Deleted part ID {part_id}")


def main():
    while True:
        print("\nCar Parts Database")
        print("1. Add Part")
        print("2. View Parts")
        print("3. Update Part")
        print("4. Delete Part")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter part name: ")
            brand = input("Enter part brand: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_part(name, brand, quantity, price)

        elif choice == '2':
            print("\nCurrent Parts:")
            view_parts()

        elif choice == '3':
            part_id = int(input("Enter part ID to update: "))
            name = input("Enter new part name: ")
            brand = input("Enter new part brand: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            update_part(part_id, name, brand, quantity, price)

        elif choice == '4':
            part_id = int(input("Enter part ID to delete: "))
            delete_part(part_id)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()

# Close the database connection when done
conn.close()
