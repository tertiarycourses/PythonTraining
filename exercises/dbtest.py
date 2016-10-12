# import sqlite3

# db = sqlite3.connect('test199.db')

# db.execute('DROP TABLE IF EXISTS student')
# db.execute('CREATE TABLE student (name text, ID int)')

# db.execute('INSERT INTO student (name, ID) VALUES (?,?)',("Kelvin",10000))
# db.execute('INSERT INTO student (name, ID) VALUES (?,?)',("Alfred",10001))
# db.execute('INSERT INTO student (name, ID) VALUES (?,?)',("Sally",10002))
# db.execute('INSERT INTO student (name, ID) VALUES (?,?)',("Cindy",10003))
# db.execute('INSERT INTO student (name, ID) VALUES (?,?)',("Ming",10004))
#db.execute('UPDATE student SET name = ? WHERE ID = ?',("Tony",10001))
#db.execute('DELETE FROM student WHERE ID = 10001')

# db.commit()

# studentlist = db.execute('SELECT * FROM student ORDER BY ID')

# f1 = open("student.txt","w+")

#for row in studentlist:
	#print(row)
#	f1.write(str(row)+"\n")

f2 = open('student.txt','r')
fl = f2.readlines()
for line in fl:
	print(line, end=' ')

