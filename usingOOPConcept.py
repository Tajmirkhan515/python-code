import sqlite3

class Person:
    def __init__(self, id_number=-1, first="", last="", age=-1, semester=""):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.semester = semester
        self.connection = sqlite3.connect("school.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first TEXT,
            last TEXT,
            age INTEGER,
            semester TEXT
        )
        """)
        self.connection.commit()

    def insert_student(self):
        self.cursor.execute("""
        INSERT INTO students (first, last, age, semester) VALUES (?, ?, ?, ?)
        """, (self.first, self.last, self.age, self.semester))
        self.connection.commit()

    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM students WHERE id = ?
        """, (id_number,))
        results = self.cursor.fetchone()

        if results:
            self.id_number = results[0]
            self.first = results[1]
            self.last = results[2]
            self.age = results[3]
            self.semester = results[4]
        else:
            print(f"No person found with id {id_number}")

    def __del__(self):
        self.connection.close()

# Example usage
st1 = Person()
st1.first = "John"
st1.last = "Doe"
st1.age = 20
st1.semester = "Fall"
st1.insert_student()

st2 = Person()
st2.load_person(1)
print(st2.first)
print(st2.last)
print(st2.age)
print(st2.id_number)

# Check the data in the database
connection = sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute("""
SELECT * FROM students
""")

rows = cursor.fetchall()
print(rows)

connection.close()
