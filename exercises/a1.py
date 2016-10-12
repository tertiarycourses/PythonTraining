import Quandl
import matplotlib.pyplot as plt

data = Quandl.get('INTC', collapse='weekly')
print(data.head())

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd 

# sp500 = pd.read_csv("data/sp500.csv",index_col='Symbol', usecols=[0, 2, 3, 7])

# a1 = pd.Series(np.random.randn(10))
# b1 = pd.Series(np.random.randn(10))

# a = pd.DataFrame({'price':a1,'qty':b1})
# print(sp500[sp500.Price<100])
# a = [1,2,3,4]
# b = [4,3,2,1]
# print(a+b)
# a = np.array([1,2,3,4])
# b = np.array([4,3,2,1])
# print(a+b)
# a = pd.Series({'alfred':4,'belinda':3,'ally':8})
# a.index=['belinda','alfred','ally']
# a = pd.Series(np.random.randn(100))
# print(a.index)


# x = np.array([3,4,2,8,5])
# plt.pie(x)
# plt.show()

# x = np.random.randn(10000)
# plt.hist(x,50)
# plt.show()
# x = np.linspace(-1,1,255)
# y = np.linspace(-2,2,300)
# X, Y = np.meshgrid(x, y)
# z = np.sin(X)*np.cos(Y)
# plt.contour(X,Y,z,50)

# x = np.random.randn(100)
# y = np.random.randn(100)
# x = np.array([3,4,5,6,7,2])
# y = np.array([1,2,3,4,5,6])
# plt.bar(x,y,color='y')
# plt.show()
# x = np.linspace(0,4*np.pi,200)
# y = np.sin(x)
# y2 = np.cos(x)
# y3 = y*y2
# y4 = y**2 - y2**2
# plt.subplot(2,2,1)
# plt.plot(x,y,'sg-',label='sine cuve')
# plt.subplot(2,2,2)
# plt.plot(x,y2,'or-',label='cosine curve')
# plt.subplot(2,2,3)
# plt.plot(x,y3,'^b-',label='cosine curve')
# plt.subplot(2,2,4)
# plt.plot(x,y4,'ok-',label='cosine curve')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.axis([0,10,-3,1.5])
# plt.legend()
# plt.title('My plots')
plt.show()
# a = [1,1,1,'hi']
# b = [2,2,'hi',2]
# print(a+b)
# c = []
# for i in range(len(a)):
# 	c.append(a[i]+b[i])

# print(c)
# a = [[1,1],[1,1],[1,1]]
# b = [[2,2],[2,2],[2,2]]
#print(a-b)

# a = np.linspace(2,20,20)
# b = np.linspace(22,40,20)
# print(a)
# print(b)
# print(a+b)
# a = np.array([[1,1],[1,1],[1,1]])
# b = np.array([[2,2],[2,2],[2,2]])
# a = np.matrix([[1,1],[1,1]])
# b = np.matrix([[2,2],[2,2]])

#print(a*b)

# a = a.astype(np.float64)
# print(a.dtype)
# def f(x,y):
#     return 10*x+y

# a = np.fromfunction(f,(5,4))

#a = np.diag([3,3,3,4,5,6,7,8])

# a = np.arange(20).reshape(5,4)
# a = np.random.normal([4,4])
# print(a)

# a = np.random.binomial(10,0.2,20)	
# print(a)

# a = np.array([2,3,-2,-3,2,6,-3,4,-3,5,-6,5,5,-2])
# print(sum(a[a>0]))
# = np.array([[1,1],[2,2],[3,3]])
# b = np.array([[4,4,],[5,5],[6,6]])
# print(a)
# print(b)
# print(np.hstack([a,b]))
# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a)
# print(a[1:3,[1,3]])

# with open('dummy999999.txt','r') as f:
# 	for i in f:
# 		print(i.strip())

# for i in open('dummy999999.txt','r'): 
# 	print(i.strip())
	
# with open('dummy999999.txt','a') as f:
# 	for i in range(41,50):
# 		f.write('Hello\t {}\t{}\n'.format(i,i*i))

# for i in range(31,40):
# 	f.write('Hello\t {}\t{}\n'.format(i,i*i))

# f.close()
# for i in range(41,50):
# 	f.write('Hello\t {}\t{}\n'.format(i,i*i))

# try:
# 	f = open('dummy999999.txt','r')
# except:
#     print("file does not exist")

# a = [1,2,3,"a",5,6,"b",7,8,"c"]
# b = []
# for i in a:
# 	try:
# 		if (i > 0): b.append(i)
# 	except:
# 		pass
# print(b)
# try:
# 	a = 'a'
# 	b = 8%a
# 	print(b)
# except:
# 	print('a has to be an integer')

# import sqlite3

# db= sqlite3.connect('test22.db')

# db.execute('CREATE TABLE stock (stock_name text, stock_price float32)')
# db.commit()

# db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Yahoo',37.67))
# db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Google',759.14))
# db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Apple',105.97))
# db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Microsoft',55.78))
# db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Intel',31.97))

