# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:49:47 2021

@author: HOME PC
"""

import numpy as np

x = np.arange(30).reshape(3,5,2)
print(x[-1, 2:-1, -1])

import numpy as np

x = np.arange(30).reshape(3,5,2)
print(x[1][::2][1])

import numpy as np

x = np.arange(4)
print(x.flatten())


import numpy as np

x = np.arange(30).reshape(3,5,2)
print(x[1,::2,1])

import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 1]])

import numpy as np

x = np.arange(30).reshape(5,6)
print(x.argmax(axis=1))

import numpy as np

x = np.arange(30).reshape(3,5,2)
print(x[1][::2][1])

import numpy as np

x = np.array([[3.2, 7.8, 9.2],
             [4.5, 9.1, 1.2]], dtype='int64')
print(x.itemsize)


import numpy as np

x = np.arange(30).reshape(3,5,2)
print(x[-1, 2:-1, -1])

import numpy as np

x = np.array([[-1,0,1], [-2, 0, 2]])

y = np.zeros_like(x)
print(y)

import numpy as np

x = np.arange(30).reshape(3,5,2)
print(x[1,::2,1])

import numpy as np

x = np.array([[-2], 
              [2]])
y = np.array([[-3, 3]])
print(x.dot(y))

import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 1]])