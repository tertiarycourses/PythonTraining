# Python Essential Training
# Module 8: Object Oriented Programming
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

# class Person:

# 	def __init__(self,height):
# 		self.height = height

# 	def talk(self):
# 		print("i can talk")

# 	def disp_height(self):
# 		print("Height is {}cm".format(self.height))

# Create Object
# p1 = Person(170)
# p2 = Person(180)

# Access Property and Methods
#p1.height = 170
#print(p1.height)
# p1.disp_height()
# p1.talk()

#p2.height = 180
#print(p2.height)
# p2.disp_height()
# p2.talk()

# Challenge: Class

# class Rectangle():

# 	def __init__(self,length,width):
# 		self.length = length
# 		self.width = width

# 	def area(self):
# 		print("Area = {}".format(self.length*self.width))


# rect1 = Rectangle(10,20)
# rect1.area()

# rect2 = Rectangle(6,12)
# rect2.area()

# rect3 = Rectangle(13,33)
# rect3.area()

# Challenge: Class 
# class Employee():

# 	empCount = 0

# 	def __init__(self,name,salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.empCount += 1

# 	def __del__(self):
# 		Employee.empCount -= 1

# 	def disp_empCount(self):
# 		print("Employee Count = {}".format(Employee.empCount))

# 	def disp_empDetails(self):
# 		print("{} salary is {}".format(self.name,self.salary))

# emp1 = Employee("Ally",4000)
# emp2 = Employee("Belinda",5000)
# emp3 = Employee("Jane",2000)
# emp4 = Employee("Steven",6000)
# emp1.disp_empCount()
# del emp4
# emp1.disp_empCount()

# class Square(Rect):

# 	def __init__(self,length):
# 		super().__init__(length,length)

# s1 = Square(10)
# s1.area()


# Challenge : Inheritance
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


# Polymerism
# class Animal():

# 	#legs = 4

# 	def __init__(self,legs):
# 		self.legs = legs

# 	def talk(self):
# 		print("talk like an animal")

# 	def info(self):
# 		print("This animal has {} legs".format(self.legs))

# class Dog(Animal):

# 	def __init__(self,color):
# 		super().__init__(4)
# 		self.color = color

# 	def talk(self):
# 		print("Woof Woof Woof...")

# 	def info(self):
# 		print("This {} dog has {} legs  ".format(self.color, self.legs))
# 		self.talk()

# class Cat(Animal):

# 	def __init__(self,color):
# 		super().__init__(4)
# 		self.color = color

# 	def talk(self):
# 		print("Meow Meow Meow...")

# 	def info(self):
# 		print("This {} cat has {} legs  ".format(self.color, self.legs))
# 		self.talk()

# def playSound(animal):
# 	animal.info()

# d1 = Dog("white")
# c1 = Cat("gray")

# playSound(c1)


	




