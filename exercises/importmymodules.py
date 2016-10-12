import mymodules as me

def main():	
	duck1 = me.Duck("donald","dark")
	duck1.sound()
	duck1.walk()
	duck1.talk()
	duck1.displayname()

	print(" ")
	dog1 = me.Dog("white")
	dog1.sound()
	dog1.walk()
	dog1.talk()
	dog1.displaycolor()
	dog1.displaycount()

if __name__ == "__main__" : main()
