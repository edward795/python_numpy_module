# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 16:15:55 2021

@author: HOME PC
"""

import numpy as np 

#normal addition 
x=np.array([1,2,3])
y=np.array([2,3,4]) 

arr=np.add(x,y)
print(arr)

#summation
arr=np.sum([x,y])
print(arr)

#summation over an axis 

arr=np.sum([x,y],axis=1)
print(arr)

#cumulative sum 

arr=np.cumsum(x) 
print(arr)