# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:34:29 2021

@author: HOME PC
"""

import numpy as np 
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]]) 
print(arr.shape)


arr2=np.array([1,2,3,4,5],ndmin=5)
print(arr2)
print(arr2.ndim)