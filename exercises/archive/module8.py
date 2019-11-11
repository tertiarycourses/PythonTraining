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
	


class Employee:

    empCount = 0
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount = Employee.empCount+1
    
    def __del__(self):
        Employee.empCount = Employee.empCount-1
    
    def dispEmployee(self):
        print("{} salary is {}".format(self.name,self.salary))

    def dispEmployeeCount(self):
        print("Number of Employee is {}".format(Employee.empCount)) 

emp1 = Employee('Ally',5000)
emp2 = Employee('Belinda',6000)
emp3 = Employee('Jane',4000)

emp1.dispEmployee()
emp1.dispEmployeeCount()
del emp1
emp2.dispEmployeeCount()



