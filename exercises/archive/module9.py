# Python Essential Training
# Module 9: Database
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

import sqlite3

# db = sqlite3.connect('school.db')

# db.execute('create table student (name text,rank int)')

# Insert Record
# db.execute('insert into student (name,rank) values (?,?)',('Belinda',2))
# db.execute('insert into student (name,rank) values (?,?)',('Jane',3))
# db.execute('insert into student (name,rank) values (?,?)',('Steve',4))
# db.execute('insert into student (name,rank) values (?,?)',('Alfred',5))
# db.commit()

# Update Record
# db.execute('update student set rank=? where name=?',(5,'Steve'))
# db.execute('update student set rank=? where name=?',(4,'Alfred'))

# Delete Record
# db.execute('delete from student where rank=5')

# Read REcord
# list = db.execute('select * from subjects order by subject')

# for i in list:
# 	print(i)


# Challenge
# db = sqlite3.connect('school.db')

# db.execute('create table subjects (subject text,students int, classes int)')

# db.execute('insert into subjects (subject,students, classes) values (?,?,?)',('English',200,10))
# db.execute('insert into subjects (subject,students, classes) values (?,?,?)',('Chinese',50,8))
# db.execute('insert into subjects (subject,students, classes) values (?,?,?)',('Math',80,12))
# db.execute('insert into subjects (subject,students, classes) values (?,?,?)',('Science',80,12))
# db.commit()

# list = db.execute('select * from subjects order by subject')

# for i in list:
# 	print(i)
