def range_sq(n):
	for x in range(n):
		yield x ** 2  

for i in range_sq(10):
	print(i)
