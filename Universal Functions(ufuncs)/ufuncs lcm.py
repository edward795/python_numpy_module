# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:48:50 2021

@author: HOME PC
"""

import numpy as np
x=3 
y=4

#lcm
lcm=np.lcm(x,y)
print(lcm)

#lcm of a range of numbers 
arr=np.array([1,2,3,4,5]) 
lcm=np.lcm.reduce(arr)
print(lcm)

arr=np.arange(1,10) 
lcm=np.lcm.reduce(arr)
print(lcm)