# a = (i*i for i in range(10) )

# b = list(a)
# print(b)


b = sum(i*i for i in range(10) )
b2 = sum(n*n for n in range(10) if n % 2 == 0)

print(b)
print(b2)

# for i in (i*i for i in range(10) ):
#   	print(i)

