
# Module 2: Data Types
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

# print(1)
# print(1.3)
# print(1+4j)

# a = 1.4354354
# b = 4.45435434
# a,b = 1,8
# print(a+b)
# print("{:0.2f}".format(a))
# print("{1:0.2f}+{0:0.2f}={2:0.2f}".format(a,b,a+b))

# a,b,c= 4,5,6
# d = a+b+c
# print("{1}+{2}+{0}={3}".format(a,b,c,d))

# String
# a = "hello".upper()
# b = " WORLD".lower()
# a = "         hello       ".lstrip()
# b = " world".replace(" world"," alfred")
# print((a+b).upper().capitalize().lower())

# a = " Today is a sunny day"
# b = a.split()
# print(b[0])

# c = "-0-0-".join(b)
# print(c)

# email = "angch@tertiaryinfotech.com"
# domain = email.split("@")
# print(domain)

# a = "Today is a sunny day"
# print(a.find("day",3))

# gene = "atgcgcataaggacat"

# print(gene.find("cat"))
# print(gene.count("cat"))

# name = "Alfred"
# print("Hello {}".format(name))

# country ="France".upper()
# capital ="paris".capitalize()

# print("The capital of {} is {}".format(country,capital))

# List

# a = [3,4,7.5,[4,5],'hi',8]
# print(a)
# print(a[3])
# print(a[0:3])
# print(a[-1])
# print(a.index('hi'))

# a.append(99999)
# print(a)
# a.insert(2,8888)
# print(a)
# a.pop()
# print(a)
# a.remove(8888)
# print(a)

# a = [1,2,3,4,5]
# b = a
# c = a.copy()

# a.append(9999)
# print(a)
# print(b)
# print(c)

# a = [4,7,2,9,3,2]
# a.sort()
# b = sorted(a)
# print(a)
# print(b)
# print(sum(a))
# print(min(a))
# print(max(a))
# print(a.count(2))

# letters =['A','C','C','A','T','T','G','A','C','A']
# print(letters.count('A'))
# print(letters.index('T'))
# letters2 = letters.copy()
# letters2.remove('G')
# letters2.insert(3,'A')
# letters2.reverse()
# print(letters2)

# a = [4,7,2,9,3,2]
# b = [5,6,7]
# print(a+b)

# Tuple
# a = (3,4,6,2,3)
# print(a)
# print(a[2])
# print(sum(a))

#a.append(99999)
#a.insert(3,8888)

# a = (4,7,2,9,3,2)
# b = (5,6,7)
# print(a+b)
# print(a)
# print(b)

# Dictionary

# a = {'a':3,'b':5,'c':6}
# print(a)
# print(a['b'])
# a['d'] = 6
# print(a)

# b = {'e':7,'f':9}
# a.update(b)
# print(a)

# Set

# a = {3,4,5,7}
# b = {4,7,7,3,5,5}
# print(a == b)
# print(a)
# print(b)

# c = {5,6,3,10}
# print(a.union(c))
# print(a.intersection(c))

# Change Type

a = {4,5,6,3}
b = list(a)
print(b)
c = tuple(a)
print(c)
d = set(c)
print(d)