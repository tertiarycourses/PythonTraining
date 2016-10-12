class Animal:
	count = 0
	def __init__(self,color):
		self.color = color
		Animal.count += 1

	def talk(self):
		print("talk like an animal")

	def displaycolor(self):
		print("color is ",self.color)

	def displaycount(self):
		print("number of animals are ",Animal.count)

class Duck(Animal):

	def __init__(self,name):
		self.name = name
	
	def sound(self):
		print("quaaaaaak")
	
	def walk(self):
		print("walk like a duck")

	def talk(self):
		print("talk like a duck")

	def displayname(self):
		print("my name is ",self.name)

	
class Dog(Animal):

	def sound(self):
		print("wooooooof")
	
	def walk(self):
		print("walk like a dog")

def areaofcirlce(r):
	pi = 3.1417
	return pi*r*r
