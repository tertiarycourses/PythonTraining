def main():
	try:
		for fl in readfile('hello.tt'):
			print(fl.strip())
	except FileNotFoundError as e:
		print("File not exist", e)
	except ValueError as e:
		print("Bad filename",e)


def readfile(file):
    if file.endswith('.txt'):
        f = open(file)
        return f.readlines()
    else:
        raise ValueError("wrong extension")

if __name__ == "__main__":main()