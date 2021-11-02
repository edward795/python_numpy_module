# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:37:46 2021

@author: HOME PC
"""

"""
random.randint(100) --> 82 
random.rand() --> 0.5628718526875489


random.randint(range,dimension) --> Integer random numbers
random.rand(dimension)  --->  Float random numbers 

eg 1: random.randint(100,5) -->  [90 73 94 57 13]
eg 2:random.randint(100,size=(2,3)) --> [[33 53 60]
                                         [26 70 44]]
eg 3:random.rand(5) --> [0.12022896 0.13206681 0.48868538 0.388493   0.77282544]
eg 4:random.rand(2,3) --> [[0.54141224 0.17859752 0.50114937]
                           [0.78297693 0.5059648  0.93584561]]
eg 5:random.choice([2,3,4,5])
eg 6:random.choice([45,67,34,23])

"""

from numpy import random
x=random.randint(100) 
print(x)

y=random.rand() 
print(y)

arr=random.randint(100,size=5)
print(arr) 

arr=random.randint(100,size=(2,3)) 
print(arr)

arr=random.rand(5) 
print(arr)

arr=random.rand(2,3)
print(arr)

x=random.choice([67,89,23,12])
print(x)

y=random.choice([23,67,89,12],size=(3,5))
print(y)
