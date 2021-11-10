# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:26:32 2021

@author: HOME PC
"""

import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10]) 
#add
z=np.add(x,y)
print(z)

#subtract 
z=np.subtract(x,y)
print(z)

#mulitply 
z=np.multiply(x,y)
print(z) 

#divide 
z=np.divide(x,y)
print(z)

#power
z=np.power(x,y)
print(z)

#mod() remainder() 
z=np.mod(x,y)
print(z)

z=np.remainder(x,y)
print(z)

z=np.divmod(x,y)
print(z)

z=[-1,-2,-3,-4]
z=np.absolute(z)
print(z)