# Python Code Repository

Welcome to the Python Code Repository! This repository covers main topics and concepts in Python, including working with SQLite databases and handling database data using Object-Oriented Programming (OOP) concepts. Below you'll find code examples and explanations for each topic.

## SQLite Database Operations

**File Name: `sqliteDatabaseCode.py`**

This script demonstrates basic SQLite database operations such as creation, connection, table management, data insertion, and data retrieval.

```python
# Import the sqlite3 module
import sqlite3

# Step 1: Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('school.db')

# Step 2: Create a cursor object to interact with the database
cursor = connection.cursor()

# Step 3: Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        first TEXT,
        last TEXT,
        age INTEGER,
        semester TEXT
    )
""")

# Step 4: Insert data into students table
cursor.execute("""
    INSERT INTO students (first, last, age, semester) VALUES
    ('ali', 'khan', 23, 'bs4'),
    ('taj', 'khan', 23, 'bs4'),
    ('kashi', 'khan', 23, 'bs4'),
    ('ali', 'muhmmad', 23, 'bs4'),
    ('hasn', 'ali', 23, 'bs4')
""")

# Step 5: Retrieve data
cursor.execute("""
    SELECT * FROM students WHERE last='khan'
""")
rows = cursor.fetchall()
print(rows)

# Close the connection
connection.close()


