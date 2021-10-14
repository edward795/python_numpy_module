# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:43:27 2021

@author: HOME PC
"""

#reshaping arrays 

import numpy as np 


#converting to 2D
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)

newarr=arr.reshape(4,3)
print(newarr)

#converting to 3D
arr2=arr.reshape(2,3,2)
print(arr2)

#converting to 1D or flattening
newarr=arr2.reshape(-1)
print(newarr) 

#unknown dimension 
arr=np.array([1,2,3,4,5,6,7,8]) 
newarr=arr.reshape(2,2,-1)
print(newarr)