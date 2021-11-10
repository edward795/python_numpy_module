# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:59:29 2021

@author: HOME PC
"""

import numpy as np
x=5 
y=15 
#gcd of 2 nums
res=np.gcd(x,y) 
print(res)

#gcd of an array of elements 
arr=np.array([1,2,3,4,5]) 
res=np.gcd.reduce(arr) 
print(res)