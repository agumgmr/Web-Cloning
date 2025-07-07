import sqlite3
import uuid
import os

dir_name = os.path.dirname(os.path.abspath(__file__))

class sql:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(dir_name,'instance', 'data.db'))  # Connect to SQLite database

        # Create a self.cursor object
        self.cursor = self.conn.cursor()

        # Print connection status
        print("Connected to SQLite database")

    # Create table
    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS anilist (
            id TEXT PRIMARY KEY,
            title TEXT,
            alt_title TEXT,
            information TEXT,
            synopsis TEXT,
            char_and_va TEXT,
            staff TEXT,
            statistics TEXT,
            image TEXT
        )
        """

        self.cursor.execute(create_table_query)
        self.conn.commit()
        print("Table created successfully")

    def read_data(self):
        # Read data
        select_query = "SELECT * FROM anilist"
        self.cursor.execute(select_query)

        rows = self.cursor.fetchall()
        
        return rows

    def insert_data(self, title, alt_title, information, synopsis, char_and_va, staff, statistics, image):
        # Insert data
        insert_query = """
        INSERT INTO anilist (id, title, alt_title, information, synopsis, char_and_va, staff, statistics, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        data = (str(uuid.uuid4()), title, alt_title, information, synopsis, char_and_va, staff, statistics, image)

        self.cursor.execute(insert_query, data)
        self.conn.commit()
        print("Data inserted successfully")

    def update_data(self, key, email, username=None):
        # Update data
        if username is None:
            update_query = """
            UPDATE users SET email = ? WHERE id = ?
            """
            data = (email, key)
        else:
            update_query = """
            UPDATE users SET email = ?, username = ? WHERE id = ?
            """
            data = (email, username, key)

        self.cursor.execute(update_query, data)
        self.conn.commit()
        print("Data updated successfully")

    def delete_data(self, key):
        # Delete data
        delete_query = "DELETE FROM users WHERE id = ?"
        data = (key,)

        self.cursor.execute(delete_query, data)
        self.conn.commit()
        print("Data deleted successfully")

    def select_data(self, key):
        # Select data
        select_query = "SELECT * FROM anilist WHERE id = ?"
        data = (key,)

        self.cursor.execute(select_query, data)
        rows = self.cursor.fetchall()
        
        return rows

    # Close the connection
    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("SQLite connection closed")
