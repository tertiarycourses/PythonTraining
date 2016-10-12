class Vehicle:
	def turn(self):
		print("I can turn")

	def walk(self):
		print("I can walk")


class Duck(Animal):
	def __init__(self,color):
		self.color = color
		Animal.count += 1

	def sound(self):
		print("quaaaaaak")
	
	def walk(self):
		print("walk like a duck")

	def talk(self):
		print("talk like a duck")

	
class Dog(Animal):
	def __init__(self,color):
		self.color = color
		Animal.count += 1

	def sound(self):
		print("wooooooof")
	
	def walk(self):
		print("walk like a dog")

def main():	
	print("Duck:")
	duck1 = Duck("black")
	duck1.sound()
	duck1.walk()
	duck1.talk()
	duck1.displaycolor()

print("\nDog:")
	dog1 = Dog("white")
	dog1.sound()
	dog1.walk()
	dog1.talk()
	dog1.displaycolor()
	dog1.displaycount()


if __name__ == "__main__" : main()

