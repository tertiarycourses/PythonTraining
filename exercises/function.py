def main2():

	a = areaofcircle(2)
	print("area of circle with radius 2 = ", a)

	b = areaoftriangle(2,6)
	print("area of triangle = ", b)

def areaofcircle(radius):
	pi = 3.1417
	return pi*radius*radius

def areaoftriangle(base=1,height=5):
	return 0.5*base*height

if __name__ == "__main__": main()