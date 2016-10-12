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

def main():	
	print("Duck:")
	duck1 = Duck("donald")
	duck1.sound()
	duck1.walk()
	duck1.talk()
	duck1.displayname()

	print("\nDog:")
	dog1 = Dog("white")
	dog1.sound()
	dog1.walk()
	dog1.talk()
	dog1.displaycolor()
	dog1.displaycount()


if __name__ == "__main__" : main()

