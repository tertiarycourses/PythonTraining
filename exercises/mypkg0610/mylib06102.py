def sum(a,b,*c):
	 s = a+b
	 for i in c:
	 	s = s + i
	 return s

def min(a,*b):
	m = a
	for i in b:
		if i<m: m = i
	return m