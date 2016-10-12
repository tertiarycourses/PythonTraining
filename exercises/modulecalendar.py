def range_sq(n):
	for i in range(n):
		yield i*i

for i in range_sq(10):
	print(i)