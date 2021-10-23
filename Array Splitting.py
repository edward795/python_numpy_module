# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:13:35 2021

@author: HOME PC
"""

#Splitting 1D-Array

import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9]) 
new_arr=np.array_split(arr,3) 
print(new_arr)

for i in new_arr:
    print(i)
    
print(new_arr[0])


#Splitting 2D-Arrays

arr=np.array([[1,2,3],[4,5,6],[7,8,9],[11,12,13],[14,15,16],[17,18,19]])
print(arr)
new_arr=np.array_split(arr,3)
print(new_arr)

#Splitting 2D-Arrays specifying axis=1 based on row 

new_arr=np.array_split(arr,3,axis=1)
print(new_arr)

#Using hsplit(),vsplit(),dsplit() 
new_arr=np.hsplit(arr,3) 
newarr2=np.vsplit(arr,3)
print(new_arr)
print(newarr2)

arr=np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])
new_arr=np.dstack(arr) 
print(new_arr)