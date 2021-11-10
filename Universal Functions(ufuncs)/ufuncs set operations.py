# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:55:11 2021

@author: HOME PC
"""

import numpy as np 
x=np.array([1,2,2,2,4,4,4,4,5]) 
y=np.unique(x) 
print(y)

#union 
x=np.array([1,2,3,4,5]) 
y=np.array([4,5,6,7,8]) 
arr=np.union1d(x,y) 
print(arr)

#intersection  
arr=np.intersect1d(x,y,assume_unique=True)
print(arr)

#difference 
arr=np.setdiff1d(x,y,assume_unique=True) 
print(arr)

#symmetric difference 
arr=np.setxor1d(x,y,assume_unique=True) 
print(arr)