def range_sq(n):
	for x in range(n):
		yield x ** 2  

def sum(a,b,*c):
	s = a+b
	for i in c:
		s = s+i
	return s


def min(*b):
	m = b[0]
	for i in b:
		if i<m:m=i
	return m

def f2(x=0,y=0):
	return x*x+y*y*y

def fare(distance):
	booking_fee = 3
	starting_price = 3
	cost = 0.5 
	return booking_fee+starting_price+distance*cost

def grocery(order):
	discount = 25 if order > 200 else 0
	tax = 0.07*(order-discount*order/100)
	return discount, tax

def test():
	print(sum(4,5,6,8,9,19))
	order = 800
	discount, tax = grocery(order)
	print('discount = {} and tax = {:0.2f}'.format(discount,tax))

print(__name__)
if __name__ == "__main__": test()