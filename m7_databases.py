# --------------------------------------------------
# Databases => 
# data => ram "memory" => file => A database  
# --------------------------------------------------
# database connectivity => allowing python to communicate with a database 
#database => an organized collection of data => table "student" , table "teachers"
# id  name  age
# 1   John   23 
#DBMS => Database Managment System => it is a software that manages database 
# MYSQL , POSTGRESSQL , SQLITE , MONGODB 
# Responsibilities => store data , retreive , security , backup , transcations 
#Data Integrity => database prevents invalid operation 

#Database => 1- Relational Databases (SQL) => Stored in Tables  SQL Language "Structured Query Language "
#2- NOSQL Database (MongoDB) => Documents , key,value pairs , graphs 
# {
#   "name" : "Marina",
#   "age" :23
# }
#3-In-Memory Databases => Ram 
#=========================================================================
#How python connects to database :
# Method 1 => Built in Modules => sqlite
# Method 2=> External libraries => mysql  need installation 
# Method 3 => ORM framworkds => Django ORM 

#--------------------------------------------------------------
#Components :
#1-  Connection Object (conn) => represent the connection 
#Python => Connection => Database 
# conn = sqlite3.connect("students.db")

#2- Cursor Object => Used for SQL Commands 
#cursor = conn.cursor() => carries queries to the database 

# import sqlite3
# conn = sqlite3.connect("students.db")
# cursor = conn.cursor()

# tables => row(record) column (attribute)
# SQLlite => lightweight , very small , setup , fast  => just a file , no server 

#Creating a Table : 
# cursor.execute("""
#   CREATE TABLE students(
#     id INTEGER PRIMARY_KEY UNIQUE,
#     name TEXT,
#     age INTEGER
#   )
# """
# )
# conn.commit()
# conn.close()
#sql => DDL(Data definition language)=> create ,  alter ,drop  , 
#  DML (Data Manipulation Language )=> data insert , update , delte
#  DQL retreive data => SELECT 
#CRUD OPERATION => C (Create) R(Read) U(Update) D (Delete)

#Insert data 
# cursor.execute("INSERT INTO students VALUES (1,'Marina',22)"
# )
# conn.commit()
# cursor.execute("INSERT INTO students VALUES (2,'John',22)"
# )
# conn.commit()

# cursor.execute("SELECT * FROM students")
# row = cursor.fetchall()
# print(row)

# cursor.execute("UPDATE students Set age=25 WHERE id=2")
# conn.commit()
# row = cursor.fetchall()
# print(row)

#Delete:
# cursor.execute("DELETE FROM students WHERE id=2")
# conn.commit()
# cursor.execute("SELECT * FROM students")
# row = cursor.fetchall()
# print(row)
#=============================================
#ORM => Object Relational Mapping 
# it converts Databse Table -> Python Class
#instead a student table -> class Student
#Table -> class Name 
#Row -> Object
# Column => Attribute 

import sqlite3

print("MODULE 7 HANDS-ON: SQLITE CRUD APPLICATION")
print("-" * 55)

# --------------------------------------------------
# 1. CONNECT TO DATABASE
# --------------------------------------------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

print("\nDatabase connected successfully")


# --------------------------------------------------
# 2. CREATE TABLE
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

print("Table created successfully")


# --------------------------------------------------
# 3. INSERT DATA (CREATE)
# --------------------------------------------------
print("\nInserting records...")

students_data = [
    (1, "Rahul", 85),
    (2, "Anita", 90),
    (3, "John", 78)
]

cursor.executemany("INSERT OR IGNORE INTO students VALUES (?, ?, ?)", students_data)
conn.commit()

print("Records inserted successfully")


# --------------------------------------------------
# 4. READ DATA
# --------------------------------------------------
print("\nReading records...")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)


# --------------------------------------------------
# 5. UPDATE DATA
# --------------------------------------------------
print("\nUpdating record...")

cursor.execute("UPDATE students SET marks = 95 WHERE name = 'Rahul'")
conn.commit()

cursor.execute("SELECT * FROM students WHERE name = 'Rahul'")
print("Updated Record:", cursor.fetchone())


# --------------------------------------------------
# 6. DELETE DATA
# --------------------------------------------------
print("\nDeleting record...")

cursor.execute("DELETE FROM students WHERE name = 'John'")
conn.commit()

cursor.execute("SELECT * FROM students")
print("Remaining Records:")
for row in cursor.fetchall():
    print(row)


# --------------------------------------------------
# 7. ORM STYLE (SIMULATION)
# --------------------------------------------------
print("\nORM STYLE REPRESENTATION")

class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(id={self.id}, name={self.name}, marks={self.marks})"

cursor.execute("SELECT * FROM students")
students = [Student(*row) for row in cursor.fetchall()]
student1 = Student(1,"Marina" ,23)
student11 = Student()

for student in students:
    print(student)


# --------------------------------------------------
# CLOSE CONNECTION
# --------------------------------------------------
conn.close()
print("\nDatabase connection closed")

print("\nLab completed successfully.") 

