# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:11:43 2021

@author: HOME PC
"""

#Array Operations +,-,/,*
import numpy as np 

arr=np.arange(6).reshape(2,3) 
print(arr,end="\n\n")
print(arr+10,end="\n\n") 
print(arr*2,end="\n\n") 
print(arr//2,end="\n\n")


a=np.array([[1,-1],[-1,1]]) 
b=np.array([[1,1],[1,1]])
print(a+b)

print(a*b)


x = np.array([[-1, 1], [-2, 2]])
y = np.array([-10, 10])
print(x * y)