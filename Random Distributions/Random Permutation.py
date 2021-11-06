# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:06:29 2021

@author: HOME PC
"""

from numpy import random 
import numpy as np 
arr=np.array([5,7,8,9,3]) 
#shuffle makes changes to original array
print(random.shuffle(arr))
#permutation returns a new instance of an array 
new_arr=random.permutation(arr)
print(new_arr)
