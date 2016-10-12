def geometric_progression(a, r, n):
	for x in range(n):
		yield a*(r**x)

for i in geometric_progression(2,3,10):
	print(i)
