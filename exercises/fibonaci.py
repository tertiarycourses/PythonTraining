f = []
a , b = 0 , 1
while (b < 100):
	f.append(b)
	b, a = a+b, b
print(f)