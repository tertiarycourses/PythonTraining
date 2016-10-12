# Module 7 Modules


a = [i*i for i in range(11)]
print(a)

# import pandas as pd

# a = [1,2,3,4]
# b = [4,3,2,1]
# print(a+b)
# a1 = pd.Series(a)
# b1 = pd.Series(b)
# print(a1+b1)

# import giclib

# order = 100
# discount,tax = giclib.grocery(order)
# print("discont =${:0.2f}".format(discount))
# print("tax = ${:0.2f}".format(tax))

#import math as m
# from math import sin,pi
# #import time 
# from time import sleep

# print(sin(pi/2))
# sleep(5)
# print(sin(pi))


# Module 5 Function

# def grocery(order):

# 	# if order>200:
# 	# 	discount = 25
# 	# else:
# 	# 	discount = 0

# 	discount = 200 if order > 200 else 0

# 	discount_amt = order*discount/100
# 	amt = order - discount_amt
# 	tax = amt*0.07

# 	return(discount_amt,tax)

# order = 150
# (discount,tax) = grocery(order)
# print("Discount = ${:0.2f}".format(discount))
# print("GST = ${:0.2f}".format(tax))

# def fare(distance):
# 	booking= 2.5
# 	starting = 3.5
# 	cost = 1
# 	fare = booking+starting+distance*cost
# 	return fare

# distance = 10
# print("Taxi fare is ${}".format(fare(distance)))

# def f(x=1,y=1):
# 	return (2*x,3*y)

# print(f(2,3))

# Module 4 Control Structures

# Loop

# for i in range(11):
# 	if i == 4:break
# 	print(i)
# name = ['ally','belinda','jane']
# height = [170,150,160]
# weight = [50,60,55]

# person = zip(name,height,weight)
# for (n,h,w) in person:
# 	print("{} height is {}cm and weight {}kg".format(n,h,w))



# for index,name in enumerate(person):
# 	h = height[index]
# 	w = weight[index]
# 	print("{} height is {}cm and weight {}kg".format(name,h,w))

# for index,name in enumerate(person):
# 	h = height[index]
# 	w = weight[index]
# 	print("{} height is {}cm and weight {}kg".format(name,h,w))





# a = []
# for i in range(1,11):
# 	if i%3 == 0: continue
# 	a.append(i*i)
# print(a)

#a = [3,4,5,7]
# for i in range(2,10,3):
# 	print(i)


# a = 1
# b = 1
# while (b<200):
# 	a = b
# 	b = a+b
# 	#a,b = b,a+b
# 	print(a)

# while a<5:
# 	while b<5:
# 		print(a)
# 		b = b + 1
# 	b = 1
# 	a += 1


# Conditional
# grade='D'

# if grade == 'A':
# 	print('Excellent')
# elif grade == 'B':
# 	print('Well done')
# elif grade == 'C':
# 	print('Good job')
# else:
# 	print('I dont know your grade')


# a = 3
# b = 4

# c = a if a>b else b
# print(c)
# if a<b:
#    print("a is smaller than b")
# elif a>b:
# 	print("a is larger than b")
# else:
# 	print("a same as b")

# print("the end")

#Module 3 Operators

# a = [3,4,5,7,2]
# print(4 not in a)
# a = 2
# print(a)
# print(a == 2)

# a += 5 #a = a +5 
# print(a)
#print(7//3)

# Module 2 Data Types


# a = {3,4,6,7}
# print(list(a))

# Set

# a = {4,5,2,4}
# b = {4,5,10,9}
# print(b-a)

# Dictionary

# height = {'ally':150,'belinda':144,'jane':160}
# print(height['belinda'])

# Tuple

# a = (4,5,6,'hi',8.9,4)
# print(len(a))
# print(a[-1])
# List

# a = [1,2,3,4]
# b = [4,3,2,1]
# print(a+b)

# letters =['A','C','C','A','T','T','G','A','C','A']
# print(letters.count('A'))
# print(letters.index('T'))

# letters2 = letters.copy()
# letters2.remove('G')
# letters2.insert(3,'A')
# letters2.reverse()
# print(letters2)

#a = [4,5,7,'hi',9.8,8,5,5,5,5,5]
# print(a)
# print(a[-1])
# print(len(a))
# print(a.count(5))
# a.insert(2,99999)
# a.append(999999)
# a.remove(99999)
# a.pop()
# a = [4,5,7,'hi',9.8,8,5,5,5,5,5]
# b = a.copy()
# c = a
# c.append(99999)
# print(a)
# print(b)
# print(c)
# a = [7,4,5,2,9,3,4]
# print(sum(a))
# print(a)
# b = sorted(a)
# a.reverse()
# print(a)
# print(b)

# Strings

# country ="France".upper()
# capital ="Paris".lower()

# print("The capital of {} is {}".format(country,capital))

# a = 'atgcaattgcaacctagctagggctcaata'
# #print(a[16:19])
# #print(a.find('gct',17))
# b= a.count('gct')
# print("Count = {}".format(b))

#a = 'Today is a good day'
# a = 'angchewhoe@gmail.com'
# b = a.split('@')
# print(b)
# c = "@".join(b)
# print(c)

# a = "Hello            ".strip().upper()
# b = " World".lower().replace('world','Alfred')
# print(a+b)


# Numbers
# a = 5
# b = 3
# a,b,c = 5.454543,3.45454,10.4545454
#print(a*b*c)
# print("{:0.3f}+{}".format(a,b))


# Module 1
#print("Hello World")
# print("Run again")