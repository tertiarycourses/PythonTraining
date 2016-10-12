def main():
	emp1 = Employee('Ally',5000,45)
	emp1.displayDetails()
	print(emp1.age)

def areaofcircle(r):
	pi = 3.1417
	return pi*r*r

def areaoftri(b,h):
	return 0.5*b*h

class Employee:
	empCount = 0

	def __init__(self,name,salary,age):
		self.name = name
		self.salary = salary
		self._age = age
		Employee.empCount += 1

	
	@property
	def age(self):
	    return self._age
	

	def __del__(self):
		print("I am out")
		Employee.empCount -= 1

	def displayDetails(self):
		print("{} salary is {}".format(self.name,self.salary))

	def displayCount(self):
		print("No of employee is {}".format(Employee.empCount))

class FullTimeStaff(Employee):

	def __init__(self,name,salary,age, leave):
		super().__init__(name,age, salary)
		self.leave = leave
		Employee.empCount += 1

	def displayDetails(self):
		print("{} salary is {} and leave is {}".format(self.name,self.salary,self.leave))


class Rectangle:

	def __init__(self,sizeA,sizeB):
		self.sizeA = sizeA
		self.sizeB = sizeB

	def area(self):
		print(self.sizeA*self.sizeB)

class Square(Rectangle):

	def __init__(self,size):
		super().__init__(size,size)

class Duck:

	def __init__(self,color):
		self.color = color

	def __del__(self):
		print("I am deleted")

	def walk(self):
		print("walk like a duck")

	def talk(self):
		print("quaaak")

class Dog:

	def __init__(self,color):
		self.color = color

	def __del__(self):
		print("I am deleted")

	def walk(self):
		print("walk like a dog")

	def talk(self):
		print("woooooof")

if __name__ == "__main__": main()

