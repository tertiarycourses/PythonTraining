class Employee:
	count = 0
	name = "blank"
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.count += 1

	def displayCount(self):
		print("Total Employee %d" % Employee.count)

	def displayEmployee(self):
			print("Name : ", self.name,  ", Salary: ", self.salary)

employee1 = Employee("John Ang",4000)
employee2 = Employee("Tanya Ong",2000)
employee3 = Employee("Steve Wang",6000)
employee4 = Employee("Alfred Chee",1000)

employee1.displayEmployee()
employee2.displayEmployee()
employee3.displayEmployee()

employee1.displayCount()


