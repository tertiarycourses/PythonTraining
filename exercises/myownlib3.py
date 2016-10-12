def main():
	a = areaofcircle(2)
	b = areaoftri(2,4)

	print(a)
	print(b)

	duck1 = Duck()
	duck1.walk()

def circle(r):
	pi = 3.1417
	return pi*r*r, 2*pi*r

def areaoftri(b,h):
	return 0.5*b*h

class Duck:

	def walk(self):
		print("walk like a duck")

if __name__ == "__main__":main()


