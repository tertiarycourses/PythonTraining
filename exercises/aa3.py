class Person:

	def __init__(self,name,weight,height):
		self.name = name
		self.weight = weight
		self.height = height 

	def talk(self):
		print('{} talk like a person'.format(self.name))

	def walk(self):
		print('{} walk like a person'.format(self.name))

	def figure(self):
		print('{} height is {}cm and weight is {}kg'.format(self.name,self.height,self.weight))

ally = Person('Ally',60,160)
# ally.weight = 60
# ally.height = 160
# ally.name = 'Ally'
belinda = Person('Belinda',55,155)
# belinda.weight = 55
# belinda.height = 155
# belinda.name = 'Belinda'


ally.talk()
ally.walk()
ally.figure()
belinda.talk()
belinda.walk()
belinda.figure()


# import random

# a = random.uniform(3,10	)
# print(a)


# from math import sin,pi

# x = sin(pi/2)
# print(x)

#a = (i*i for i in range(1,10000000))
# a = (i*i for i in range(1,11) if (i*i)%3!=0 and (i*i)%5!=0)

# for i in a:
#  	print(i)

# list = ["this","is","a","list","of","words"]
# items = [ word[-1] for word in list]
# print(items)

# a = []
# for i in range(1,11):
# 	a.append(i*i)
# print(a)


# f = lambda x:x*x
# f = lambda x,y:10*x+y
# x = [0,1,2,3]
# y = [2,4,6,8]
# print(list(map(f,x,y)))

# g = lambda x,y:10*x+y

# print(g(2,4))

# a = f(2)
# print(a)

# a =[9,7,4,6,2]

# def f(n):
# 	for i in range(n):
# 		yield i*i 

# for i in :
# 	print(i)

# def f(x):
# 	yield x*x

# print(list(map(f,a)))

# for i in range(1,11):
# 	print(f(i))

def circle(r):
	pi = 3.1417
	return (pi*r*r,2*pi*r)

def rect(a=3,b=4):
	return a*b

def sum(a,b,*c):
	s = a + b	
	for i in c:
		s = s +i
	return s

def min(a,*b):
	m = a
	for i in b:
		if i<m: m=i
	return m

def grocery(order):
	discount = 25 if order > 200 else 0
	tax = 0.07*(order-discount*order/100)
	return (discount,tax)

#a = sum(1,2,3,4,5,6,7,8,9,10)
# b = min(8,5,7,6,9,8,9,5)
# print(b)