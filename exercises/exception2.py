try:
	f = open("xhello.txt")
	fl = f.read()
	print(fl)
except FileNotFoundError as e:
	print("File not exist", e)
