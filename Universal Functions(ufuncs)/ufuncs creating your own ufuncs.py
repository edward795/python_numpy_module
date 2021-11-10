# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:55:30 2021

@author: HOME PC
"""
"""
To create you own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""
import numpy as np 

def mul(x,y):
    return x*y 

mymul=np.frompyfunc(mul, 2, 1) 
print(mymul([1,2,3],[4,5,6]))

#checking if a function is ufunc 

print(type(np.add))
print(type(mymul))