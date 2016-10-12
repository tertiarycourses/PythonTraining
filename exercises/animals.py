class Animal():
	count = 0
	def __init__(self,c):
		self.color = c
		Animal.count += 1
	def __del__(self):
		Animal.count -= 1
	def sound(self):
		print("sound like an animal")
	def walk(self):
		print("walk like an animal")
	def displaycolor(self):
		print("have a {} color".format(self.color))
	def displaycount(self):
		print("Total number of animals is {}".format(Animal.count))

class Duck(Animal):
	def __init__(self,c,name):
		self.color = c
		self.name = name
		Animal.count += 1
	def quack(self):
		print("quaaaaaak")
	def walk(self):
		print("walk like a duck")


class Dog(Animal):
	def bark(self):
		print("wooooooooof")

def main():
	duck1 = Duck("white","duck1")
	duck2 = Duck("black","duck2")
	dog1 = Dog("white")
	dog2 = Dog("grey")

	duck1.displaycount()
	del duck2
	del dog1
	del dog2
	duck1.displaycount()

if __name__ == "__main__": main()