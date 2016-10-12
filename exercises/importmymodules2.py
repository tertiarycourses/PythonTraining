import mymodules, myfunctions

def main():	
	duck1 = mymodules.Duck("donald","white")
	duck1.sound()
	duck1.walk()
	duck1.talk()
	duck1.displayname()

	print(" ")
	dog1 = mymodules.Dog("white")
	dog1.sound()
	dog1.walk()
	dog1.talk()
	dog1.displaycolor()
	dog1.displaycount()

	print(" ")
	
	radius = 2
	area = myfunctions.areaofcircle(radius)
	print("area of cicle with %0.2f is %0.2f" %(radius,area))

	print(" ")

	base = 2
	height = 6
	area = myfunctions.areaoftriangle(base,height)
	print("area of triangle with base %0.2f and height %0.2f is %0.2f" %(base,height,area))


if __name__ == "__main__" : main()
