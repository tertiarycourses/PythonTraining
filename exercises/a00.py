# Python Essential Training

import mysuperlib as my

order = 300
discount, tac = my.grocery(order)

# import numpy as np
# import pandas as pd 

# a = [1,2,3,4]
# #a2 =[4,3,2,1]
# b = np.array(a,dtype=np.float64)
# print(b.dtype)
# print(b)
#b2 = np.array(a2)
# c = pd.Series(a,index=[1,2,3,4])
# c2 = pd.Series(a2,index = [4,3,2,1])

# print(a+a2)
# print(b+b2)
# print(c+c2)

# a = [3,4,-2,6,8,-4,-3,9]
# b = np.array(a)
# print(b)
# print(b[[1,3]])

# b = np.array(a)
# print(sum(b[b>0]))

# s = 0
# for i in a:
# 	if i>0: s = s + i
# print(s)

# import matplotlib.pyplot as plt

# x = np.linspace(0,10,200)
# y = np.sin(x)
# y2 = np.cos(x)
# y3 = y*y2
# y4 = y*y-y2*y2

# plt.subplot(2,2,1)
# plt.plot(x,y,color='red',label='sine')
# plt.subplot(2,2,2)
# plt.plot(x,y2,color='green',label='cosine')
# plt.subplot(2,2,3)
# plt.plot(x,y3)
# plt.subplot(2,2,4)
# plt.plot(x,y4)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('my plots')
# plt.legend()
# plt.show()

# N = 20
# theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
# radii = 10 * np.random.rand(N)
# width = np.pi / 4 * np.random.rand(N)

# ax = plt.subplot(111, projection='polar')
# bars = ax.bar(theta, radii, width=width, bottom=0.0)

# # Use custom colors and opacity
# for r, bar in zip(radii, bars):
#     bar.set_facecolor(plt.cm.jet(r / 10.))
#     bar.set_alpha(0.5)

# plt.show()
# Numpy
# import numpy as np
# import matplotlib.pyplot as plt

# a = [1,1,1]
# b = [2,2,2]
# print(a+b)
# a1 = np.array(a)
# b1 = np.array(b)
# print(a1/b1)



# Module 11 File Input?/Output

# for i in open('test00.txt','r'): print(i.strip())

# with open('test00.txt','r') as f:
# 	for i in f:
# 		print(i.strip())
# f = open('test00.txt','r')
# text = f.readlines()
# for i in text:
# 	print(i.strip())
# f.close()

# with open('test00.txt','w') as f:
# 	for i in range(10):
# 		f.write('Line {}\n'.format(i))



# for i in open('test00.txt','w'):
# 	write('OK {}\n'.format(i))

# f = open('test00.txt','w')

# for i in range(10):
# 	f.write('Hello {}\n'.format(i+10))

#f.close()
# f.write('The End')

# Module 10 Exception

# try:
# 	print(int("a"))
# except:
# 	print("do not put alphbet in to int")

# correct_number = 5

# while True:
#     try:
#         guess = int(input('Guess a number : '))
#         if (guess == correct_number):
#             print("good guess!")
#             break
#         else:
#             print(int("a"))
#     except:
#     	print("Wrong guess. Try again")

# try:
# 	print(int('A'))
# except:
# 	print('Please use only numbers')

# Module 9 Database 

import sqlite3

db = sqlite3.connect('test23.db')

# # db.execute('create table student(name text,rank int)')

# # db.execute('insert into student(name, rank) values (?,?)',('Belinda',2))
# # db.execute('insert into student(name, rank) values (?,?)',('Jane',3))
# # db.execute('insert into student(name, rank) values (?,?)',('Alfred',4))
# # db.execute('insert into student(name, rank) values (?,?)',('Kelvin',5))
# # db.execute('insert into student(name, rank) values (?,?)',('John',6))

# # db.execute('update student set rank=? where name=?',(6,'Ally'))
# # db.execute('update student set rank=? where name=?',(1,'John'))

# db.execute('delete from student where rank = 6')

# students = db.execute('select * from student order by rank')
# db.commit()

# with open('students.txt','w') as f:
# 	for r in students:
# 		f.write('{}\t{}\n'.format(r[0],r[1]))

# Module 8: Object Oriented Programming (OOP)

# class Employee():
# 	empCount = 0

# 	def __init__(self,name,salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.empCount += 1

# 	def __del__(self):
# 		#print('{} left the company'.format(self.name))
# 		Employee.empCount -= 1

# 	def dispEmpCount():
# 		print('Number of Employees is {}'.format(Employee.empCount))

# 	def dispEmpDetails(self):
# 		print('{} salary is {}'.format(self.name,self.salary))

# class FullTimeStaff(Employee):

# 	def __init__(self,name,salary,leave):
# 		super().__init__(name,salary)
# 		self.leave = leave

