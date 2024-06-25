import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''CREATE TABLE students (
             student_id INTEGER PRIMARY KEY,
             name TEXT,
             age INTEGER,
             year TEXT,
             major TEXT)''')

c.execute('''CREATE TABLE courses (
             course_id INTEGER PRIMARY KEY,
             course_name TEXT,
             credits INTEGER,
             department TEXT,
             professor TEXT)''')

c.execute('''CREATE TABLE professors (
             professor_id INTEGER PRIMARY KEY,
             name TEXT,
             department TEXT,
             title TEXT,
             email TEXT)''')

c.execute('''CREATE TABLE departments (
             department_id INTEGER PRIMARY KEY,
             name TEXT,
             building TEXT,
             budget INTEGER,
             chair TEXT)''')

c.execute('''CREATE TABLE enrollments (
             enrollment_id INTEGER PRIMARY KEY,
             student_id INTEGER,
             course_id INTEGER,
             semester TEXT,
             grade TEXT,
             FOREIGN KEY(student_id) REFERENCES students(student_id),
             FOREIGN KEY(course_id) REFERENCES courses(course_id))''')

conn.commit()



students = [
    (1, 'Alice', 20, 'Sophomore', 'Computer Science'),
    (2, 'Bob', 21, 'Junior', 'Mathematics'),
    (3, 'ChShilpa', 22, 'Senior', 'Physics'),
    (4, 'Ankan', 23, 'Senior', 'Chemistry'),
    (5, 'Josha', 19, 'Freshman', 'Biology')
]

c.executemany('INSERT INTO students VALUES (?, ?, ?, ?, ?)', students)

courses = [
    (1, 'Introduction to CS', 4, 'Computer Science', 'Dr. Shanket'),
    (2, 'Calculus I', 3, 'Mathematics', 'Dr. Johnson'),
    (3, 'Physics I', 4, 'Physics', 'Dr. Brown'),
    (4, 'Organic Chemistry', 4, 'Chemistry', 'Dr. Shilpa'),
    (5, 'Biology I', 3, 'Biology', 'Dr. Miller')
]

c.executemany('INSERT INTO courses VALUES (?, ?, ?, ?, ?)', courses)

professors = [
    (1, 'Dr. Smith', 'Computer Science', 'Professor', 'shanket@university.edu'),
    (2, 'Dr. Johnson', 'Mathematics', 'Associate Professor', 'johnson@university.edu'),
    (3, 'Dr. Brown', 'Physics', 'Assistant Professor', 'brown@university.edu'),
    (4, 'Dr. Jones', 'Chemistry', 'Professor', 'shilpa@university.edu'),
    (5, 'Dr. Miller', 'Biology', 'Associate Professor', 'miller@university.edu')
]

c.executemany('INSERT INTO professors VALUES (?, ?, ?, ?, ?)', professors)

departments = [
    (1, 'Computer Science', 'Building A', 2000000, 'Dr. Shanket'),
    (2, 'Mathematics', 'Building B', 1500000, 'Dr. Johnson'),
    (3, 'Physics', 'Building C', 1800000, 'Dr. Brown'),
    (4, 'Chemistry', 'Building D', 1700000, 'Dr. Shilpa'),
    (5, 'Biology', 'Building E', 1600000, 'Dr. Miller')
]

c.executemany('INSERT INTO departments VALUES (?, ?, ?, ?, ?)', departments)

enrollments = [
    (1, 1, 1, 'Fall 2023', 'A'),
    (2, 2, 2, 'Fall 2023', 'B'),
    (3, 3, 3, 'Fall 2023', 'A'),
    (4, 4, 4, 'Fall 2023', 'B'),
    (5, 5, 5, 'Fall 2023', 'A')
]

c.executemany('INSERT INTO enrollments VALUES (?, ?, ?, ?, ?)', enrollments)

conn.commit()



def display_table_data(table_name):
    
    c.execute(f'PRAGMA table_info({table_name})')
    col_names = [col[1] for col in c.fetchall()]

    c.execute(f'SELECT * FROM {table_name}')
    rows = c.fetchall()

    print(f"\nTable: {table_name}")
    print(tabulate(rows, headers=col_names, tablefmt='grid'))

table_names = ['students', 'courses', 'professors', 'departments', 'enrollments']

for table in table_names:
    display_table_data(table)
conn.close()
