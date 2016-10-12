# Numpy and Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# fake data
np.random.seed(937)
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
fs = 10  # fontsize

# demonstrate how to toggle the display of different elements:
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6, 6))
axes[0, 0].boxplot(data, labels=labels)
axes[0, 0].set_title('Default', fontsize=fs)

axes[0, 1].boxplot(data, labels=labels, showmeans=True)
axes[0, 1].set_title('showmeans=True', fontsize=fs)

axes[0, 2].boxplot(data, labels=labels, showmeans=True, meanline=True)
axes[0, 2].set_title('showmeans=True,\nmeanline=True', fontsize=fs)

axes[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axes[1, 0].set_title('Tufte Style \n(showbox=False,\nshowcaps=False)', fontsize=fs)

axes[1, 1].boxplot(data, labels=labels, notch=True, bootstrap=10000)
axes[1, 1].set_title('notch=True,\nbootstrap=10000', fontsize=fs)

axes[1, 2].boxplot(data, labels=labels, showfliers=False)
axes[1, 2].set_title('showfliers=False', fontsize=fs)

for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

fig.subplots_adjust(hspace=0.4)
plt.show()


# demonstrate how to customize the display different elements:
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12,
                  linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6, 6))
axes[0, 0].boxplot(data, boxprops=boxprops)
axes[0, 0].set_title('Custom boxprops', fontsize=fs)

axes[0, 1].boxplot(data, flierprops=flierprops, medianprops=medianprops)
axes[0, 1].set_title('Custom medianprops\nand flierprops', fontsize=fs)

axes[0, 2].boxplot(data, whis='range')
axes[0, 2].set_title('whis="range"', fontsize=fs)

axes[1, 0].boxplot(data, meanprops=meanpointprops, meanline=False,
                   showmeans=True)
axes[1, 0].set_title('Custom mean\nas point', fontsize=fs)

axes[1, 1].boxplot(data, meanprops=meanlineprops, meanline=True, showmeans=True)
axes[1, 1].set_title('Custom mean\nas line', fontsize=fs)

axes[1, 2].boxplot(data, whis=[15, 85])
axes[1, 2].set_title('whis=[15, 85]\n#percentiles', fontsize=fs)

for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

fig.suptitle("I never said they'd be pretty")
fig.subplots_adjust(hspace=0.4)
plt.show()
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0,8*np.pi,200)
# y = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x,y,label="sin",color="red",marker="o")
# plt.plot(x,y2,label="cos",color="magenta",marker="^")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('sine and cosine curves')
# plt.legend()
# plt.show()

# a = [4,5,-3,5,-7,2,-9,1,-2,-6,4]
# a1 = np.array(a)
# print(a1[a1>0])

# a = [1,1,1,1]
# b = [2,2,2,2]
#print(a+b)
# a1 = np.array(a)
# b1 = np.array(b)
# print(a1)
# print(b1)
# print(a1+b1)

# Files Input and Output

# with open("tdk.txt","r") as f:
# 	for i in f:
# 		print(i.strip())

# f = open("tdk.txt","r")
# data = f.readlines()
# for i in data:
# 	print(i.strip())

# f.close()


# Method 1
# with open("tdk.txt","w") as f:
# 	for i in range(10):
# 		f.write("Hello {}\n".format(i))

# for i in range(10):
# 	f.write("hello {}\n".format(i+10))

# Method 2		
# f = open("tdk.txt","a")

# for i in range(10):
# 	f.write("hello {}\n".format(i+10))

#f.close()

# for i in range(10):
# 	f.write("hello {}\n".format(i+10))


# try: 
# 	f = open("tdk.txt","r")
# except:
# 	print("file not exist")

#Exceptions

# a = [1,2,3,"a",4,5,"b",6,7,"c"]
# b = []
# for i in a:
# 	try:
# 		if (i > 0): b.append(i)
# 	except:
# 		pass

# print(b)

# try:
# 	print(int('A'))
# except:
# 	print("Can you please enter integer")




# a = [4,-5,-7,3,2,9,-1]
# # compute the sum of all positive numbers
# a1 = np.array(a)
# print(sum(a1[a1>0]))



# Database

# import sqlite3
# db = sqlite3.connect("tdk.db")

# data = db.execute('select * from shift order by shift')

# with open("tdk.txt","w") as f:
# 	for i in data:
# 		f.write("{}\t{}\t{}\n".format(i[0],i[1],i[2]))


# #db.execute('create table shift(shift char, stuff int, duty int)')
# db.execute('insert into shift(shift,stuff,duty) values (?,?,?)',("A",60,1))
# db.execute('insert into shift(shift,stuff,duty) values (?,?,?)',("B",50,0))
# db.execute('insert into shift(shift,stuff,duty) values (?,?,?)',("C",80,1))
# db.execute('insert into shift(shift,stuff,duty) values (?,?,?)',("D",40,0))
# db.commit()

