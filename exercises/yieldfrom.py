def range_sq(n):
    yield from (i ** 2 for i in range(n))

for i in range_sq(10):
    print(i)