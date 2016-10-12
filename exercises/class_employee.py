# define the class which is template
class Employee:

	def __init__(self,name, salary):
		self.name = name
		self.salary = salary

	def displayEmpDetails(self):
		print("{} salary is {}".format(self.name, self.salary))

class FullTimeStaff(Employee):

	empCount = 0

	def __init__(self,name, salary,leave):
		super().__init__(name,salary)
		FullTimeStaff.empCount = FullTimeStaff.empCount +1
		self.leave = leave

	def displayEmpCount(self):
		print("The number of full time employees is ",FullTimeStaff.empCount)

	def displayEmpDetails(self):
		print("{} salary is {} and leave is {}".format(self.name, self.salary,self.leave))

class PartTimeStaff(Employee):

	empCount = 0

	def __init__(self,name,hrrate):
		PartTimeStaff.empCount = PartTimeStaff.empCount +1
		self.name = name
		self.hrrate = hrrate

	def displayEmpCount(self):
		print("The number of part time employees is ",PartTimeStaff.empCount)

	def displayEmpDetails(self):
		print("{} hourly rate is {}".format(self.name, self.hrrate))

# Create objects
emp1 = FullTimeStaff('Ally',5000,21)
emp2 = FullTimeStaff('Belinda',4000,18)
emp3 = PartTimeStaff('Jane',50)

#Ask Ally salary
emp1.displayEmpDetails()
emp2.displayEmpDetails()
emp3.displayEmpDetails()

#Ask # of employee
emp2.displayEmpCount()
emp3.displayEmpCount()


# class Duck:

# 	def __init__(self,name):
# 		print("I am borned")
# 		self.name = name

# 	def __del__(self):
# 		print("I am destroyed")

# 	def walk(self):
# 		print("{} walk like a duck".format(self.name))

# 	def talk(self):
# 		print("quaaaaaaak ")

# # Create objects based on the class
# duck1 = Duck('donald')
# duck2 = Duck('duck2')

# # Get the objects to do something
# duck1.walk()
# duck1.talk()
# duck2.walk()
# duck2.talk()