a  = 3
b = 4

if (a<b):
	print('a is smaller than b')
# a = 1
# b = 2
# print(a+b)
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd 

# a = [[1,2],[3,4],[5,6]]
# b = [[6,5],[4,3],[2,1]]
# a1 = pd.DataFrame(a,columns=['a','b'],index=[1,2,3])
# b1 = pd.DataFrame(b,columns=['b','a'],index=[1,3,5])
# print(a1)
# print(b1)
# print(a1+b1)

#b = [6,5,4,3,2,1]
# print(a+b)
# a1 = np.array(a)
# b1 = np.array(b)
# print(a1+b1)
# a2 = pd.Series(a,index=[1,2,3,4,5,6])
# b2 = pd.Series(b,index=[8,7,6,5,4,3])
# print(a2+b2)


# y = np.random.randn(100)
# plt.hist(y)
# plt.xlabel('x')
# plt.ylabel('rainings')
# plt.show()
# a = [1,1,-1,1,-1,1,2,-3,4,-5,-2,1,3,4]
# s = 0
# for i in a:
# 	if i>0:
# 		s += i
# print(s)

#b = [i for i in a if i>0]
#print(b)
# print(sum(b))
#b = [2,2,2,2,2]

# a1 = np.array(a,dtype=np.int16)
# print(sum(a1[a1>0]))
#print(sum(a1>0))
# b1 = np.array(b,dtype=np.float32)
# c1 = a1+b1
# print(c1.dtype)
# b1 = np.array(b)
# print(a1/b1)

#method 3
# for i in open('test0517','r'): 
# 	print(i.strip())

#method 1
# with open('test0517','r') as f:
# 	for i in f:
# 		print(i.strip())

# method 2
# f = open('test0517','r')
#data = f.readlines()
# for i in f:
# 	print(i.strip())


# method 1 
# with open('test0517','w') as f:
# 	for i in range(10):
# 		f.write('Hello {}\n'.format(i))

# method 2
# f = open('test0517','a')
# for i in range(10):
# 	f.write('Hello {}\n'.format(i+10))
#f.close()
# f.write('hi')

#f.close()

#f.write('hi')

# correct_number = 4

# while True:
#     try:
#         guess = int(input('Guess a number : '))
#         if (guess == correct_number):
#             print("good guess!")
#             break
#         else:
#             guess = int("a")
#     except:
#     	pass    
# a = [1,2,3,"a",4,5,"b",6,7,"c"]
# b = []
# for i in a:
# 	try:
# 		if (i > 0): b.append(i)
# 	except:
# 		pass
# print(b)
# try:
# 	a = input('Enter a :')
# 	b = input('Enter b :')
# 	print('a+b = {}'.format(int(a)+int(b)))
# except:
# 	print('a and b must be integers')

# import sqlite3

# db = sqlite3.connect('db0517')

#db.execute('create table student(name text, ranking int)')
# db.execute('insert into student(name,ranking) values(?,?)',('Ally',2))
# db.execute('insert into student(name,ranking) values(?,?)',('Belinda',1))
# db.execute('insert into student(name,ranking) values(?,?)',('Jane',5))
# db.execute('insert into student(name,ranking) values(?,?)',('Alfred',3))
# db.execute('insert into student(name,ranking) values(?,?)',('John',4))

# db.execute('update student SET ranking=? where name=?',(2,'Belinda'))
# db.execute('update student SET ranking=? where name=?',(1,'Ally'))

# db.execute('delete from student where ranking=5')
# db.commit()

# data = db.execute('select * from student order by ranking')

# with open('subjects0517.txt','w') as f:
#  	for r in data:
#  		f.write("{}\t{}\n".format(r[0],r[1]))

# class Animal():

# 	def talk(self):
# 		print('talk like an animal')

# class Dog(Animal):

# 	def talk(self):
# 		print('woooooof')

# class Cat(Animal):

# 	def talk(self):
# 		print('meooooow')

# def animal_talk(a):
# 	a.talk()

# dog1 = Dog()
# cat1 = Cat()

# animal_talk(dog1)
# animal_talk(cat1)

# dog1.talk()
# cat1.talk()

# class Employee():

# 	EmpCount = 0

# 	def __init__(self, name, salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.EmpCount += 1

# 	def __del__(self):
# 		print('{} left the company'.format(self.name))
# 		Employee.EmpCount -= 1

# 	def displayEmpCount(self):
# 		print('No of employees = {}'.format(Employee.EmpCount))

# 	def displayEmpDetail(self):
# 		print('{} salary is {}'.format(self.name,self.salary))

# class FullTimeStaff(Employee):

# 	def __init__(self,name,salary,leave):
# 		super().__init__(name,salary)
# 		self.leave = leave

# 	def displayEmpDetail(self):
# 		print('{} salary is {} and leave is {}'.format(self.name,self.salary,self.leave))

