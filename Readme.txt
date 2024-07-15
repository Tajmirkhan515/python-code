I want to move all my Python code into this repository, where I will cover all the main topics and concepts in Python.

  <===========Code one: file name sqliteDatabaseCode.py=============>


=>The simple steps to creation and connection with sqlite3 database 

 step 1: 
         import sqlite3

 step 2: Connect to the database (or create it if it doesn't exist)
         
         connection = sqlite3.connect('school.db')

 step 3:  Create a cursor object to interact with the database
           cursor=connection.cursor()


 step 4:  create a table
          cursor.execute(""" create table if not exists students(
               id Integer primary key,
               first Text,
               last Text,
               age integer,
               semester Text
               )
               """)

Step 5: Insert data into students table
 	cursor.execute("""
	insert into students (first, last, age, semester) values ('ali', 'khan', 23, 'bs4'),
               ('taj', 'khan', 23, 'bs4'),
               ('kashi', 'khan', 23, 'bs4'),
               ('ali', 'muhmmad', 23, 'bs4'),
               ('hasn', 'ali', 23, 'bs4')
	""")
 
Step 6: retrieve data 
        cursor.execute("""
	 select * from students where last='khan'
	""")
	rows=cursor.fetchall()
	print(rows)
	connection.close()

