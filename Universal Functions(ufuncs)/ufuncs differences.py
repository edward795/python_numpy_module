# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:44:55 2021

@author: HOME PC
"""

import numpy as np 
x=np.array([0, 15, 25, 5])

#discrete differences
arr=np.diff(x) 
print(arr)

#succesive iteration of discrete differences - specify n(eg: n=2)
arr=np.array([1,2,3,4])
arr=np.diff(arr,n=2) 
print(arr)