# 	def dispEmpDetails(self):
# 		print('{} salary is {} and leave is {}'.format(self.name,self.salary,self.leave))

# class PartTimeStaff(Employee):

# 	def __init__(self,name,hrrate):
# 		self.name = name
# 		self.hrrate = hrrate

# 	def __del__(self):
# 		pass

# 	def dispEmpDetails(self):
# 		print('{} hourly rate is {}'.format(self.name,self.hrrate))

# emp1 = FullTimeStaff('Ally',5000,21)
# emp2 = FullTimeStaff('Belinda',4000,18)
# emp3 = PartTimeStaff('Jane',100)

# Employee.dispEmpCount()
# emp1.dispEmpDetails()
# emp2.dispEmpDetails()
# emp3.dispEmpDetails()

# del emp2
# del emp3 
# Employee.dispEmpCount()

# emp1 = Employee('Ally',5000)
# emp2 = Employee('Belinda',6000)
# emp3 = Employee('Jane',4500)

# Employee.dispEmpCount()
# emp1.dispEmpDetails()
# emp2.dispEmpDetails()
# emp3.dispEmpDetails()

# del emp2
# Employee.dispEmpCount()


# class Rectangle():

# 	def __init__(self,length, width):
# 		self.length = length
# 		self.width = width

# 	def area(self):
# 		return self.length*self.width

# class Square(Rectangle):

# 	def __init__(self,length):
# 		super().__init__(length,length)

# sq1 = Square(10)

# print(sq1.area())

# r1 = Rectangle(10,20)
# print(r1.area())

# r2 = Rectangle(5,6)
# print(r2.area())

# del r1
# del r2


# class Person():

# 	def __init__(self,a,b):
# 		self.name = a
# 		self.height = b

# 	def walk(self):
# 		print('walk like a person')

# class Lady(Person):

# 	def walk(self):
# 		print('{} walk like a lady'.format(self.name))

# 	def dance(self):
# 		print('{} dance like a butterfly'.format(self.name))

# class Man(Person):

# 	def __init__(self,name,height,weight):
# 		super().__init__(name,height)
# 		self.weight = weight

# 	def walk(self):
# 		print('{} walk like a man'.format(self.name))

# lady1 = Lady('Ally',160)
# man1 = Man('Alfred',170,70)

# print(lady1.name)
# print(lady1.height)
# lady1.walk()
# lady1.dance()

# print(man1.name)
# print(man1.height)
# print(man1.weight)
# man1.walk()





# p1 = Person('Ally',160) 
# p2  = Person('Belinda',166) 

# print('{} height is {}'.format(p1.name,p1.height))
# print('{} height is {}'.format(p2.name,p2.height))

# p1.walk()
# p2.walk()


# Module 6 Comprehension and Generators

# Generator
# a = (i*i for i in range(10))

# for i in a:
# 	print(i)

# for i in range(10):
# 	print(i)

# Compreshension
# a = [i*i for i in range(100000)]
# print(a)

# a = 'Today is a good day and nice day'
# b = a.split()
# print(b)

# set_compreshension = {word[0] for word in b}
# print(set_compreshension)

# list_comprehension = [word[0] for word in b]
# print(list_comprehension)

# a = []
# for i in range(10):
# 	if i%2 == 0:continue
# 	a.append(i*i)
# print(a)

# a = {i:i*i for i in range(10) if not i%2 == 0}
# print(a)
# print(a[3])

# a = [i*i for i in range(10) if not i%2 == 0 ]
# a = [i*i for i in range(20)]
# print(a)
# a = [i*i for i in range(20) if not i%3 == 0 and not i%5==0]
# print(a)

# Module 7 Modules & Packages

# a = [3,4]
# a.append(99)
# print(a)
# a = (3,4)

# person = ['Ally','Belinda','Jane']
# height = [170,160,175]
# weight = [60,55,62]

# a = zip(person,height,weight)
# for (n,h,w) in a:
# 	print('{} height is {} and weight is {}'.format(n,h,w))

#print(list(a))
# for i,name in enumerate(person):
# 	h = height[i]
# 	print('{} height is {}'.format(name,h))

# import numpy as np 
# import matplotlib.pyplot as plt 
# import pandas as pd 

# x = np.linspace(0,4*np.pi,200)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()
#import mysuperlib as m
# import mysuperpkg.mysuperlib as m

# order = 300

# discount,tax = m.grocery(order)
# print(discount)
# print(round(tax,2))

#import math as m
# from math import sin,pi
# import random

# a = ['a','b','c']
# print(random.choice(a))

# # import time

# print(sin(pi/2))
# time.sleep(5)
# print('wake up')

# Module 5 Functions

# f = lambda x: x*x

# g = lambda x,y: 10*x+y

#print(f(2))
#print(g(2,4))

# def min(a,*b):
# 	m = a
# 	for i in b:
# 		if i<m: m=i
# 	return m

