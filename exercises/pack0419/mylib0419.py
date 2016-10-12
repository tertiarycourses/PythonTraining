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

