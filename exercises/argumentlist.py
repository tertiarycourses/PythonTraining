def add(a,b,*c):
	d = a + b
	for k in c:
		d += k
	return d

def main():

	print(add(2,3))
	print add(2,3,4,5,6)

if __name__ == "__main__" : main()