#db.execute('create table filters(length float, width float, freq float)')
# db.execute('insert into filters(length,width,freq) values (?,?,?)',(50,60,200))
# db.execute('insert into filters(length,width,freq) values (?,?,?)',(60,60,300))
# db.execute('insert into filters(length,width,freq) values (?,?,?)',(70,70,400))
# db.execute('insert into filters(length,width,freq) values (?,?,?)',(80,70,500))
#db.execute('update filters set width=? where freq = ?',(95,300.0))
#db.execute('delete from filters where freq = 500.0')

# data = db.execute('select * from shift order by shift')

# for i in data:
# 	print(i)


# Object Oriented Programming
# Inheritance

# class Rectangle():

# 	def __init__(self,length,width):
# 		self.length = length
# 		self.width = width

# 	def area(self):
# 		print("Area = {}".format(self.length*self.width))

# class Square(Rectangle):

# 	def __init__(self,length):
# 		super().__init__(length,length)


# sq1 = Square(10)
# sq1.area()

# class Employee():
# 	EmpCount = 0

# 	def __init__(self,name,salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.EmpCount += 1

# 	def dispEmpCount():
# 		print("# of Employee = {}".format(Employee.EmpCount))

# 	def dispEmpDetails(self):
# 		print("{}'s ID is {} and salary is ${}".format(self.name,self.ID,self.salary))

# class FullTimeStaff(Employee):

# 	def __init__(self,name,salary,leave):
# 		Employee.__init__(self,name,salary)
# 		self.leave = leave

# 	def dispEmpDetails(self):
# 		print("{}'s salary is ${} and leave is {} days".format(self.name,self.salary,self.leave))


# class PartTimeStaff(Employee):

# 	def __init__(self,name,hrrate):
# 		self.name = name
# 		self.hrrate = hrrate

# 	def dispEmpDetails(self):
# 		print("{}'s hourly rate is ${} per hour".format(self.name,self.hrrate))

# emp1 = FullTimeStaff("ally",3000,21)
# emp2 = FullTimeStaff("Belinda",4000,19)
# emp3 = PartTimeStaff("Jane",30)
# Employee.dispEmpCount()

# emp1.dispEmpDetails()
# emp2.dispEmpDetails()
# emp3.dispEmpDetails()

# emp1 = Employee("ally",3000)
# emp2 = Employee("belinda",4000)
# emp3 = Employee("jane",5000)

# Employee.dispEmpCount()
# emp1.dispEmpDetails()
# emp2.dispEmpDetails()
# emp3.dispEmpDetails()
# emp1.dispEmpDetails()


# class Dry_Etching():

# 	def __init__(self,gas_ratio, temperature, presssure):
# 		self.gas_ratio = gas_ratio
# 		self.temperature = temperature
# 		self.presssure = presssure

# 	def etch_rate(self):
# 		return 0.5*self.gas_ratio+1.29*self.temperature-0.6*self.presssure

# etcher1 = Dry_Etching(1.5,600,0.5)
# etcher2 = Dry_Etching(2.0,650,1.5)

# etchrate1 = etcher1.etch_rate()
# print("Etch Rate = {}".format(etchrate1))

# class Rectangle():

# 	def __init__(self,length,width):
# 		self.length = length
# 		self.width = width

# 	def area(self):
# 		print("Area = {}".format(self.length*self.width))

# rect1 = Rectangle(5,9)
# rect2 = Rectangle(6,10)

# rect1.area()
# rect2.area()

# class Person():

# 	def __init__(self,name,height):
# 		self.name = name
# 		self.height = height

# 	def talk(self):
# 		print("{} talk like a person".format(self.name))

# p1 = Person("ally",155)
# p2 = Person("belinda",160)

# p1.talk()
# p2.talk()

# p1.name ="ally"
# p1.height = 155

# p2.name = "belinda"
# p2.height = 160

# print(p2.name)
# print(p2.height)

# Generators

# Generator Expression
# a = (i*i for i in range(20) if (i*i%3 and i*i%5))

# for i in a:
# 	print(i)

# Generator Functions

# def f(x):
# 	a = []
# 	for i in range(x):
# 		a.append(i*i)
# 	yield a

# for i in f(10):
# 	print(i)

# Comprehension

# s = 'Today is a good day'
# s2 = s.split()
# print(s2)
# s3 = [i[-1] for i in s2]
# print(s3)

# a = {i:i*i for i in range(11)}
# print(a)

# a = [i*i for i in range(11) if i*i%3]
# print(a)


# a = []
# for i in range(11):
# 	if i*i%3==0:continue
# 	a.append(i*i)
# print(a)

#modules and packages

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0,4*np.pi,200)
# y = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x,y,'ro')
# plt.plot(x,y2,'g^')
# plt.show()

# import mypkg.mylib as gg

# order = 400
# discount, tax  = gg.grocery(order)
# print("discount = {}".format(discount))
# print("tax = {}".format(tax))

#import math as m
# from math import pi, sin, cos
# import time

# r= 5
# area = pi*r*r

# print(sin(pi/2))
# time.sleep(5)
# print(cos(pi/2))

# # Functions

## lambda function and map

# f = lambda x,y:10*x+y

# x = [0,1,2,3]
# y = [2,4,6,8]

# print(list(map(f,x,y)))

# a = lambda x,y: 10*x+y

# print(a(3,4))

# def f(x,y):
#     return 10*x+y

