def areaofcircle(r):
	pi = 3.1417
	return pi*r*r

def areaoftriangle(b,h):
	return 0.5*b*h

def main():
	
	radius = 2
	area = areaofcircle(radius)
	print("area of cicle with %0.2f is %0.2f" %(radius,area))


	base = 2
	height = 6
	area = areaoftriangle(base,height)
	print("area of triangle with base %0.2f and height %0.2f is %0.2f" %(base,height,area))

if __name__ == "__main__":main()