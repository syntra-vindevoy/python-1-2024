from datetime import datetime
import pyodbc
from getforcebit import convert_and_process_list, read_and_parse_file


def search_database(item_list):
    # Extract first items for the query and map to second items
    search_items = [item[0] for item in item_list]
    associated_items = {item[0]: item[1] for item in item_list}
    # print("Search Items:", search_items)
    # print("Associated Items:", associated_items)

    # Path to the Access-database
    mdb_path = r"C:/Users/tom_v/OneDrive/Documenten/database/project/controller_l.mdb"

    # ODBC connection
    connection_string = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={mdb_path};"
    )

    try:
        # Connect to the database
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        if search_items:  # Check if the list is not empty
            # Generate placeholders for the search items
            placeholders = ", ".join("?" for _ in search_items)
            query = f"SELECT *, SecondComment FROM NIET WHERE Name IN ({placeholders})"

            # Execute the query
            cursor.execute(query, search_items)
            results = cursor.fetchall()

            # Process the results
            processed_results = []
            for row in results:
                # Use safe stripping to handle possible None values
                name_mnemo = (row[1] or "").strip()
                # Only build mnemo_s if row[3] exists and is not an empty string after stripping
                if row[3] and (row[3] or "").strip():
                    mnemo_s = f"{(row[2] or '').strip()}.{(row[3] or '').strip()}.{(row[4] or '').strip()}"
                else:
                    mnemo_s = "None"

                comment = (row[5] or "").strip() if (row[5] or "").strip() else "None"
                second_comment = (row[0] or "").strip() if (row[0] or "").strip() else "None"
                associated_item = associated_items.get(name_mnemo, "None")
                type_field = (row[6] or "").strip()

                # Collect processed results as a dictionary
                processed_results.append({
                    'name_id': name_mnemo,
                    'KKS': mnemo_s,
                    'Comment': comment,
                    'Second_comment': second_comment,
                    'Type': type_field,
                    'Value': associated_item
                })

            return processed_results
        else:
            print("De lijst met te zoeken items is leeg. Beëindig query.")
            return []  # Return an empty list

    except pyodbc.Error as e:
        print(f"Er is een fout opgetreden: {e}")
        return []  # Return an empty list on error

    finally:
        # Close the connection
        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":
    start = datetime.now()
    words_list = read_and_parse_file("for.dat")
    item_list = convert_and_process_list(words_list)
    results = search_database(item_list)
    end = datetime.now()
    print(f"Time taken: {(end - start).total_seconds()} seconds")
    # Print the processed results
    for row in results:
        print(row)