# class PartTimeStaff(Employee):

# 	def __init__(self,name,hrrate):
# 		self.name = name
# 		self.hrrate = hrrate

# 	def __del__(self):
# 		print('{} left the company'.format(self.name))
	

# 	def displayEmpDetail(self):
# 		print('{} hourly rate is {}'.format(self.name,self.hrrate))


# emp1 = FullTimeStaff('Ally',5000,21)
# emp2 = PartTimeStaff('Belinda',100)
# emp3  = FullTimeStaff('Jane',8000,18)
# emp1.displayEmpDetail()
# emp1.displayEmpCount()
# emp2.displayEmpDetail()
# del emp2
# emp1.displayEmpCount()
# del emp3
# emp1.displayEmpCount()

# class Rectangle():

# 	def __init__(self,length=10, width=10):
# 		self.length = length
# 		self.width = width

# 	# def __del__(self):
# 	# 	print('I am destroyed')

# 	def WhoamI(self):
# 		print('I am a Rectangle')

# 	def compute_area(self):
# 		print('Area = {}'.format(self.length*self.width))

# class Square(Rectangle):

# 	def __init__(self,length=10):
# 		super().__init__(length,length)

# 	def WhoamI(self):
# 		print('I am a Square')

# 	def compute_perimeter(self):
# 		print('Perimeter = {}'.format(4*self.length))

# rect1 = Rectangle(10,20)
# rect1.WhoamI()

# sq1 = Square(20)
# sq1.compute_area()
# sq1.compute_perimeter()
# sq1.WhoamI()


# rect1 = Rectangle(10,20)
# rect1.compute_area()
# del rect1

# class Person():
# 	name = ''
# 	age = 0

# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age

# 	def __del__(self):
# 		print('{} is destroyed'.format(self.name))

# 	def talk(self):
# 		print('{} talk like a person'.format(self.name))

# p1 = Person('Ally',30)
# p2 = Person('Belinda',40)

# p1.name = 'Ally'
# p1.age = 30
# p2.name = 'Belinda'
# p2.age = 40

# print('{} age is {}'.format(p1.name,p1.age))
# p1.talk()

# class Person():

# 	def __init__(self,name='Ally',age=30):
# 		self.name = name
# 		self.age = age

# 	def talk(self):
# 		print('{} talk like a person'.format(self.name))

# p1 = Person()
# p2 = Person('Belinda',25)
# p3 = Person(age =30, name='Jane')
# p1.name ='Ally'
# p2.name ='Belinda'

# p1.age = 30
# p2.age = 25

# print('{} age is {}'.format(p1.name,p1.age))

# p1.talk()
# p2.talk()
# p3.talk()

# def f(n):
# 	a =[]
# 	for i in range(n):
# 		a.append(i**2)
# 	return a

# def f(n):
# 	for i in range(n):
# 		yield i*i

# for i in f(10):
# 	print(i)

# print(f(10))

# def f2(n):
# 	for i in range(n):
# 		yield i**2

# for i in f2(10):
# 	print(i)

# a = 'Today is a great day'
# b = a.split()
# print(b)

# a = [i[-1] for i in b]
# print(a)
# c = []
# for i in b:
# 	c.append(i[0])
# print(c)

# a = []
# for i in range(10):
# 	if i*i%2 ==0: continue
# 	a.append(i*i)
# print(a)

a = (i*i for i in range(10) if not(i*i%2==0))
# for i in a:
# 	print(i)
#print(sum(a))


# c = [i[0] for i in b ]
# print([i[0] for i in b ])
# a = []
# for i in range(11):
# 	if i%2 ==0: 
# 		a.append(i*i)

# print(a)

# a = [i*i for i in range(38) if not(i%3==0 or i%5==0)]
# b = (i*i for i in range(38) if not(i%3==0 or i%5==0))

# print(sum(a))
# print(sum(b))

# import numpy as np 
# import matplotlib.pyplot as plt 

# x = np.linspace(0,4*np.pi,200)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()


# import random

# print(random.randint(1,6))
#from mypkg0516 import mylib0516 as m1
# import mypkg0516.mylib0516 as m1

# print(m1.min(4,5,6,2,7,8))

# import math as m
# from math import sin,pi,cos
# from time import sleep

# print(sin(pi/2))
# sleep(5)
# print(cos(pi/2))

# def f(a,b,*c):
# 	print(a)
# 	print(b)
# 	print(c)

# f(2,4,4,5,7,8,10,2,3)

# a = [1,2,3,4,5,6]
# f = lambda x: x%3
# print(list(filter(f,a)))

# f = lambda x,y:10*x+y
# x = [0,1,2,3]
# y = [2,4,6,8]
# print(list(map(f,x,y))

# def m(a,*b):
# 	min = a
# 	for i in b:
# 		if i<min: min=i
# 	return min