# def sum(a,b,*c):
# 	s = a+b
# 	for i in c:
# 		s += i
# 	return s

# print(min(9,7,3,5,7))

# def main():
# 	order = 280
# 	a,b = grocery(order)
# 	print('Discount = ${:0.2f} for ${} order'.format(a,order))
# 	print('Tax = ${:0.2f} for ${} order'.format(b,order))

# def grocery(order):
# 	discount = 25 if order > 200 else 0
# 	discount_amt = discount*order/100
# 	tax = 0.07*(order-discount_amt)
# 	return discount_amt,tax

# order = 280
# a,b = grocery(order)
# print('Discount = ${:0.2f} for ${} order'.format(a,order))
# print('Tax = ${:0.2f} for ${} order'.format(b,order))

# print(__name__)
# if __name__ == "__main__":main()

# def f(x=3,y=4):
# 	return x*2+y*3,x*x

# print(f(2,3))

# def fare(distance):
# 	booking_fee = 2.5
# 	starting_price = 3
# 	cost = 1
# 	return booking_fee + starting_price + distance * cost

# distance = 10
# print('My taxi fare is ${}'.format(fare(distance)))

# def f(x):
# 	return x**2

# print(f(5))

# Module 4 Control Structures

# Loop

# For loop

# a = []
# for i in range(1,11):
# 	a.append(i*i)
# print(a)
# for i in range(10,1,-1):
# 	print(i)
# weekdays = ['mon','tues','wed','thurs','fri']

# for day in weekdays:
# 	if day == 'wed': break
# 	print('Weekday is {}'.format(day))

# a = [4,6,8,10]

# for i in a:
# 	print(i)

# While loop
# a = 1
# b = 1
# while (b<200):
# 	a,b = b,a+b
# 	print(a)


# a = 1

# while (a<10):
# 	print(a)
# 	a += 1

# ternary operator
# order = 80

# discount = 25 if order>100 else 0

# print(discount)

# light = 'PURPLE'

# if (light == 'RED'):
# 	print('stop the car')
# elif (light == 'GREEN'):
# 	print('drive the car')
# elif (light == 'ORANGE'):
# 	print('prepare to stop')
# else:
# 	print('traffic light is faulty')

# a = 4
# b = 4

# if (a<b):
# 	print('a is smaller than b')
# elif (a>b):
# 	print('a is larger than b')
# else:
# 	print('a is same as b')

# Module 3 Operators
# a = [4,5,6]
# print(4 not in a)
# a = 1
# a +=  5
#a = a + 5
# print(5 != 8)
# print(5//3)
# Module 2: Data Types
# Set 
# a = {3,6,8,2}
# b = {3,6,10,11}
# print(b - a)
# b = {6,6,2,3,8,8}
# print(a)
# print(b)
# print(a == b)
# print(3 in a)
# print(10 in b)
# Dictionary
# test = {'a':1,'b':2,'c':3}
# print(test)
# print(test['b']) 

# Tuple
# a = (4,5,5,6)
# print(a)
# print(a[0])
# print(min(a))
# List
# letters =['A','C','C','A','T','T','G','A','C','A']
# print(letters.count('A'))
# print(letters.index('T'))
# letters2 = letters.copy()
# letters2.remove('G')
# letters2.insert(3,'A')
# letters2.reverse()
# print(letters2)
# a = [3,4,10,8,9,2]
# a.remove(4)
# a.reverse()
# print(a)
# b = sorted(a)
# a.sort(reverse=True)
# print(b)
# print(a)
# b = a 
# c = a.copy()
# b.append(9999)
# print(b)
# print(c)
# print(a)
# print(a)
# a.append(99999)
# print(a)
# a.pop()
# print(a)
# a.insert(1,88888)
# print(a)
#print(a[2])

# print(a.index(8))
# print(9 in a)
# Strings

# country = "France"
# capital = "Paris"
# print('The capital of {} is {}'.format(country.upper(),capital.lower()))
# a = 'Alfred'
# print('My name is {}'.format(a))

# a ="atgcatagcaacag"
# print(a.count('at'))
# a = "Today is a great day"
# print(a.find("great"))

# a ='angchewhoe@gmail.com'
# b = a.split('@')
# print(b)

# a = "Today has no Haze !!"
# b = a.split()
# print(b)
# c = "--".join(b)
# print(c)
# a ="              hello".upper().strip()
# b = "WORLD".lower().replace('world','Alfred')
# print(a+' '+b)
# Numbers

# a = 4
# b = 5
# c = 6
# d = a + b +c
# print('{1}+{2}+{0}={3}'.format(a,b,c,d))
# a = 1.6
# b = 5.6
# a,b = 3.5555,4.85555
# print('{1:0.2f}+{0:0.2f} = {2:0.2f}'.format(a,b,a+b))
#print(a+b)