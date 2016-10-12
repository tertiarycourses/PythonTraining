# Open the file back up and read the contents
# f = open("textfile.txt","r")
# fl = f.readlines() # readlines reads the individual lines into a list
for x in open("textfile.txt","r"):
	print (x.strip())