# def s(a,b,*c):
# 	sum = a+b
# 	for i in c:
# 		sum += i
# 	return sum

# print(min(10,21,6))

# def grocery(order):
# 	discount = 25 if order > 200 else 0
# 	discount_amt = order*discount/100
# 	tax = 0.07*(order*(1-discount/100))
# 	return discount_amt, tax

# a,b = grocery(350)
# print('discount is {:0.1f} and tax is {:0.1f}'.format(a,b))

# def fare(distance):
# 	booking = 3
# 	start = 3
# 	cost = 0.5
# 	fare = cost*distance+start+booking
# 	return fare

# d = 5
# print(fare(5))

# def f(x,y):
# 	return x*x+3*y,x*x*x

# (a,b) = f(3,2)
# print(a,b)
# def f(x,y):
#     return 10*x+y
# g = lambda x,y:10*x+y


# print(g(3,2))

# a = [4,3,5,7,8]

# def f(x):
# 	return x*x

# print(list(map(lambda x: x*x,a)))



# g = lambda x:x*x*x
# print(g(2))

# def f2(f1):
# 	a = 3
# 	return f1(a)

# print(f2(lambda x:x*x)) 

# print(f(1,3))

# a =['Ally','Belinda','Jane']
# b = [170,160,165]
# c = [60,55,58]

# d = zip(a,b,c)
# print(list(d))
#print(list(c))
# for i,j,k in a,b,c:
# 	print(i,j,k)
# 	name=a[i]
# 	height=b[j]
# 	weight=c[k]
# 	print('{} height is {} and weight is {}'.format(name,height,weight))

# for i,name in enumerate(a):
# 	height = b[i]
# 	print("{}'s height is {}".format(name,height))

# primes = []
# for n in range(1,101):
# 	for divisor in range(2, n):
# 		if n%divisor == 0:break
# 	else: 
# 		primes.append(n)

# print(primes)
# a = []
# for i in range(11):
# 	a.append(i*i)

# print(a)

# for i in range(10):
# 	if i == 4: break
# 	print(i)
# else:
# 	print('no break')

# a = 0
# b = 1

# while (a<100):
# 	a,b=b,a+b
# 	print(a)

# a = 1

# while (a<10):
# 	print(a)
# 	a += 1
# else:
# 	print('run smoothly')
# grade  = input('What is your grade')
# #grade  = 'A'

# if grade == 'A':
#     print('Excellent')
# elif grade == 'B':
#     print('Well done')
# elif grade == 'C':
#     print('Work harder next time')
# else:
#     print('I dont know your grade')

# order = 50
#
# discount = 25 if order > 100 else 0
#
# print(discount)

# a = 4
# b = 4

# if (a<b): 
# 	print('a is smaller than b')
# elif (a>b) :
# 	print('a is larger than b')
# else:
# 	print('a is same as b')

# a = {3,4,'hi',10,9,2}
# b = tuple(a)
# c = list(b)
# print(dir(a))
# b = {3,4,19,23,1}
# c = {19,3}
# print(19 in c)

# a = {'a':1,'b':4,'c':9}
# b = {'d':5,'e':6}
# a.update(b)
# print(a)
# del a['c']
# print(a)
# a = (4,5,2,6,7,6,8,2,7)
# b = (4,5,7,8,10)
#print(a+b)
# print(min(a))
#print(b*2)
# a =['A','C','C','A','T','T','G','A','C','A']
# print(a.count('A'))
# print(a.index('T'))
# b = a.copy()
# b.remove('G')
# b.insert(3,'A')
# b.reverse()
# print(b)
#a = [4,5,2,6,7,6,8,2,7]
#a.reverse()
# a.sort()
# b = a.copy()
# b.sort()
# print(b)
# print(a)
#print(sorted(a))
#print(a.count(6))
# b = [1,2,3,4,5,6,7,8,9]
# print(a+b)
# print(a*2)
# print(a+[3])

# b = a
# c = a.copy()
# b.append(99999)
# print(b)
# print(c)
# print(a)

# a.append(99999)
# print(a)
# a.pop()
# print(a)
# a.insert(2,88888)
# print(a)
# a.remove(7)
# print(a)
# del a[0:3]
# print(a)
# print(data.index(6))
# print(2 in data)
# print(9 in data)
# country ="France"
# capital ="Paris"
# print('The capital of {} is {}'.format(country,capital.upper()))

# a = 'Hello'
# b = 'Alfred'
# print('{1}, Mr {0}, How are you today?'.format(a,b))
#a = 'atgcaattgcaactagcctaattagccca'
# a = 'angch@tertiaryinfotech.com'.split('@')
# b = "--------".join(a)
# a = '      hello               '.upper().lstrip()
# b = '         WORLD'.replace('WORLD','ALFRED').strip()
#print(a.count('gc'))
#print(a.find('gc',9))