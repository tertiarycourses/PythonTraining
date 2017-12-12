#print("Hello World")
# print(a+b)
# a, b = 1,3
# a = 4.545098659048609486
# print("{1:0.2f} + {0:0.2f} = {2:0.2f}".format(a,b,a+b))

# a,b = 3,4
# print("{1:}*{0:}={2:}".format(a,b,a*b))
# # Exercise
# a,b,c = 4.8,5.5,6.5

# print("{1:0.1f}+{2:5.1f}+{0:0.1f}={3:0.1f}".format(a,b,c,a+b+c))

# String
# greet = "Hello".lower().capitalize()
# name = "Alfred".upper()
# height = 170
# print("{}, I am {}. My height is {}cm".format(greet, name,height))

# Exercise - 5 mins
# country = "france"
# capital = "paris"

# print("The capital of {} is {}".format(country.upper(),capital.capitalize()))

# today = "Today is a cloudy day"
# split = today.split(" a ")
# print(split)

# Exercise - 5 mins

# email = "abc@def.com"
# s = email.split("@")
# print("User name is ",s[0])
# print("Domain is ",s[1])

# z = " , ".join(s)
# print(z)

# dna = "atgcaatggccattagccat"
# print(dna.find("cat",11))

# a = 3
# b = a
# b = 4
# print(a)


# List
a = [4,5,6,2]
#a.sort()
# b = sorted(a)
# print(a)
# print(b)

# a.append(10)
# print(a)
# a.pop(2)
# print(a)
# print(max(a))

# a = [3,4,5,5,5]
# print(a.count(5))
# print(a.index(4))
# a.reverse()
# print(a)
# a.insert(2,888)
# print(a)
# a.remove(888)
# print(a)
# print(a)
# c = a.copy()
# b = a 
# b[0] = 5
# c[0] = 6
# print(c)
# print(a)

# letters =['A','C','C','A','T','T','G','A','C','A']
# print(letters.count('A'))
# print(letters.index('T'))

# letters2 = letters.copy()
# letters2.remove('G')
# letters2.insert(3,'A')
# letters2.reverse()
# print(letters2)
# a = [5,6,3,4,'hi']
# print(a.append(8.8))
# Tuple

# a = (5,6,3,4)
# #print(a.append(8.8))
# print(sum(a))

# Dictionary

# person = {'alfred':1,'ally':2}
# print(person['alfred'])

# Set 
# a = {3,4,5,5}
# b = {3,3,4,4,4,5,5}
# print(a == b)
# print(a)
# print(b)

# print(7%5)
# a = 4
# a += 5
# print(a)

# print(1 or 0)
# print(1 and 0)
# print(not 1)

# if then else
# a = 2 
# b = 2
# if a<b:
# 	print("a is smaller than b")
# elif a>b:
# 	print("a is larger than b")
# else:
# 	print("a is same as b")

# order = 300

# discount = 0.25*order if order > 100 else 0
# print(discount)

# grade = input('What is your grade :' )

# if grade == 'A':
# 	print("Excellent!")
# elif grade == 'B':
# 	print("Well Done!")
# elif grade == "C":
# 	print("Work harder")
# else:
# 	print("i don't know your grade")

# a = 1

# while a<10:
# 	print(a)
# 	a += 1

# a,b = 0,1
# while b<100:
# 	print(b)
# 	a,b = b,a+b

# For loop

# for i in ['a',2,3]:
# 	print(i)

# for i in range(10,1,-1):
# 	print(i)

# a = []

# for i in range(11):
# 	a.append(i*i)

# print(a)

# person = ['Alfred','Ally','Jane']
# height = [170,165,155]
# weight = [75,48,60]

# p = zip(person,height,weight)
# # print(list(p))

# for name,height,weight in p:
# 	#print(name,height)
# 	print("{} height is {}cm and weight is {}kg".format(name,height,weight))

