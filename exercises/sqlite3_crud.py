import sqlite3

db= sqlite3.connect('test.db')

# Create table
# db.execute('CREATE TABLE student (name text, rank int)')

# Insert data
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Ally',1))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Belinda',2))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Jane',3))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Alfred',4))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('John',5))

# Update data
db.execute('UPDATE student SET rank=? WHERE name=?',(1,'Alfred'))
db.execute('UPDATE student SET rank=? WHERE name=?',(2,'Ally'))
db.execute('UPDATE student SET rank=? WHERE name=?',(3,'Belinda'))
db.execute('UPDATE student SET rank=? WHERE name=?',(4,'John'))
db.execute('UPDATE student SET rank=? WHERE name=?',(5,'Jane'))

# Delete data
db.execute('DELETE FROM student WHERE rank = 5')
db.commit()

# Read data
items = db.execute('SELECT * FROM student order by rank')

for student in items:
    print(student)
