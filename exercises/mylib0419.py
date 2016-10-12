def circle(r):
	pi = 3.1417
	return (pi*r*r,2*pi*r)

def rect(a=3,b=4):
	return a*b

def sum(a,b,*c):
	s = a + b	
	for i in c:
		s = s +i
	return s

def min(a,*b):
	m = a
	for i in b:
		if i<m: m=i
	return m

def grocery(order):
	discount = 25 if order > 200 else 0
	tax = 0.07*(order-discount*order/100)
	return (discount,tax)

