# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:05:03 2021

@author: HOME PC
"""

import numpy as np 

x=np.sin(np.pi/2) 
print(x)

arr=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/6]) 
x=np.sin(arr)
print(x)

#degree --> radians
arr=np.array([90,180,270,360]) 
x=np.deg2rad(arr) 
print(x)

#radians --> degrees
arr=np.array([np.pi/2,np.pi/3,np.pi/6,np.pi/5]) 
x=np.rad2deg(arr) 
print(x)

#finding angles arcsin(),arccos(),arctan() 
print(np.arcsin(1))
print(np.arctan(1))


arr=np.array([1,0.75,0.5]) 
x=np.arcsin(arr) 
print(x)

#hypotenuse from perpendicular & hypotenuse
hypot=3 
perp=4 
x=np.hypot(hypot,perp) 
print(x)