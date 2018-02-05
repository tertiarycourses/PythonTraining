# Python Essential Training
# Module 11: File I/O
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017


# Open a file to write or append
# f = open('test.txt','w')

# for i in range(10):
# 	f.write('Hello {}\n'.format(i+10))

#f.close()
#f.write('Hello')

# with open('test.txt','w') as f:
# 	for i in range(10):
# 		f.write('Test {}\n'.format(i))

# with open('test.txt','a') as f:
# 	for i in range(10):
# 		f.write('Test {}\n'.format(i+10))

#f.write('Test again')

# Open a file to read
# try:
# 	f = open('test.txt','r')
# except:
# 	print("check your file name")

# fl = f.readlines()

# for i in fl:
# 	print(i.strip())

# f.close()

# 2nd method: with open
# try:
# 	with open('test.txt','r') as f:
# 		for i in f:
# 			print(i.strip())
# except:
# 	print("check your file name")

# 3rd method: for open
# try:
# 	for i in open('test.txt','r'):
# 			print(i.strip())
# except:
# 	print("check your file name")


# Read CSV file
# import csv
# with open('test.csv', 'r') as f:
# 	fl = csv.reader(f) 
# 	for i in fl:
# 		print(i)

# Challenge

# import sqlite3

# db = sqlite3.connect('school.db')

# students = db.execute('select * from subjects order by subject')
# # print(students)
# # for i in students:
# # 	print(i)

# with open('subjects.txt','w') as f:
# 	for i,j,k in students:
# 		f.write("{}\t{}\t{}\n".format(i,j,k))

