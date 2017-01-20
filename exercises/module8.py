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

class Rectangle():

	def __init__(self,length,width):
		self.length = length
		self.width = width

	def area(self):
		print("Area = {}".format(self.length*self.width))


# rect1 = Rectangle(10,20)
# rect1.area()

# rect2 = Rectangle(6,12)
# rect2.area()

# rect3 = Rectangle(13,33)
# rect3.area()

# Challenge: Class 
class Employee():

	empCount = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def __del__(self):
		Employee.empCount -= 1

	def disp_empCount(self):
		print("Employee Count = {}".format(Employee.empCount))

	def disp_empDetails(self):
		print("{} salary is {}".format(self.name,self.salary))

# emp1 = Employee("Ally",4000)
# emp2 = Employee("Belinda",5000)
# emp3 = Employee("Jane",2000)
# emp4 = Employee("Steven",6000)
# emp1.disp_empCount()
# del emp4
# emp1.disp_empCount()


# class Square(Rectangle):

# 	def __init__(self,length):
# 		super().__init__(length,length)

# 	def perimeter(self):
# 		print("Perimeter = {}".format(4*self.length))

# sq1 = Square(10)
# sq1.area()
# sq1.perimeter()
# print(sq1.length)
# print(sq1.width)

# Challenge : Inheritance
# class FullTimeStaff(Employee):
# 	#pass

# 	def __init__(self,name,salary,leave):
# 		super().__init__(name,salary)
# 		# self.name = name
# 		# self.salary = salary
# 		self.leave = leave

# 	def disp_empDetails(self):
# 		print("{} salary is {} and leave is {}".format(self.name,self.salary,self.leave))


# class PartTimeStaff(Employee):
# 	def __init__(self,name,hrrate):
# 		super().__init__(name,0)
# 		self.hrrate  = hrrate

# 	def disp_empDetails(self):
# 		print("{} hourly rate is {}".format(self.name,self.hrrate))


# emp1 = FullTimeStaff("Ally",4000,21)
# emp2 = FullTimeStaff("Belinda",5000,25)
# emp3 = PartTimeStaff("Jane",100)

# emp1.disp_empDetails()
# emp2.disp_empDetails()
# emp3.disp_empDetails()
# emp1.disp_empCount()
# del emp3
# emp1.disp_empCount()

# Polymerism
# class Animal():
# 	def talk(self):
# 		print("Animal can talk")

# class Cat(Animal):
# 	def talk(self):
# 		print("meow meow meow")

# class Dog(Animal):
# 	def talk(self):
# 		print("wof wof wof")

# def sound(a):
# 	a.talk()

# cat1 = Cat()
# dog1 = Dog()

# sound(cat1)
# sound(dog1)


	




