# List operations

a= [2,3,6,3,5,3,4,3,6]
print("original a :",a)
a[0]=6
print("after change a :",a)
b = a.count(6)
print("Number of 6 in the list : ",b)

#append to add last number
a.append(10)
print("append : ", a)

#insert the number 
a.insert(2,99)
a.insert(-1,199)
print("insert :", a)

#remove the number
a.remove(99)
print("remove :", a)

#pop to remove last number
b = a.pop()
print(b)
print("pop :", a)

#reverse
a.reverse()
print("reverse :", a)

#sort
a.sort()
print("sort : ",a)


