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

# 	def __init__(self,name, salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.empCount = Employee.empCount + 1

# 	def __del__(self):
# 		Employee.empCount = Employee.empCount - 1

# 	def dispEmpCount(self):
# 		print("Employee count is ",Employee.empCount)
		
# 	def dispEmpDetail(self):
# 		print("{} salary is ${}".format(self.name,self.salary))

# class FullTimeStaff(Employee):

# 	def __init__(self,name,salary,leave):
# 		super().__init__(name,salary)
# 		self.leave = leave

# 	def dispEmpDetail(self):
# 		print("{} salary is ${} and leave is {}days".format(self.name,self.salary,self.leave))

# class PartTimeStaff(Employee):

# 	def __init__(self,name,hrrate):
# 		super().__init__(name,0)
# 		self.hrrate = hrrate
# 		Employee.empCount = Employee.empCount - 1

# 	def __del__(self):
# 		pass

# 	def dispEmpDetail(self):
# 		print("{} hourly rate is ${} per hour".format(self.name,self.hrate))

# # Testing
# ally = FullTimeStaff("Ally",4000,21)
# belinda = FullTimeStaff("Belinda",4000,21)
# jane = PartTimeStaff("Jane",200)
# steve = PartTimeStaff("Steve",200)
# ally.dispEmpCount()
# del belinda
# del steve
# ally.dispEmpCount()


# Polymerism
# class Animal():

# 	type = "animal"

# 	# color = "white"
# 	# legs = 4

# 	def __init__(self,color,legs):
# 		self.color = color
# 		self.legs = legs

# 	# def __del__(self):
# 	# 	print("i am destroyed")

# 	def talk(self):
# 		print("talk like an animal")

# class Dog(Animal):

# 	def __init__(self,color,name):
# 		super().__init__(color,4)
# 		self.name = name
	
# 	def talk(self):
# 		print("{} woof woof woof".format(self.name))

# class Cat(Animal):

# 	def __init__(self,color,name):
# 		super().__init__(color,4)
# 		self.name = name
	
# 	def talk(self):
# 		print("{} meow meow meow".format(self.name))

# d1 = Dog("white","ally")
# c1 = Cat("black","belinda")

# def sound(any):
# 	any.talk()

# sound(d1)
# sound(c1)
	




