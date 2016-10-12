class Employee:
	empCount = 0

	def __init__(self, name, salary):
	  self.name = name
	  self.salary = salary
	  Employee.empCount += 1

	def displayCount(self):
	 print("Total Employee %d" % Employee.empCount)

	def displayEmployee(self):
	  print("Name : ", self.name,  ", Salary: ", self.salary)

def main():

	emp1 = Employee("Zara", 2000)
	emp2 = Employee("Manni", 5000)

	emp1.displayEmployee()
	emp2.displayEmployee()

	emp1.displayCount()
	emp2.displayCount()

if __name__ == "__main__" : main()