# db.execute('UPDATE stock SET stock_price=? WHERE stock_name=?',(80,'Yahoo'))
# db.execute('UPDATE stock SET stock_price=? WHERE stock_name=?',(790,'Google'))
# db.commit()

# db.execute('DELETE FROM stock WHERE stock_name = "Yahoo"')

# a = db.execute('SELECT * FROM stock ORDER BY stock_name')
# db.commit()

# f = open('stock999.txt','w')
# for i in a:
# 	f.write('{} \t{}\n'.format(i[0],i[1]))


# class Employee():

# 	EmpCount = 0

# 	def __init__(self,name,salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.EmpCount = Employee.EmpCount + 1

# 	def __del__(self):
# 		Employee.EmpCount = Employee.EmpCount - 1 

# 	def displayEmpDetails(self):
# 		print('{} salary is ${}'.format(self.name,self.salary))

# 	def displayEmpCount():
# 		print('Number of employee = {}'.format(Employee.EmpCount))

# class FullTimeStaff(Employee):

# 	def __init__(self,name,salary,leave):
# 		Employee.__init__(self,name,salary)
# 		self.leave = leave

# 	def displayEmpDetails(self):
# 		print('{} salary is ${} and {} leaves '.format(self.name,self.salary,self.leave))

# class PartTimeStaff(Employee):

# 	def __init__(self,name,hrrate):
# 		self.name = name
# 		self.hrrate = hrrate
# 		Employee.EmpCount = Employee.EmpCount + 1

# 	def displayEmpDetails(self):
# 		print('{} hourly rate is ${}'.format(self.name,self.hrrate))

# emp1 = FullTimeStaff('Ally',4000,21)
# emp2 = FullTimeStaff('Belinda',5000,25)
# emp3 = PartTimeStaff('Jane',100)

# emp1.displayEmpDetails()
# emp2.displayEmpDetails()
# emp3.displayEmpDetails()
# Employee.displayEmpCount()

# del emp1
# del emp2
# Employee.displayEmpCount()


# class Rectangle():

# 	def __init__(self,length,height):
# 		self.length = length
# 		self.height = height

# 	def area(self):
# 		print('Area  = {}'.format(self.length*self.height))

# class Square(Rectangle):

# 	# def __init__(self,length):
# 	# 	Rectangle.__init__(self,length,length)

# 	def __init__(self,length):
# 		super().__init__(length,length)


# rect1 = Rectangle(10,5)
# rect1.area()
# sq1 = Square(10)
# sq1.area()


# class Person():

# 	def __init__(self,name, weight=50,height=180):
# 		self.name = name
# 		self.weight = weight
# 		self.height = height

# 	def walk(self):
# 		print('{} walk like  a person'.format(self.name))

# 	def talk(self):
# 		print('{} talk like a person'.format(self.name))

# ally = Person(name='Ally',height=170)
# belinda = Person('Belinda')

# ally.weight = 120

# print('Ally weight is {}'.format(ally.weight))
# print('Belinda weight is {}'.format(belinda.weight))

# ally.walk()
# belinda.talk()

# from time import sleep, time

# # def measure(func):
# # 	t = time()
# # 	func()
# # 	print(time()-t)

# # @decorator


# def measure(func):
# 	t = time()
# 	func()
# 	print(time()-t)

# @measure
# def delay():
# 	sleep(0.7)





# # def foo(func):
# # 	print("foo")
# # 	return func

# # @foo
# # def bar():
# # 	print("bar")
# # bar()
# # def get_text(name):
# #    return "lorem ipsum, {0} dolor sit amet".format(name)

# # def p_decorate(func):
# #    def func_wrapper(name):
# #        return "<p>{0}</p>".format(func(name))
# #    return func_wrapper

# # my_get_text = p_decorate(get_text)

# # print(my_get_text("John"))


# # import numpy as np 
# # import matplotlib.pyplot as plt 
# # import pandas as pd 
# # a = pd.Series(np.random.random(100))
# # b = pd.Series(np.random.random(100))
# # c = pd.DataFrame({'col1':a,'col2':b})
# # print(c.ix[2])
# # a = pd.DataFrame([['ally',165,'F'],['belinda',158,'F']],index=[1,2],columns=['name','height','gender'])
# # b = pd.DataFrame([['alfred',165,'M'],['Jane',158,'M']],index=[3,4],columns=['name','height','gender'])
# # print(a+b)
# # a = pd.Series({'a':5,'b':7,'c':2,'d':4})
# # print(a['c'])
# # b = pd.Series([4,3,2,1],index=['c','a','d','b'])
# # print(a+b)
# # x = np.linspace(0,4*np.pi,200)
# # y = np.sin(x)
# # y2 = np.cos(x)
# # y3 = np.sin(x)*np.cos(x)
# # y4 = np.sin(x)**2 - np.cos(x)**2
# # plt.subplot(2,2,1)
# # plt.plot(x,y,'^b-', label='sine')
# # plt.subplot(2,2,2)
# # plt.plot(x,y2,'or-', label='cosine')
# # plt.subplot(2,2,3)
# # plt.plot(x,y3,'sk-', label='sin*cos')
# # plt.subplot(2,2,4)
# # plt.plot(x,y4,'*g-', label='sin^2*cos^2')
# # plt.xlabel('x')
# # plt.ylabel('y')
# # plt.title('sine curve')
# # plt.legend()
# # plt.show()
# # a = [2,3,-2,-3,2,6,-3,4,-3,5,-6,5,5,-2]
# # b = np.array(a)
# # print(b[b>0])
# # print(sum(b[b>0]))


