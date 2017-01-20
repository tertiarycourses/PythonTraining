# Python Essential Training
# Module 12: Intro to Numpy, Matplotlib, Pandas
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

# Numpy demo
a = [3,4,5,6]
b = [6,5,4,3]
print(a+b)
a1 = np.array(a)
b1 = np.array(b)
print(a1-b1)

# Matplolib demo
x = np.linspace(0,4*np.pi,200)
y = np.sin(x)
plt.plot(x,y)
plt.show()

# Pandas demo
a = [3,4,5,6]
b = [6,5,4,3]
a1 = np.array(a)
b1 = np.array(b)
#print(a1+b1)
a2 = pd.Series(a,index=['a','b','c','d'])
b2 = pd.Series(b,index=['e','f','b','a'])
print(a2)
print(b2)
print(a2+b2)

