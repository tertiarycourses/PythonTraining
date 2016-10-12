# Open a file for writing and create it if it doesn't exist
f = open("textfile.txt","w+")
  
# Open the file for appending text to the end
#  f = open("textfile.txt","a+")

# write some lines of data to the file
for i in range(10):
  f.write("This is line %d\n" % (i+1))
  
# close the file when done
f.close()