# #a = np.array([4,5,-3,2,-1,7,-2,8])
# # print(a[a>0])
# # a = np.array([[1,2],[3,4]])
# # print(np.mean(a,axis=1))

# # a = np.arange(1,10,2)
# # b = np.arange(11,20,2)
# # a = np.linspace(1,10,5)
# # b = np.linspace(11,20,5)
# # a = np.diag([3,3,3])
# # print(a)
# # print(b)
# # print(a+b)

# a =[[1,1],[1,1]]
# b =[[2,2],[2,2]]
# print(a+b)

# a = np.array([[1,1],[1,1]])
# b = np.array([[2,2],[2,2]])
# print(a+b)

# for i in  open('dummy.txt','r'):
# 	print(i.strip())
# # with open('dummy.txt','w') as f:
# # 	for i in range(20):
# # 		f.write('Hello {}\n'.format(i))

# a = [1,2,3,"a",5,6,"b",7,8,"c"]
# b = []
# for i in a:
# 	try:
# 		if (i > 0): b.append(i)
# 	except:
# 		pass
# print(b)

# a = 'hello'
# b = a**2
# print(b)

# try:
# 	a = 'hello'
# 	b = a**2
# 	print(b)
# except:
# 	print('Make sure a is a number')



# import sqlite3

# db= sqlite3.connect('test21.db')

# list = db.execute('SELECT * FROM stock ORDER BY stock_name')
# db.commit()


# f = open('dummy2.txt','w')
# for i in list:
# 	f.write('{}\t {}\n'.format(i[0],i[1]))

# # db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Yahoo',37.84))
# # db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Google',752.67))
# # db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Apple',107.13))
# # db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Intel',32.00))
# #db.execute('INSERT INTO stock (stock_name,stock_price) values (?,?)',('Amazon',632.99))

# # db.execute('UPDATE stock SET stock_price=? WHERE stock_name=?',(40.1,'Yahoo'))
# # db.execute('UPDATE stock SET stock_price=? WHERE stock_name=?',(800.5,'Google'))
# # db.execute('UPDATE stock SET stock_price=? WHERE stock_name=?',(60,'Intel'))
# # db.commit()

# db.execute('DELETE FROM stock WHERE stock_name = "Yahoo"')

# list = db.execute('SELECT * FROM stock ORDER BY stock_name')
# db.commit()

# for i in list:
# 	print(i)

# # db.execute('CREATE TABLE stock (stock_name text, stock_price float)')
# # db.commit()

# # class Rectangle:

# # 	def __init__(self,length,height):
# # 		self.length = length
# # 		self.height = height

# # 	def area(self):
# # 		area = self.length*self.height
# # 		print('Area = {}'.format(area))

# # class Square(Rectangle):

# # 	def __init__(self,length):
# # 		super().__init__(length,length)


# # rect1 = Rectangle(5,3)
# # sq1 = Square(5)

# # rect1.area()
# # sq1.area()

# # import math

# # print(dir(math))

# # a= [1,2,3,4,5,6,7,8,9,10]
# # f = lambda x: x%2
# # c = map(f,a)
# # print(list(c))

# # b = filter(f,a)
# # print(list(b))

# f2 = lambda x,y:10*x+y
# x = [0,1,2,3]
# y = [2,4,6,8,9,10]

# z = map(f,x,y)
# print(list(z))

# def f(x):
# 	return x*x

# a = []
# for i in range(1,11):
# 	a.append(i*i)
# print(a)

# def range_sq(n):
# 	for x in range(n):
# 		yield x ** 2  

# for i in range_sq(10):
# 	print(i)


# a = "Today is a good day"
# list = a.split()
# items = [word[-1] for word in list]
# print(items)

# a = ( (n, n**2) for n in range(10) )
# print(a)
# a = sum([i*i for i in range(1,1000000)])
# print(a)

# a = sum(i*i for i in range(1,1000000))
# print(a)

# def sum(a,b,*c):
# 	s = a+b
# 	for i in c:
# 		s = s+i
# 	return s

# def min(*b):
# 	m = b[0]
# 	for i in b:
# 		if i<m:m=i
# 	return m

# def f2(x=0,y=0):
# 	return x*x+y*y*y

# def fare(distance):
# 	booking_fee = 3
# 	starting_price = 3
# 	cost = 0.5 
# 	return booking_fee+starting_price+distance*cost

# def grocery(order):
# 	discount = 25 if order > 200 else 0
# 	tax = 0.07*(order-discount*order/100)
# 	return discount, tax


