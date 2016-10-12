with open("hello.txt",'w') as f:
	for i in [1,2,3,4,5]:
		f.write("Hello World {}\n".format(i))


with open("hello.txt",'r') as f:
	for i in f:
		print(i)

		