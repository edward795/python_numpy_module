'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import numpy as np 

li=[[1,2,3],[4,5,6]] 

arr=np.array(li)
print(arr)
print()

arr=np.zeros(shape=(2,4))
print(arr)
print()

arr=np.full(shape=(2,3),fill_value=10.5) 
print(arr)
print() 

arr=np.arange(0,10,2.5)
print(arr)
print() 

arr=np.linspace(3,15,5) 
print(arr)