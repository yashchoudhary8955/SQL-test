User Registration CRUD Operations
Introduction
This project demonstrates basic CRUD (Create, Read, Update, Delete) operations for a user registration system. The system uses a SQLite database and is implemented in Python.

Table Structure
The project includes a table called "Register" with the following structure:

sql
Copy code
CREATE TABLE IF NOT EXISTS Register (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    DateOfBirth DATE
);
Requirements
Python 3.x
SQLite (or any other preferred SQL database)
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/user-registration-crud.git
cd user-registration-crud
Install dependencies (SQLite should be installed by default):

bash
Copy code
# No additional dependencies
Run the Python script:

bash
Copy code
python registration_crud.py
Follow the on-screen instructions to perform CRUD operations.

CRUD Operations
1. Create Record
Creates a new user registration record.

python
Copy code
create_record('John Doe', 'john@example.com', '1990-01-01')
2. Read Record
Reads a user registration record by ID.

python
Copy code
read_record(1)
3. Update Record
Updates a user registration record by ID.

python
Copy code
update_record(1, 'John Updated Doe')
4. Delete Record
Deletes a user registration record by ID.

python
Copy code
delete_record(1)
