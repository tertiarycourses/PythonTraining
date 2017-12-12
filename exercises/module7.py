# Python Essential Training
# Module 7: Comprehension & Generators
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

# List Comprehension
# Manual Entry
# a = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(a)

# For Loop
# c = []
# for i in range(11): 
# 	if i%2 == 0: continue
# 	c.append(i*i)
# print(c)

# List Comprehension
# b = [i*i for i in range(11)]
# b = [i*i for i in range(11) if not i%2 == 0]
# print(b)

# a = "Today is a rainy day"
# b = a.split()
# print(b)

# Get the first letter of each word
# c = [i[0] for i in b]
# print(c)

# Get the last letter of each word
# c = [i[-1] for i in b]
# print(c)

# Set Comprehension
# a = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
# print(a)

# b = {i*i for i in range(11)}
# print(b)

# print(a == b)

# Dict Compreshension
# a = {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}
# print(a)

# b = {i:i*i for i in range(11)}
# print(b)

# Challenge 
# b = [i*i for i in range(40) if not (i%3 == 0 or i%5 == 0)]
# print(b)

# Problem of List - Inefficient memory storage
# a = [i*i for i in range(100)]
# print(a)

# Generator Expression
a = (i*i for i in range(100) if i%2==0)
#print(a)
#print(list(a))

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# for i in a:
# 	print(i)

# Comparing List and Generator Computation
# a = [i*i for i in range(100)]
# print(sum(a))

# a = (i*i for i in range(100))
# print(sum(a))

# Challenge
# namelist = ['Ally','Jane','Belinda']
# upper_name = (name.upper() for name in namelist)
# print(next(upper_name))
# print(next(upper_name))
# print(next(upper_name))

# Generator Function

# def range2(n):
# 	for i in range(n):
# 		if i%2 == 0:yield i

# for i in range2(10):
# 	print(i)


# Challenge
# def fibo():
# 	a,b=0,1
# 	while True:
# 		yield a
# 		a,b=b,a+b

# f = fibo()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
