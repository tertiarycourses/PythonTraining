# Python Essential Training
# Module 5: Functions
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

# def f(x):
# 	return x*x

# print(f(7))

# def taxifare(distance):
# 	booking = 2.5
# 	starting = 3
# 	cost = 1
# 	fare = booking + starting + distance*cost
# 	gst = fare*0.07
# 	return fare,gst

# distance = 38
# (fare,tax) = taxifare(distance)
# print("Taxi fare is ${} and tax is ${:0.1f}".format(fare,tax))

# def grocery(order):
# 	discount = 25 if order > 200 else 0
# 	discount_amt = order*discount/100
# 	order_discounted = order - discount_amt
# 	tax = 0.07*order_discounted
# 	return discount_amt,tax

# order = 100
# discount,tax = grocery(order)
# print("The discount is ${:0.2f}".format(discount))
# print("The tax is ${:0.2f}".format(tax))

# Multiple Inputs
# def f(x=2,y=0):
# 	return 2*x+3*y

# print(f(1,6))

# Variable Inputs
# def sum(a,b,*c):
# 	s = 0
# 	s = a+b
# 	for i in c:
# 		s = s+i
# 	return s
# print(sum(3,4,5,6,7,8,9,10,11,12))

# def min(a,*b):
# 	m = a
# 	for i in b:
# 		if m>i:m=i
# 	return m

# print(min(6,7,3,4,5))
# def sum2(a,b):
# 	s = 0
# 	for i in range(a,b+1):
# 		s = s+i
# 	return s

# print(sum2(1,100))

# Loop through dictionary
# def f(**a):
# 	for i,j in a.items():
# 		print(i,j)

#a = {'a':3,'b':5}
# f(a=3,b=5)

# Lambda Function

# def f(x):
# 	return x*x
# a = lambda x:x*x

# print(a(4))

# def f(x,y): return 10*x+y
# print(f(3,4))

# a = lambda x,y:10*x+y
# print(a(3,4))

# Map 
# a = [2,3,4,5]
# b = map(lambda x:10*x+4,a)
# print(list(b))

# Exercise: Map
# x = [0,1,2,3]
# y = [2,4,6,8]

# a = map(lambda x,y:10*x+y,x,y)
# print(list(a))

# Filter
# a = filter(lambda x:x>4,[5,6,3,2,7])
# print(list(a))




