# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 21:07:16 2021

@author: HOME PC
"""

import numpy as np 

arr=np.array([[1,2,3],[4,5,6]]) 
print(arr) 

#ndim 
print(arr.ndim)

#shape 
print(arr.shape)

#size 
print(arr.size)

#dtype 
print(arr.dtype)

#itemsize 
print(arr.itemsize)

#nbytes 
print(arr.nbytes)

#dtype float
arr_1=np.array([1,2,3,4,5],dtype='float64') 
print(arr_1)

#higher dimensional arrays 
arr_2=np.array([1,2,3,4,5],ndmin=5) 
print(arr_2.ndim)