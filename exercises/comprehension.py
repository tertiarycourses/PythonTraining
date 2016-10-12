a = []
for x in range(10):
	a.append(x**2)
print(a)

b = [x**2 for x in range(10)]
print(b)

b = [x**2 for x in range(10) if x%2==0]
print(b)

listOfWords = ["this","is","a","list","of","words"]

items = [ word[0] for word in listOfWords ]

print(items)