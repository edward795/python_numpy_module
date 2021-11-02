# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:44:36 2021

@author: HOME PC
"""

import numpy as np 
arr=np.array([41,42,43,45]) 

x=[True,False,False,True] 

new_arr=arr[x] 
print(new_arr) 


arr=np.array([56,78,89,90,23]) 
filter_arr=[]
for i in arr:
    if i%2==0:
        filter_arr.append(True) 
    else:
        filter_arr.append(False) 
        
new_arr=arr[filter_arr] 
print(new_arr) 



arr=np.array([41,42,43,44,45])
filter_arr=arr > 42 
new_arr=arr[filter_arr] 

print(new_arr)


arr=np.array([1,2,3,4,5,6,7,8,9,10]) 
filter_arr=arr%2==0 
new_arr=arr[filter_arr]
print(new_arr)