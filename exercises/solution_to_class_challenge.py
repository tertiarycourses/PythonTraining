class Employee():

	count = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.count += 1

	def displayName(self):
		print("My name is {}".format(self.name))

	def displaySalary(self):
		print("My salary is ${}".format(self.salary))

	def displayCount(self):
		print("Number of employee is {}".format(Employee.count))

class Animal:
	
	def __init__(self,name):
		self.name = name
	def walk(self):
		print("{} walk like an animal".format(self.name))
	def talk(self):
		print("{} talk like an animal".format(self.name))
		
class Duck(Animal):

	def walk(self):
		print("{} walk like a duck".format(self.name))
	def quack(self):
		print("{} quaaaaack".format(self.name))

class Dog(Animal):
	def __init__(self,name,color):
		self.name = name
		self.color = color
	def walk(self):
		print("{} walk like a dog".format(self.name))
	def bark(self):
		print("{} wooooof".format(self.name))
	def displaycolor(self):
		print("{} has a {} color".format(self.name,self.color))

duck1 = Duck("duck1")
# duck2 = Duck("duck2") 
# duck3 = Duck("duck3") 
# duck4 = Duck("duck4") 
# duck5 = Duck("duck5")

# dog1 = Dog("dog1","white")
# dog2 = Dog("dog2","black") 
# dog3 = Dog("dog3","grey") 

duck1.walk()
duck1.quack()
duck1.talk()
# duck2.walk()
# duck2.quack()
# duck3.walk()
# duck3.quack()

# dog1.walk()
# dog1.bark()
# dog1.displaycolor()

