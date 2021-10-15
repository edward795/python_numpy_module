# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:57:34 2021

@author: HOME PC
"""
#Iterationg over 1D Arrays

import numpy as np 
arr=np.array([1,2,3,4,5]) 

for i in arr:
    print(i)
    
#Iteration over 2D Arrays

print('Iterationg over 2D Arrays:')
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]]) 

for i in arr2:
    print(i)
    
for i in arr2:
    for j in i:
        print(j,end=" ")
        
#Iterating over 3D Arrays 

print("Iteration over 3D Arrays:")
arr3=np.array([[[1,2,3],[4,5,6]],[[10,11,12],[13,14,15]]])
for i in arr3:
    for j in i:
        for k in j:
            print(k)
            
"""The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.
""" 
print("using nditer():")
arr4=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(arr4):
    print(i)
    
    
arr4=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(arr4,flags=['buffered'],op_dtypes=['S']):
    print(i)
    
print("Iterating with step size:")   
arr4=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(arr4[:,::2]):
    print(i)
    
#enumerate for indexes

arr4=np.array(([1,2,3,4,5]))
for idx,i in np.ndenumerate(arr4):
    print(idx,i)
    
    
arr4=np.array([[1,2,3],[4,5,6]])
for idx,i in np.ndenumerate(arr4):
    print(idx,i)