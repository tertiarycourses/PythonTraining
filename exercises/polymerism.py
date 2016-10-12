class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
    	print('The duck don''t bark')

class Dog:
	def quack(self):
		print("The dog don't quack")

	def walk(self):
		print("walk like a dog")

	def bark(self):
		print("Woooof")

def forest(dog):
	dog.bark()
	dog.quack()
	dog.walk()

def pond(duck):
	duck.bark()
	duck.quack()
	duck.walk()


def main():
    donald = Duck()
    fido = Dog()

    #forest(donald)
    pond(fido)


if __name__ == "__main__": main()
