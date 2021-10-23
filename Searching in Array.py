# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 23:14:32 2021

@author: HOME PC
"""

import numpy as np 

arr=np.array([78,34,56,2,3]) 
x=np.where(arr==56) 
print(x)

arr=np.array([2,4,5,2,6,7,2,2])
x=np.where(arr==2) 
print(x)

arr=np.array([1,2,3,4,5,6,7,8,9,10]) 
x=np.where(arr%2==0)
print(x)

"""
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
""" 
arr=np.array([6,7,8,9,10]) 
x=np.searchsorted(arr,7) 
print(x)

#search from right side
x=np.searchsorted(arr,7,side="right") 
print(x)

#search for multiple values
x=np.searchsorted(arr,[3,15])
print(x)