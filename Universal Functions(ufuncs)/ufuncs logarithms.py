# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:32:16 2021

@author: HOME PC
"""

import numpy as np

#log to base 2 
arr=np.arange(1,10) 
arr=np.log2(arr) 
print(arr)

#log to bas 10 
arr=np.arange(1,10)
arr=np.log10(arr) 
print(arr)

#log to any base e-natural log 
arr=np.arange(1,10) 
arr=np.log(arr) 
print(arr)

#log at any base 
from math import log 
nlog=np.frompyfunc(log,2,1) 
res=nlog(100,15)
print(res)