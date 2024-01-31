import sqlite3
from datetime import datetime


conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

# Create Registration table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Register (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        DateOfBirth DATE
    )
''')
conn.commit()

def create_record(name, email, date_of_birth):
    try:
        cursor.execute('''
            INSERT INTO Register (Name, Email, DateOfBirth)
            VALUES (?, ?, ?)
        ''', (name, email, date_of_birth))
        conn.commit()
        print("Record created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating record: {e}")

def read_record(user_id):
    try:
        cursor.execute('SELECT * FROM Register WHERE ID = ?', (user_id,))
        record = cursor.fetchone()
        if record:
            print("Record found:")
            print(record)
        else:
            print("Record not found.")
    except sqlite3.Error as e:
        print(f"Error reading record: {e}")

def update_record(user_id, new_name):
    try:
        cursor.execute('''
            UPDATE Register
            SET Name = ?
            WHERE ID = ?
        ''', (new_name, user_id))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating record: {e}")

def delete_record(user_id):
    try:
        cursor.execute('DELETE FROM Register WHERE ID = ?', (user_id,))
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting record: {e}")

# testing purpose
create_record('John Doe', 'john@example.com', '1990-01-01')
read_record(1)
update_record(1, 'John Updated Doe')
read_record(1)
delete_record(1)
read_record(1)

# Close the connection when done
conn.close()
