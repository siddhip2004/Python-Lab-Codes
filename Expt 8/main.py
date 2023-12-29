import sqlite3

conn = sqlite3.connect('siddhi1.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        id INTEGER PRIMARY KEY ,
        name TEXT,
        age INTEGER,
        branch TEXT
    )
''')
conn.commit()

def enroll(id, name, age, branch):
    cursor.execute('INSERT INTO Student (id, name, age, branch) VALUES (?, ?, ?, ?)', (id, name, age, branch))
    # conn.commit()

def dis_students():
    cursor.execute('SELECT * FROM Student')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def updateinfo(Id, age, branch):
    cursor.execute('UPDATE Student SET age=?, branch=? WHERE id=?', (age, branch, Id))
    conn.commit()

def delete(Id):
    cursor.execute('DELETE FROM Student WHERE id=?', (Id,))
    conn.commit()

print("After enrolling")
enroll(123,'XYZ', 19, 'Computer')
enroll(456,'ABC', 13, 'It')
dis_students()
print("\n")


print("After updating info")
updateinfo(456, 20, "Computer")
dis_students()
print("\n")

print("After Deleting")
delete(123)
dis_students()
print("\n")

conn.close()
