class Animal:

	def __init__(self,name):
		self.name = name

	def walk(self):
		print("{} walk like a animal".format(self.name))

	def talk(self):
		print("{} talk like a animal".format(self.name))

class Duck(Animal):

	def talk(self):
		print("{} quaaaak".format(self.name))

	def walk(self):
		print("{} walk like a duck".format(self.name))


class Dog(Animal):

	def talk(self):
		print("{} wooooof ".format(self.name))

duck1 = Duck("duck1")
duck1.talk()
duck1.walk()

dog1 = Dog("dog1")
dog1.talk()
dog1.walk()

