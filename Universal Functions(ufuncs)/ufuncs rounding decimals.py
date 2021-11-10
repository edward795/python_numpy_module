# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:05:46 2021

@author: HOME PC
"""

import numpy as np

arr=[-3.1666, 3.6667]
print(arr)

#Truncation
arr=np.trunc(arr)
print(arr)

#fix 
arr=np.fix(arr)
print(arr)

#rounding
arr=np.around(arr)
print(arr)

#ceiling 
arr=np.ceil(arr)
print(arr) 

#floor 
arr=np.floor(arr)
print(arr)