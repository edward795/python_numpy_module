# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:35:33 2021

@author: HOME PC
"""

import numpy as np
x=np.array([1,2,3,4]) 
y=np.array([2,2,2,2]) 

#product 
arr=np.prod(x)
print(arr)

#product of 2 arrays 
arr=np.prod([x,y])
print(arr)

#product over an axis 
arr=np.prod([x,y],axis=1) 
print(arr)

#cumulative product 
arr=np.cumprod(x)
print(arr)