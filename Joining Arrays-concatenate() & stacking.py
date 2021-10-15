# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 17:33:36 2021

@author: HOME PC
"""

import numpy as np 

arr1=np.array([1,2,3,4,5]) 
arr2=np.array([6,7,8,9,10]) 
arr=np.concatenate([arr1,arr2]) 
print(arr) 

#2D array cncatenation 

arr1=np.array([[1,2,3],[5,6,7]]) 
arr2=np.array([[8,9,10],[11,12,13]]) 
arr=np.concatenate((arr1,arr2))
print(arr)

#specifying axis 

arr=np.concatenate((arr1,arr2),axis=1)
print(arr)

#using stacking 

print("Stacking:")
arr1=np.array([1,2,3])
arr2=np.array([4,5,6]) 
arr=np.stack((arr1,arr2)) 
print(arr)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6]) 
arr=np.stack((arr1,arr2),axis=1) 
print(arr)

#stacking along rows - hstack() 
arr1=np.array([1,2,3]) 
arr2=np.array([4,5,6]) 
arr=np.hstack((arr1,arr2)) 
print(arr)

#stacking along columns - vstack() 
arr1=np.array([1,2,3]) 
arr2=np.array([4,5,6]) 
arr=np.vstack((arr1,arr2)) 
print(arr)

#stacking along depth - dstack() 

arr1=np.array([1,2,3]) 
arr2=np.array([4,5,6]) 
arr=np.dstack((arr1,arr2)) 
print(arr)
