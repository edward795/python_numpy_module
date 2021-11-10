# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:30:06 2021

@author: HOME PC
"""

import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])

w=[]
#normal method
for i,j in zip(x,y):
    w.append(i+j)
print(w)    

#add() ufunc
z=np.add(x,y)
print(z)