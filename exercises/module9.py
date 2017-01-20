# Python Essential Training
# Module 9: Database
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

import sqlite3

# Create/Link to database
db= sqlite3.connect('test.db')

# Create table
db.execute('CREATE TABLE student(name text,rank int)')
db.commit()

# Populate data
db.execute('INSERT INTO student (name, rank) values (?,?)',('Ally',1))
db.execute('INSERT INTO student (name, rank) values (?,?)',('Belinda',2))
db.execute('INSERT INTO student (name, rank) values (?,?)',('Jane',3))
db.execute('INSERT INTO student (name, rank) values (?,?)',('Steven',4))
db.commit()

# Update data
# db.execute('UPDATE student SET rank=? WHERE name=?',(2,'Ally'))
# db.execute('UPDATE student SET rank=? WHERE name=?',(1,'Belinda'))

# Delete data
#db.execute('DELETE FROM student WHERE rank=4')

# Read data
list = db.execute('SELECT * FROM student ORDER BY rank')

for i in list:
	print(i)

