def main():

	a = areaofcircle(2)
	print("area of circle with radius 2 = ", a)

	b = areaoftriangle(2,6)
	print("area of triangle = ", b)

def areaofcircle(radius):
	pi = 3.1417
	return pi*radius*radius

def areaoftriangle(base=1,height=5):
	return 0.5*base*height

class Animal:

	count = 0

	def __init__(self,name):
		self.name = name
		Animal.count += 1

	def __del__(self):
		print("{} is gone".format(self.name))
		Animal.count -= 1

	def walk(self):
		print("{} walk like a animal".format(self.name))

	def talk(self):
		print("{} talk like a animal".format(self.name))

class Duck(Animal):

	def quack(self):
		print("{} quaaaak".format(self.name))

	def walk(self):
		print("{} walk like a duck".format(self.name))

	def bark(self):
		print("{} does not bark ".format(self.name))

	def num(self):
		print("Number of duck is {}".format(Duck.count))

class Dog(Animal):

	def quack(self):
		print("{} does not quack".format(self.name))

	def bark(self):
		print("{} wooooof ".format(self.name))

	def walk(self):
		print("{} walk like a dog".format(self.name))

	def num(self):
		print("Number of dog is {}".format(Dog.count))


if __name__ == "__main__": main()