# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 21:09:39 2021

@author: HOME PC
"""

"""
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""

#datatypes 

import numpy as np 
arr=np.array(["apple","banana"]) 
print(arr.dtype)

arr2=np.array([1,2,3,4,5]) 
print(arr2.dtype)

#specifying datatypes during initialization 

arr3=np.array([1,2,3,4,5],dtype="S") 
print(arr3.dtype)

#creating an array with integer datatypes of 4 bytes 

arr4=np.array([1,2,3,4,5],dtype="i4")
print(arr4.dtype)


#copying array with datatype 

arr5=np.array([1,2,3,4,5],dtype="i4") 
newArr=arr5.astype("i") 
print(newArr)
print(newArr.dtype)

#change datatype using astype() 

newArr1=arr5.astype("S")
print(newArr1) 
print(newArr1.dtype)

newArr2=arr5.astype(bool)
print(newArr)
print(newArr.dtype)