# for i,name in enumerate(person):
# 	#print(i,name,height[i])
# 	print("{} height is {}cm".format(name,height[i]))

# for i in range(10):
# 	#if i == 4:continue
# 	if i == 11:break
# 	print(i)
# else:
# 	print("what happen? no break")

# primes = []

# for n in range(1,101):
# 	for divsor in range(2,n):
# 		if n%divsor == 0: break
# 	else:
# 		primes.append(n)

# print(primes)

# def f(x):
# 	return x*x

# print(f(4))

# def fare(distance):
# 	start = 3
# 	booking = 3
# 	cost = 1
# 	return start+booking+cost*distance

# distance = 10
# print("My taxi fare is",fare(distance))

# def f(x):
# 	return x*x,x*x*x

# print(f(4))

# def grocery(order):
# 	dis = 25 if order > 200 else 0
# 	dis_amt = dis*order/100
# 	tax = 0.07*(order-dis_amt)
# 	return dis_amt, tax


# order = 350
# (discount,tax) = grocery(order)
# print("Discount = ${:0.2f}".format(discount))
# print("Tax = ${:0.2f}".format(tax))

# def f(x=2,y=1):
# 	return x+2*y

# print(f(y=7,x=4))

# def sum(a,*b):
# 	sum = a
# 	for i in b:
# 		sum = sum + i
# 	return sum

# print(sum(2,3,6,2,7,8,3))
 
# def min(*a):
# 	m = a[0]
# 	for i in a:
# 		if i<m: m=i
# 	return m

# print(min(-2,3,-6,2,7,8,3))

# def f(**a):
# 	for i,j in a.items():
# 		print(i,j)

#a = {'a':3,'b':5}
# f(a=3,b=5)

# r1 = {'name':'Alfred','height':170,'weight':75}
# r2 = {'name':'Ally','height':160,'weight':45}


# def f(x):
# 	return x*x

# f = lambda x:x*x

# print(f(4))

# def f(x,y):
# 	return 10*x+y

# f = lambda x,y:10*x+y

# print(f(3,4))

# a = map(lambda x:x*x,[4,5,6])
# print(list(a))

# x = [0,1,2,3]
# y = [2,4,6,8]

# a = map(lambda x,y:10*x+y,x,y)
# print(list(a))

# import math
# import time

# a = math.cos(math.pi/2)
# print(a)
# time.sleep(10)
# b = math.sin(math.pi/2)
# print(b)

# a = filter(lambda x:x>4,[5,6,3,2,7])
# print(list(a))

# import datetime

# now = datetime.datetime.now()
# print(now)

# import random

# a = random.randrange(1,6)
# print(a)
# die = random.choice([1,2,3,4,5,6])
# print(die)

# import os
# print(os.getcwd())

# import urllib.request

# with urllib.request.urlopen("http://python.org") as f:
# 	html = f.read()
# print(html)

# import math as m 

# print(m.pi)

# from math import pi, sin

# print(pi)

# import numpy as np 

# a = np.array([3,4,5])
# print(a)

# import matplotlib.pyplot as plt 
# import numpy as np  
# import pandas as pd

# import mymod
# from mypac import mymod

# print(mymod.fare(10))
# print(mymod.grocery(400))


# a = [1,2,3,4,5]
# a = [i*i for i in range(10) if i%3 != 0]
# print(a)

# sent = 'Today is a rainy day'
# words = sent.split()
# print(words)
# l = [i[-1] for i in words]
# print(l)

# a = [i*i for i in range(20) if (i%3 !=0) and (i%5 !=0) ]
# print(a)

# a = (i for i in range(100000000) if i%3 !=0)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# namelist = ['ally','jane','belinda']

# a = (name.capitalize() for name in namelist)

# print(next(a))
# print(next(a))
# print(next(a))

# for i in range(10):
# 	print(i)

# def range2(n):
# 	for i in range(n):
# 		if i%2 == 0:yield i

