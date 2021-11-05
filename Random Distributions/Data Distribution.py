# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:06:29 2021

@author: HOME PC
"""

from numpy import random
distribution=random.choice([3,5,7,9],p=[0.2,0.4,0.4,0],size=100)
print(distribution)

distribution=random.choice([12,14,15,17],p=[0.1,0.3,0.5,0.1],size=(3,5)) 
print(distribution)


