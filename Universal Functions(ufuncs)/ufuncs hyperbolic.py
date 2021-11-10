# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:45:50 2021

@author: HOME PC
"""

import numpy as np 

x=np.sinh(np.pi/2) 
y=np.cosh(np.pi/2) 
print(x)
print(y)

arr=np.array([np.pi/2,np.pi/3,np.pi/6]) 
y=np.cosh(arr) 
print(y)

print(np.arcsinh(1))
print(np.arctanh(1/3))

arr=np.array([1,2,3,4,5]) 
x=np.arccosh(arr) 
print(x)