# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 21:21:36 2021

@author: HOME PC
"""

import numpy as np 

#1-D arr
arr=np.array([1,2,3,4,5]) 
print(arr[2]) 

#negative indexing
print(arr[-1])

print(arr[0]+arr[1]+arr[2])

#2-D arr
arr_2d=np.array([[1,2,3],[4,5,6]]) 
print(arr_2d[0][1])

#negative indexing to print last element of first row
print(arr_2d[0][-1])

#3-D array 
arr_3d=np.array([[[1,2,3],[4,5,6],[7,8,9]]]) 
print(arr_3d[0][1][0])

arr4=np.array([1,2,3,4,5,6,7,8,9,10]) 
print(arr4[0:9:2])