# a = [1,2,3,4,5]
# b = map(lambda x:x*x,a)
# print(list(b))

# for i in a:
# 	print(f(i))



# def f(x):
# 	return x*x

#print(f(3))


# def sum(a,b,*c):
# 	s = a +b
# 	for i in c:
# 		s = s +i
# 	return s

# def min(*a):
# 	m = a[0]
# 	for i in a:
# 		if i<m:m=i
# 	return m

# print(min(5,6,7,8,3))

# def taxi(distance):
# 	booking = 2.5
# 	starting = 2.5
# 	cost = 5
# 	return booking+starting+distance*cost

# distance = 30
# print("My taxi fare is {}".format(taxi(distance)))

# def grocery(order):
# 	discount = 25 if order > 200 else 0
# 	discount_amt = (discount/100)*order
# 	amt = order - discount_amt
# 	tax = 0.07*amt
# 	return discount_amt,tax

# order = 300
# discount,tax = grocery(order)
# print("Discount = ${:0.2f}".format(discount))
# print("Tax = ${:0.2f}".format(tax))

# def f(x=9,y=6):
# 	return x*x,x*x+3*y

# (a,b) = f(3,4)
# print(a)
# print(b)

# print(f(y=1,x=2))

# For Loop

# primes = []
# for n in range(1,100):
# 	for divisor in range(2, n):
# 		if n%divisor == 0:break
# 	else: 
# 		primes.append(n)
# print(primes)

# for i in range(1,20):
# 	if i == 5:break
# 	print(i)
# else:
# 	print("nothing is broken")

# name = ['ally','belinda','jane']
# height = [164,155,170]

# person = zip(name,height)
#print(list(person))

# for (i,h) in person:
# 	print("{} height is {}cm".format(i,h))

# for index,i in enumerate(name):
# 	h = height[index]
# 	print("{} height is {}cm".format(i,h))

# a = []
# for i in range(1,11):
# 	if i==4:continue
# 	if i==8:break
# 	a.append(i*i)

# print(a)

#a = [4,5,6,2,'hi',4.6]

# for j in range(2,20,3):
# 	print(j)

# While Loop
# a = 0
# b = 1
# while (b<100):
# 	a,b = b,a+b
# 	print(a)

# a = 0

# while a<10:
# 	print(a)
# 	a += 1

# Conditional 

# grade = "D"

# if grade == "A":
# 	print("Excellent!")
# elif grade == "B":
# 	print("Well done!")
# elif grade == "C":
# 	print("Work harder")
# else:
# 	print("Unknown grade")

# a = 10
# b = 8

# c = a if a>b else b

# print(c)

# if (a<b):
# 	print("a is smaller than b")
# elif (a>b):
#     print("a is larger than b")
# else:
# 	print("a is same as b")

#Operators

# a = 4
# a += 6
# print(a)
# print(7//3)

# Set

# a = {3,6,5,8,7,10,12}
# b = {3,6,5,9,11,1}
# print(a | b)
# print(a & b)
# print(a - b)
# print(b - a)
# print(a)
# print(b)
# print(a == b)


# Dictionary

# a = {'ally':165, 'belinda':150,'jane':167}
# b = {'alfred':170}
# a.update(b)
# del a['jane'] 
# print(a)

# Tuple

# a = (4,5,6,7)
# b = (8,3,2,5)
# print(a+b)

# a = (4,5,6,8,2)
# a.reverse()
# print(a)
# print(a[-1])
# print(len(a))
# print(min(a))
# print(max(a))

# List

# a = [4,5,7,9]
# del a[2]
# print(a)

# letters =['A','C','C','A','T','T','G','A','C','A']
# print(letters.count('A'))
# print(letters.index('T'))
# letters2 = letters.copy()
# letters2.remove('G')
# letters2.insert(3,'A')
# letters2.reverse()
# print(letters2)
# a = [4,5,6,2,3] 
# print(len(a))
# print(min(a))
# print(max(a))
# print(sum(a))
#a.sort(reverse=True)
# print(sorted(a))
# print(a)
# b = a 
# c = a.copy()
# a.append(999999)
# print(a)
# print(b)
# print(c)

# a = [4,5,7,8,2,4.5,'hi']
# a.append(999999)
# print(a)
# a.pop()
# a.pop(2)
# a.insert(2,888888)
# a.remove('hi')
# print(a)
# print(a.index(8))
# print(5 in a)
# print(19 in a)




# Strings
# country ="France"
# capital ="Paris"
# print("The capital of {} is {}".format(country.upper(),capital.lower()))
# a = "alfred"

# print("My name is {}".format(a))

# dna = "attgcaatgcattagcaatagaggcata"
# print(dna.find("ca"))
# print(dna.count("ca"))

# a = "abc@epcos.com"
# b = a.split("@")
# print(b)
# c = "and ".join(b)
# print(c)
# a = "Hello          ".upper().strip()
# b = "World".lower().replace('world','Alfred')
# print(a+" "+ b)

# Numbers
# a = 1.5498543985490
# b = 4.485094805948958

# print("{:.2f}+{:.2f}={:.2f}".format(a,b,a+b))