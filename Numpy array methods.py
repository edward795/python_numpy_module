# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:31:31 2021

@author: HOME PC
"""

import numpy as np 
x=np.array([[0,1],[2,3]]) 
print(x)

y=np.sum(x)
print(y)

z=np.sum(x,axis=1)
print(z)

print(np.repeat(3, 4))