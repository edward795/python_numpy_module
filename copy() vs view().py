# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:10:57 2021

@author: HOME PC
"""

#copy()

import numpy as np 

arr=np.array([1,2,3,4,5]) 
x=arr.copy() 

arr[0]=10 

print(arr) 
print(x)

#view() 


arr1=np.array([1,2,3]) 
y=arr1.view() 

arr1[0]=20 

print(arr1) 
print(y)

y[2]=40

print(arr1) 
print(y)

print("Calling the base attribute to check ownership of array:")

print(x.base) 
print(y.base)