# for i in range2(10):
# 	print(i)

# def fibo():
# 	a,b = 0,1
# 	while True:
# 		a,b = b,a+b
# 		yield(a)

# f = fibo()
# for _ in range(10):
# 	print(next(f))

# a  = (i for i in range(10000000000))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# def fibo():
# 	a,b = 0,1
# 	while True:
# 		a,b = b,a+b
# 		yield a

# f = fibo()

# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))


class Animal():

	#legs = 4

	def __init__(self,legs):
		self.legs = legs

	def talk(self):
		print("talk like an animal")

	def info(self):
		print("This animal has {} legs".format(self.legs))

class Dog(Animal):

	def __init__(self,color):
		super().__init__(4)
		self.color = color

	def talk(self):
		print("Woof Woof Woof...")

	def info(self):
		print("This {} dog has {} legs  ".format(self.color, self.legs))
		self.talk()

class Cat(Animal):

	def __init__(self,color):
		super().__init__(4)
		self.color = color

	def talk(self):
		print("Meow Meow Meow...")

	def info(self):
		print("This {} cat has {} legs  ".format(self.color, self.legs))
		self.talk()

def playSound(animal):
	animal.info()

d1 = Dog("white")
c1 = Cat("gray")

playSound(c1)

# d1 = Dog("white")
# #d1.talk()
# d1.info()

# a1 = Animal(4)
# a1.talk()
# a1.info()

# class Counter():

# 	count = 0

# 	def increment(self):
# 		self.count = self.count + 1

# 	def incrementByN(self,n):
# 		self.count = self.count + n

# 	def reset():
# 		self.count = 0

# c1 = Counter()
# for i in range(10):
# 	c1.increment()
# print(c1.count)

# class Rect():

# 	def __init__(self,length=10, width=40):
# 		self.length = length
# 		self.width = width

# 	# def __del__(self):
# 	# 	print("i am done")

# 	def area(self):
# 		print("Area = ",self.length*self.width)

# class Square(Rect):

# 	def __init__(self,length):
# 		super().__init__(length,length)

# s1 = Square(10)
# s1.area()


# r1 = Rect(width=10,length=30)
# r1.area()

# class Employee():

# 	empCount = 0

# 	def __init__(self,name,salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.empCount += 1

# 	def __del__(self):
# 		Employee.empCount -= 1

# 	def dispEmpCount(self):
# 		print("No of employee = ",Employee.empCount)

# 	def dispEmpInfo(self):
# 		print("{} salary is {}".format(self.name,self.salary))

# class FullTimeStaff(Employee):
# 	def __init__(self,name,salary,leave):
# 		super().__init__(name,salary)
# 		self.leave = leave

# 	def dispEmpInfo(self):
# 		print("{} salary is {} and leave is {}".format(self.name,self.salary,self.leave))


# class PartTimeStaff(Employee):
# 	def __init__(self,name,hrrate):
# 		super().__init__(name,0)
# 		self.hrrate = hrrate
# 		Employee.empCount -= 1

# 	def __del__(self):
# 		pass

# 	def dispEmpInfo(self):
# 		print("{} hrrate is {}".format(self.name,self.hrrate))

# p1 = FullTimeStaff("Alfred",4000,21)
# p2 = FullTimeStaff("Ally",3000,18)
# p3 = FullTimeStaff("Jane",2000,14)
# p4 = PartTimeStaff("Steve",100)
# p5 = PartTimeStaff("Belinda",200)

# p1.dispEmpCount()
# p1.dispEmpInfo()
# p4.dispEmpInfo()
# del p2
# del p4
# p1.dispEmpCount()



# p1 = Employee("Alfred",4000)
# p2 = Employee("Ally",3000)
# p3 = Employee("Jane",2000)

# p1.dispEmpInfo()
# p1.dispEmpCount()

# del p1
# p2.dispEmpCount()




